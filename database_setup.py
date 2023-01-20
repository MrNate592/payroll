import pymysql
import dbinfo



# Input below the mySQL sever detials
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS payroll")

mydb = dbinfo.connect()


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE  IF NOT EXISTS user_information (ID int not null primary key auto_increment, UserID int not null unique,Username VARCHAR(100) not null, Password VARCHAR(100) not null, Name VARCHAR(255) not null, Address VARCHAR(255) not null, Gender VARCHAR(50) not null, Department VARCHAR(100) not null, DOB DATE not null, NIS VARCHAR(100) not null UNIQUE, Hours VARCHAR(10) not null, Bank VARCHAR(100) not null, BankID VARCHAR(100) not null, AccountNumber VARCHAR(100) UNIQUE not null, SalaryID Varchar(100) UNIQUE not null, Paydate DATE not null, WageRate VARCHAR(100) not null, Medical VARCHAR(100) not null,  Tax VARCHAR(100) not null, BasicSalary VARCHAR(100) not null, NetSalary VARCHAR(100) not null, SalaryReceipt VARCHAR(1000) not null)")
mySql_insert_query = """INSERT IGNORE user_information (ID, UserID,Username,Password,Name, Address, Gender,Department,DOB,NIS,Hours,Medical,Bank,BankID,AccountNumber,SalaryID,Paydate,BasicSalary) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

record = ('1', '12345','admin','admin', 'Matthew Hamilton ', '3787 Crestview Manor', 'Male','Marketing','2000-02-11','81238321','40','2000','GBTI','592','56127312','901-59','2022-11-28','100000')
mycursor.execute(mySql_insert_query, record)
mydb.commit()
