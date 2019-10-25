import sqlite3 as sql

database = sql.connect("./EmployeeData.db")
cursor = database.cursor()

# Create table
createQuery = '''CREATE TABLE EMPLOYEE (
        EMPLOYEE_ID VARCHAR(4) PRIMARY KEY,
        NAME VARCHAR(30),
        PHONE_NUMBER INT,
        SALARY INT
    )'''
try:
    cursor.execute(createQuery)
    database.commit()
except:
    print("Table Exits")

# Data
employeeData = [
    ("101", "Employee1", 9090, 9000000),
    ("102", "Employee2", 1234, 1000000),
    ("103", "Employee3", 4567, 2000000),
    ("104", "Employee4", 7890, 3000000),
    ("105", "Employee5", 1212, 4000000),
]

# Insert 
insertQuery = '''INSERT INTO EMPLOYEE (EMPLOYEE_ID, NAME, PHONE_NUMBER, SALARY) 
                 VALUES (?, ?, ?, ?)'''
try:
    cursor.executemany(insertQuery, employeeData)
    database.commit()
    print("Data inserted")
except sql.IntegrityError:
    database.rollback()
    print("Primary Key Conflict")

# Select all 
selectQuery = "SELECT * FROM EMPLOYEE"
cursor.execute(selectQuery)
allEmployees = cursor.fetchall()
print("All Employee Data")
for employee in allEmployees:
    print(employee)

# Conditional Select 
print ("Data of Employee with ID 103:")
selectQuery = "SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID = 103"
cursor.execute(selectQuery)
employee = cursor.fetchone()
print(employee) 

# Updating
updateQuery = "UPDATE EMPLOYEE SET SALARY = ? WHERE EMPLOYEE_ID = ?"
updateDetails = (1, 103)
cursor.execute(updateQuery, updateDetails)
database.commit()
print("Updated Employee 103")

# Select all 
selectQuery = "SELECT * FROM EMPLOYEE"
cursor.execute(selectQuery)
allEmployees = cursor.fetchall()
print("Employee Data after update")
for employee in allEmployees:
    print(employee)

# Deleting 
deleteQuery = "DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID = ?"
deleteDetails = (103,)
cursor.execute(deleteQuery, deleteDetails)
database.commit()
print("Deleted Employee 103")

# Select all 
selectQuery = "SELECT * FROM EMPLOYEE"
cursor.execute(selectQuery)
allEmployees = cursor.fetchall()
print("Employee Data after delete")
for employee in allEmployees:
    print(employee)



database.close()
