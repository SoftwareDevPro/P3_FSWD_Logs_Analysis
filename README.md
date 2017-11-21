
| Name: Chris Adamson                          |
|:---------------------------------------------|
| Course: Full Stack Web Developer Nanodegree  |
| Project: Logs Analysis                       |

**Purpose of the Project:**

The purpose of the project is to build an internal reporting tool that uses information from a news database.  The database from which the data is pulled contains authors with biographical information, articles (with the title, lead, and body giving basic information about the article), and a log from the news website with the URL path retrieved, IP that did the request, HTTP method, HTTP status of the request, and time of the request.

The three specific three questions that are answered:

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

**Building the run-time environment:**

Three software components are essential for the run-time environment to work correctly:

1. A Python interpreter, which interprets and executes the logs_analysis script.  It can be downloaded [here](https://www.python.org/downloads).  Python 3.x or 2.x will work.

2. PostgreSQL, which is the database system that reads the database, executes the SQL queries passed to it, and returns the resulting data.  It can be downloaded [here](https://www.postgresql.org/download/).

3.  The psycopg2 Python library which is a PostgreSQL adapter, which implements the Python DB-API, and allows access to features provided by the PostgreSQL database system.  The installation instructions are [here](http://initd.org/psycopg/docs/install.html).

**How to run the program:**

1. Download the data, decompress it, and load it into the database (see instructions below).
2. Verify that run-time environment is ready (see instructions above).
3. Open a command line terminal (for this project a pre-setup vm was used).
4. Change to the directory where logs_analysis.py is located.
5. Run “```python logs_analysis.py```” or “```python3 logs_analysis.py```”.

**Downloading the data and loading uncompressed Data into the news database:**

1. The newsdata.sql data file for the logs analysis program can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Once the compressed data file has been downloaded, de-compress it (e.g. using Winzip, unzip or another compression program).
3. Execute the following psql command to load the uncompressed data into the database: "```psql -d news -f newsdata.sql```".

**Program Design:**

For this program, the design was kept simple, in a bigger project, modules, design patterns, name spacing, functions, etc. might be taken into consideration.  I used three separate SQL strings, then followed each SQL declaration with a cursor creation, execution of that cursor, and retrieve all the results from that cursor.  After the retrieval of the query data, I printed out the question being answered, followed by the results of the query.  The other consideration was being able to run under both Python 2.x and 3.x.  The program was developed under 3.x, and tested with both versions of Python.
