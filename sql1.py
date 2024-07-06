#
#show Connection object

import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
print(connection)


'''Create database'''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database senthil007")  """




'''show all databases with in root user'''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
   print(x)  """





'''Create table '''
""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
cursor=connection.cursor()
cursor.execute("CREATE TABLE departments (department_id INT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
   print("\t",x) """


""" import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
cursor=connection.cursor()
cursor.execute("CREATE TABLE employees (employee_id INT PRIMARY KEY,employee_name VARCHAR(100),department_id INT)")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
    print("\t",x) """ 

import pymysql as mysql
connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
cursor=connection.cursor()
s="insert into employees values(%s,%s,%s)"
t=(1,"harish",1)
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted")


# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
# cursor=connection.cursor()
# s="insert into employees values(%s,%s,%s)"
# t=[(2,"harish",1),(3,"harish",2)]
# cursor.executemany(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted")

# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
# cursor=connection.cursor()
# cursor.execute("select * from employees")
# result=cursor.fetchall()
# print("Content in the python :")
# for x in result:
#    print("\t",x)




# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
# cursor=connection.cursor()
# sql = "update employees set employee_name='bala' where employee_id=1;"
# cursor.execute(sql)
# connection.commit()


# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire",database="senthil007")
# cursor=connection.cursor()
# sql = "DELETE FROM employees WHERE employee_id=1"
# cursor.execute(sql)
# connection.commit()
# print(cursor.rowcount, "record(s) deleted")





# import pymysql as mysql
# connection = mysql.connect(host="localhost",user="root",password="livewire")
# cursor=connection.cursor()
# #cursor.execute("create database database01") 
# cursor.execute("show databases")
# for x in cursor:
#    print(x) 
# cursor.execute("use database01") 
# #cursor.execute("CREATE TABLE departments (department_id INT PRIMARY KEY,department_name VARCHAR(50))")
# cursor.execute("show tables")
# print("Number of tables in database :")
# for x in cursor:
#      print("\t",x) 
# s="insert into departments values(%s,%s)"
# t=(2,"harish")
# cursor.execute(s,t)
# connection.commit()
# print(cursor.rowcount,"new row inserted",cursor.lastrowid) 
# cursor.execute("select * from departments")
# result=cursor.fetchall()
# print("Content in the python :")
# for x in result:
#    print("\t",x)
# sql = "update departments set department_name='bala' where department_id=1;"
# cursor.execute(sql)
# connection.commit() 
# sql = "DELETE FROM departments WHERE department_id=1"
# cursor.execute(sql)
# connection.commit()
# print(cursor.rowcount, "record(s) deleted")  
