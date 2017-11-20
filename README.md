
| Name: Chris Adamson                          |
|:---------------------------------------------|
| Course: Full Stack Web Developer Nanodegree  |
| Project: Logs Analysis                       |

**How to run the program:**

1.	Verify that Python is installed (Python 2.x or 3.x will work).
2.	Open a command line terminal (for this project a pre-setup vm was used).
3.	Change to the directory where logs_analysis.py is located.
4.	Run “python logs_analysis.py” or “python3 logs_analysis.py”.

**Program Design:**

For this program, the design was kept simple, in a bigger project, modules, design patterns, name spacing, functions, etc. might be taken into consideration.  I used three separate SQL strings, then followed each SQL declaration with a cursor creation, execution of that cursor, and retrieve all the results from that cursor.  After the retrieval of the query data, I printed out the question being answered, followed by the results of the query.  The other consideration was being able to run under both Python 2.x and 3.x.  The program was developed under 3.x, and tested with both versions of Python.

**View Definitions:**

The end result did not use view definitions; however, during the process of developing and exploration of the data for the third query (days with more than 1% of requests leading to errors), I did test out a solution using view definitions:

```
CREATE OR REPLACE VIEW LogErrors AS
SELECT to_char(log.time, 'Month DD, YYYY') as Date, status, COUNT(*) AS NumErrors
FROM log
GROUP BY Date, status
HAVING status!='200 OK';

CREATE OR REPLACE VIEW LogGood AS
SELECT to_char(log.time, 'Month DD, YYYY') as Date, status, COUNT(*) AS NumGood
FROM log
GROUP BY Date, status
HAVING status='200 OK';

SELECT LogGood.Date, (NumErrors*1.0/NumGood*1.0)*100 AS Pct
FROM LogGood
JOIN LogErrors ON LogGood.Date=LogErrors.Date
WHERE (NumErrors*1.0/NumGood*1.0)*100>=1.0;
```
