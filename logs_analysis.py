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

for result in results:
    str = "\"%s\" - %d views" % (result[0], result[1])
    print(str)

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

for result in results:
    str = "%s - %d views" % (result[0], result[1])
    print(str)

# Query 3: On which days did more than 1% of requests lead to errors?

sql3 = '''
SELECT good.Date as date,
       to_char((errors.NumErrors*1.0/good.NumGood)*100,'999.99') as pct
FROM
(SELECT to_char(log.time, 'FMMonth DD, YYYY') as Date,
        status,
        COUNT(*) AS NumGood
 FROM log GROUP BY Date, status HAVING status='200 OK') good
JOIN
(SELECT to_char(log.time, 'FMMonth DD, YYYY') as Date,
        status,
        COUNT(*) as NumErrors
 FROM log GROUP BY Date, status HAVING status!='200 OK') errors
ON
good.Date=errors.Date
WHERE
(errors.NumErrors*1.0/good.NumGood)*100 >= 1.0
ORDER BY
pct;
'''

cur = conn.cursor()
cur.execute(sql3)
results = cur.fetchall()

print("\nOn which days did more than 1% of requests lead to errors?\n")

for result in results:
    str = "%s - %s%% errors" % (result[0], result[1])
    print(str)

cur.close()

# Close communication with the database
conn.close()
