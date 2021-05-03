import sqlite3
conn = sqlite3.connect('student1.sqlite')
print("opened database sucessfully")

conn.execute('''Create Table student
				(Id int primary key not null,
				 name varchar(10) not null,
				 branch varchar(5),
				 dept varchar(5),
				 year int,
				 semester int )''')

conn.execute('''insert into student (id,name,branch,dept,year,semester) values (1,'Aditya','IT','ICT',3,5)''')
conn.execute('''insert into student (id,name,branch,dept,year,semester) values (2,'Aayush','IT','ICT',3,5)''')
conn.execute('''insert into student (id,name,branch,dept,year,semester) values (3,'Abhi','CCE','ICT',3,5)''')
conn.execute('''insert into student (id,name,branch,dept,year,semester) values (4,'Hrithik','IT','ICT',1,2)''')
id,name,branch,dept,year,semester = 17,'ravi','IT','ICT',3,5
conn.execute('''insert into student (id,name,branch,dept,year,semester) values (?,?,?,?,?,?)''',(id,name,branch,dept,year,semester))

conn.commit()

print("Records Entered Database Perfectly")
cursor = conn.execute('Select * from Student')
for tuples in cursor:
	print('ID={} ,Name={} ,Branch={} ,Department={} ,Year={} ,Semester={}'.format(tuples[0],tuples[1],tuples[2],tuples[3],tuples[4],tuples[5]))

conn.execute('update student set semester = 2 where id=17')
conn.execute('delete from student where id = 4')
conn.commit()
cursor = conn.execute('Select * from student')
for tuples in cursor:
	print('ID={} ,Name={} ,Branch={} ,Department={} ,Year={} ,Semester={}'.format(tuples[0],tuples[1],tuples[2],tuples[3],tuples[4],tuples[5]))
