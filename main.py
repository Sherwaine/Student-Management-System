import mysql.connector
mydb = mysql.connector.connect(host="localhost" , user="root",passwd="02121993")
mycursor = mydb.cursor()

#if studentdb doesn't exists then it will be created
mycursor.execute("create database if not exists studentdb") 
mycursor.execute("use studentdb")

#if studentsinfo table doesn't exists then it will be created
mycursor.execute("create table if not exists studentsinfo(sch_id varchar(50),name varchar(100),course varchar(50), courseID varchar(50), coursemarks varchar(150),phone varchar(150))")

#if teacher table doesn't exists then it will be created
mycursor.execute("create table if not exists teacher(id char(100),password varchar(150))")
mydb.commit()

########################################

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    var1=str(input("Enter the sch id. of the student:"))
    var2=str(input("Enter the name of the student:"))
    var3=str(input("Enter the course of the student:"))
    var6=str(input("Enter the course id of the student:"))
    var4=str(input("Enter the coursemark of the student:"))
    var5=str(input("Enter the phone no. of the student:"))
    mycursor.execute("insert into studentsinfo values('"+var1+"','"+var2+"','"+var3+"','"+var6+"','"+var4+"','"+var5+"')")
    mydb.commit()
    print("Data saved successfully!")
    input("Press Enter to continue!")
    display_menu()
    return

###########################################

def sview_students():
    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")
    a=input("Enter the sch id:")
    mycursor.execute("select name,course,coursemarks from studentsinfo where sch_id=('"+a+"')")
    records = mycursor.fetchall()
    row_no=0
    if records:
            for rows in records :
                row_no+=1
                print("******************************","Student Record","******************************")
                print("\t             Name: ", rows[0])
                print("\t           Course: ", rows[1])
                print("\t           Course Grade: ", rows[2])
                print()
    input("Press Enter to continue!")
    start()
    return

def view_students():
    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")
    mycursor.execute("select * from studentsinfo")
    for i in mycursor:
        print(i)
    input("Press Enter to continue!")
    display_menu()
    return

##############################################################

def search_student():
    print("------------------------")
    print("--- Search Student ---")
    print("------------------------")
    a=input("Enter the sch id. of the student:")
    mycursor.execute("select * from studentsinfo where Sch_id=('"+a+"')")
    result=mycursor.fetchall()
    if len(result)==0:
        print("Enter valid sch no.!")    
    else:
        for i in result:
            print(i)
    input("Press Enter to continue!")
    display_menu()
    return

#########################################################################

def update_student():
    print("------------------------")
    print("--- Update Student ---")
    print("------------------------")
    var1=str(input("Enter the sch id. of the student:"))
    var7=str(input("Enter the course id of the student:"))
    var2=str(input("Enter the name of the student:"))
    var3=str(input("Enter the course enrolled:"))
    var4=str(input("Enter the course grade:"))
    var5=str(input("Enter the phone no. of the student:"))
    mycursor.execute("update studentsinfo set name=('"+var2+"'),course=('"+var3+"'),coursemarks=('"+var4+"'),phone=('"+var5+"') where sch_id=('"+var1+"') and courseID=('"+var7+"')")
    mydb.commit()
    print("Data updated successfully!")
    input("Press Enter to continue!")
    display_menu()
    return

#######################################################################

def delete_student():
    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1=input("Enter the sch no. of the student:")
    var2=input('Enter CourseID')
    mycursor.execute("delete from studentsinfo where sch_id=('"+var1+"') and courseID=('"+var2+"')")    
    mydb.commit()
    print("Data deleted successfully!")
    input("Press Enter to continue!")
    display_menu()
    return

#######################################################################

def exit_program():    
    print("---------------------------------")
    print(" Thank you for using our system!")
    print("          Goodbye             ")
    print("---------------------------------")

####################################################################

def display_menu():
    print("1: Add New Student")
    print("2: View Students")	
    print("3: Search Student")
    print("4: Update Student")
    print("5: Delete Student")
    print("6: Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        exit_program()
    else:
        print("invalid")    

##############################################################

def register():
    print("-------------------------")
    print("--------Register---------")
    print("-------------------------")
    id=str(input("Enter your Id:"))
    password=str(input("Enter your Password:"))
    mycursor.execute("insert into teacher values('"+id+"','"+password+"')")
    mydb.commit()
    print("Registered successfully!")
    input("Press Enter to continue!")
    login()
    return

####################################################################

def login():
    print("-------------")
    print("--- login ---")
    print("-------------")
    id=input("Enter the id:")
    password=input("Enter the password:")
    mycursor.execute("select * from teacher where id=('"+id+"') and password=('"+password+"')")
    result=mycursor.fetchall()
    if len(result)==1:
        print("-------------------------------------")
        print("--Welcome",id,"what you want to do!--")
        print("-------------------------------------") 
        display_menu()       
    else:
        print("Enter valid Id and Password!")
        login()

###########################################################################

def slogin():
    print("-------------")
    print("--- login ---")
    print("-------------")
    id=input("Enter the sch id:")
    password=input("Enter the phone no:")
    mycursor.execute("select * from studentsinfo where sch_id=('"+id+"') 1 phone =('"+password+"')")
    result=mycursor.fetchall()
    if len(result)==1:
        sview_students()
    else:
        print("Enter valid Sch Id and Phone Number!")
        slogin()
        return

############################################################################

def start():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")    
    print("1: Student Login")
    print("2: Teacher Login")
    choice = input("Enter your choice: ")
    if choice == '1':
        slogin()
    elif choice == '2':
        tstart()
    else:
        print('Wrong input')
        print('Try Again')
        start()

##############################################################################

def tstart():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")    
    print("1: Login")
    print("2: Register")
    choice = input("Enter your choice: ")
    if choice == '1':
        login()
    elif choice == '2':
        register()
    else:
        print('Wrong input')
        print('Try Again')
        start()

start()