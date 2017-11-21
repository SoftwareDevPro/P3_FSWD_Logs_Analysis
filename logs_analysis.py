#!/usr/bin/python3

# Name: Chris Adamson
# Course: Full Stack Web Developer Nanodegree
# Project: Logs Analysis

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=news")

#  Query 1: What are the most popular three articles of all time?
sql1 = '''
SELECT
title, sub.total
FROM
articles
JOIN
(select substring(path from 10) AS slug, COUNT(*) as total
 from log group by slug) sub
ON articles.slug=sub.slug
ORDER BY sub.total DESC
LIMIT 3;
'''

cur = conn.cursor()
cur.execute(sql1)
results = cur.fetchall()

print("What are the most popular three articles of all time?\n")

for title, views in results:
    print('"{}" - {} views'.format(title, views))

cur.close()

# Query 2: Who are the most popular article authors of all time?

sql2 = '''
SELECT
name, sum(log.total) as views
FROM
articles
JOIN
(select substring(path from 10) AS slug, COUNT(*) AS total
 from log group by slug) log
ON articles.slug=log.slug
JOIN authors ON authors.id=articles.author
GROUP BY name
ORDER BY views DESC;
'''

cur = conn.cursor()
cur.execute(sql2)
results = cur.fetchall()

print("\nWho are the most popular article authors of all time?\n")

for author, views in results:
    print('{} - {} views'.format(author, views))

# Query 3: On which days did more than 1% of requests lead to errors?

sql3 = '''
SELECT to_char(good.Date, 'FMMonth DD, YYYY') as date,
       to_char((NumErrors*1.0/(NumGood+NumErrors))*100,'999.99') as pct
FROM
(SELECT date(log.time) as Date, COUNT(*) AS NumGood
 FROM log WHERE status='200 OK' GROUP BY Date) good
JOIN
(SELECT date(log.time) as Date, COUNT(*) as NumErrors
 FROM log WHERE status!='200 OK' GROUP BY Date) errors
ON
good.Date=errors.Date
WHERE
(NumErrors*1.0/(NumGood+NumErrors))*100 >= 1.0
ORDER BY
pct;
'''

cur = conn.cursor()
cur.execute(sql3)
results = cur.fetchall()

print("\nOn which days did more than 1% of requests lead to errors?\n")

for day, pct in results:
    print('{} - {}% errors'.format(day, pct))

cur.close()

# Close communication with the database
conn.close()
