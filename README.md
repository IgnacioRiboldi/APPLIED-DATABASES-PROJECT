# APPLIED-DATABASES-PROJECT
FINAL PROJECT FOR ATU

Before start using the app:

Install Python:

Two ways: 
1- Terminal -> python (it might open store to download it)
2- https://www.python.org/downloads/

Install "pymysql":

Run in your terminal:

python -m pip install pymysql so we can connect to MYSQL with python.

Install also Neo4j

python -m pip install neo4j so we can connect to Neo4j with python.

Activate Neo4j.

Go to -> C:\Users\appDB\Documents\neo4j-community-5.26.19\conf -> Open neo4j.conf -> Make sure dbms.default_database=appdbprojNeo4j
After that go to -> C:\Users\appDB\Documents\neo4j-community-5.26.19\bin -> cmd 
Once the commander is open run -> neo4j.bat console
Open http://localhost:7474/ and run the query given on: appdbprojNeo4j to make sure you have the connections.

Sources:

Menu:
https://medium.com/@firozkaif27/create-a-python-menu-to-run-various-commands-7be4d70cc127
https://stackoverflow.com/questions/19964603/creating-a-menu-in-python

SQL Local connection:
https://help.interfaceware.com/kb/1062/2
https://www.w3schools.com/php/php_mysql_connect.asp

Cursor:

https://www.geeksforgeeks.org/sql/what-is-cursor-in-sql/

Fetchall and Fetchone

Fetchall: Return all (remaining) rows of a query result as a list. Return an empty list if no rows are available. Note that the arraysize attribute can affect the performance of this operation.

Fetchone: If row_factory is None, return the next row query result set as a tuple. Else, pass it to the row factory and return its result. Return None if no more data is available.

https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone

Inner joins

https://www.w3schools.com/sql/sql_join_inner.asp

https://www.postgresql.org/docs/current/queries-table-expressions.html

Input Validation:

https://www.geeksforgeeks.org/python/input-validation-in-python/

Date and Time

https://www.w3schools.com/python/python_datetime.asp

Commit

https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html

Neo4j connection:

https://neo4j.com/docs/python-manual/current/

https://www.datacamp.com/tutorial/neo4j-tutorial?utm_cid=23781701478&utm_aid=196565213035&utm_campaign=260417_1-ps-dscia~amx-tofu~python_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1007850-&utm_mtd=p-c&utm_kw=python%20user%20input&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~emea-en~amx~tofu~tutorial~python&gad_source=1&gad_campaignid=23781701478&gbraid=0AAAAADQ9WsGvoS6UtOIknIAJ57uB4Yuar&gclid=CjwKCAjw-8vPBhBbEiwAoA39WuFzNtHAz19u6EC2iKNw31sAj26wxEZ-MBPEt6UWaH7Hm26LyyiHlRoCMiEQAvD_BwE

https://www.youtube.com/watch?v=ytzMN-b6v7E

Neo4j relationships

https://neo4j.com/docs/graph-data-science/current/management-ops/graph-write-to-neo4j/write-back-relationships/

Cache function 

https://docs.python.org/3/library/functools.html#functools.lru_cache

https://en.wikipedia.org/wiki/Cache_(computing)