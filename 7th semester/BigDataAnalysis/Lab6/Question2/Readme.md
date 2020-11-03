## Cassandra Lab

### Library Keyspace

1. Create a Keyspace by name library

   ![](Images/createKeyspace.png)

2. Create a column family by name LibraryInfo with attributes id Primary Key, counterValue of type Counter, studentName bookName, bookId, dateOfIssue

   ![](Images/createColumnFamily.png)

3. Insert values.

   ![](Images/insert.png)

4. Display the details of the table created and increase the value of the counter

   ![](Images/select.png)

   ![](Images/increaseCounter.png)

5. Export the created column to a csv file

   ![](Images/export.png)

   The CSV file can be found [here](library.csv)

6. Import a given csv dataset from local file system into Cassandra column family

   ![](Images/import.png)
