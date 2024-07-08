import pymysql as mysql
a=mysql.connect(host="localhost",user="root",password="livewire",database="python10")
print(a)
cursor=a.cursor()
cursor.execute("create table py(name varchar(255),age int)")
cursor.execute("create table py1(id int auto_increment primary key,name varchar(255))")
cursor.execute("show tables")
print("number of tables in database:")
for x in cursor:
    print("\t",x)
