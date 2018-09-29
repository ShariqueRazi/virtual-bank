import os
import sys
import pymysql as sql
import re
import random
import datetime
import transfermoney
import loan
import transaction
import change

def transaction(name, cus_id,cus_balance):
    qry ="INSERT INTO transaction (Name, Account_No, Balance) VALUES ('%s', '%s', '%s')" %(name, cus_id,cus_balance)
    con1=sql.connect("localhost","root","purbalok1","bank")
    cu1=con1.cursor()
    cu1.execute(qry)
    con1.commit()
    con1.close()

count=1
def adminlogin():
    global count
    count_cu=0
    os.system("cls")
    adname=input("Enter the name :")
    adacc=input("Enter the bank id ")
    adpas=input("Enter the password ")
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    qry="SELECT * FROM admin WHERE Name ='%s' and password='%s' and Bank_id='%s'"%(adname,adpas,adacc)
    cu.execute(qry)
    count_cu=cu.rowcount
    con.close()

    if count_cu>0:
        os.system("cls")
        print("1> Show customer details:")
        print("2> Show transaction of customer")
        print("3> Change Credentials")
        choice2=int(input("Enter Your choice: "))
        if choice2==1:
            print("showing customer details")
            qry="select * from customer"
            con1=sql.connect("localhost","root","purbalok1","bank")
            cu1=con1.cursor()
            cu1.execute(qry)
            if cu1.rowcount>0:
                for row in cu1.fetchall():
                    for col in row:
                        print(col,end="\t")
                    print()
            con1.commit()
            con1.close()
        if choice2==2:
            print("showing transaction history")
            qry="select * from transaction"
            con1=sql.connect("localhost","root","purbalok1","bank")
            cu=con1.cursor()
            cu.execute(qry)
            if cu.rowcount>0:
                for row in cu.fetchall():
                    for col in row:
                        print(col,end="\t")
                    print()
            con1.commit()
            con1.close()
        if choice2==3:
            change.credentials(adname,adacc,1)

    else :
        if count!=3:
            print("The credentials do not match with any admin existing records !!!")
            print("TRY AGAIN!!!")
            count=count+1
            adminlogin()
        else:
            print("LOGIN FAILED!!!")
            print("Please Try Restarting The Program")
            sys.exit()
         
count_customer=0
def customerlogin():
    global count_customer
    os.system("cls")
    cus_name=input("Enter the account holder name ")
    cus_acc=input("Enter the account no ")
    cus_pass=input("Enter the password for this account")
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    qry="SELECT * from customer WHERE Name='%s' and Account_No='%s' and Password='%s'"%(cus_name,cus_acc,cus_pass)
    cu.execute(qry)
    con.close()
    if cu.rowcount>0:
        print("1> Change Credentials")
        print("2> Transfer Money")
        print("3> View Balance")
        print("4> Loans")
        print("5> View Details Of transaction")
        inputchoice=int(input("Enter ur choice :"))
        if inputchoice==1:
            change.credentials(cus_name,cus_acc,2)
        if inputchoice==2:
            transfermoney.transfermoney(cus_name,cus_acc)
        if inputchoice==3:
            qry="select Balance from customer where Name='%s' and Account_No='%s'"%(cus_name,cus_acc)
            con=sql.connect("localhost","root","purbalok1","bank")
            cu=con.cursor()
            cu.execute(qry)
            balance=cu.fetchone()
            print("Your account balance is : ",end="")
            print(balance[0])
            con.close()
        if inputchoice==4:
            loan.loans(cus_name,cus_acc)
        if inputchoice==5:
            transaction.transaction1(cus_acc,cus_name)
        cus_choice=input("Do you want to View other field?: Y/N")
        if cus_choice=='Y':
            customerlogin()
    else:
        if count_customer !=3:
            print("The credentials do not match with any  existing records !!!")
            print("TRY AGAIN!!!")
            count_customer=count_customer+1
            customerlogin()
        else:
            print("LOGIN FAILED!!!")
            print("Please Try Restarting the Program!!!")
            sys.exit()
        

def newadminlogin():
    count=0
    print("Please Enter the credentials:")
    ad_name=input("Please Enter Your Name :")
    if ad_name.isalpha():
        pass
    else:
        print("Name Entered Is Not According To Rules: ")
        newadminlogin()
    ad_dob=input("Please Enter the DOB: in format 'yy-mm-dd'")
    year,month,day = ad_dob.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    if(isValidDate) :
        pass
    else:
        print("DOB Entered Is Not According To Rules: ")
        newadminlogin()
    ad_address=input("Please Enter address:")
    ad_phone=int(input("Enter your phone no. must be a 10 digit no."))
    phone=str(ad_phone)
    if len(phone)==10:
        pass
    else:
        print("Phone No. Entered Is Not According To Rules: ")
        newadminlogin()
    del phone
    da_pas=input("Enter the database password:")
    if da_pas=="purbalok1":
        pass
    else:
        print("Password To The Database Doesn't Match ")
        newadminlogin()
    ad_pas=input("Enter Your Password to database: \n Must be atleast of 8 characters and must contain a special character and a number ")
    
    if ad_pas.isalnum():
        if len(ad_pas) > 7:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',ad_pas):
                pass
                count+=1
    if count==1:
        print("Password Entered Is Not According To Rules: ".center())
        newadminlogin()
                
    admin_id="bank"
    while(len(admin_id)!=10):
        n=random.randrange(0,10)
        admin_id=admin_id+str(n)
    qry = ("INSERT INTO admin "
               "(Name, Bank_id, Date_Of_Birth, Address, Phone_no, Password) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
    data= (ad_name, admin_id, ad_dob, ad_address, ad_phone,ad_pas)
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    
    
    count=cu.rowcount
    cu.execute(qry,data)
    if cu.rowcount>count:
        print("data entered successful!!!")
        con.commit()
        con.close()
        inputuser()
    else:
        print("data not entered!!!!!")
        con.close()


def newcustomerlogin():
    count=0
    print("Please Enter the credentials:")
    name=input("Please Enter Your Name :")
    if name.isalpha():
        pass
    else:
        print("Name Entered Is Not According To Rules: ")
        newcustomerlogin()
    cus_dob=input("Please Enter the DOB: in format 'yy-mm-dd'")
    year,month,day = cus_dob.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    if(isValidDate) :
        pass
    else:
        print("DOB Entered Is Not According To Rules: ")
        newcustomerlogin()
    cus_address=input("Please Enter address:")
    cus_phone=int(input("Enter your phone no. must be a 10 digit no."))
    if len(str(cus_phone))==10:
        pass
    else:
        print("Phone No. Entered Is Not According To Rules: ")
        newcustomerlogin()
    cus_adhar=int(input("Enter your addhaar card no."))
    if len(str(cus_adhar))==10:
        pass
    else:
        print("addhaar No. Entered Is Not According To Rules: ")
        newcustomerlogin()
    cus_pan=input("Enter your pan card details:")
    if len(cus_pan)==10:
        if cus_pan.isalnum():
            count1=1
    if count1==0:
        print("Pan No. Entered Is Not According To Rules: ")
        newcustomerlogin()
    cus_balance=int(input("Enter the Opening Amount:"))
    cus_pas=input("Enter Your Password to database: \n Must be atleast of 8 characters and must contain a special character and a number ")
    if cus_pas.isalnum():
        if len(cus_pas) > 7:
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',cus_pas):
                count=1
                pass
    if count==1:
            print("Password Entered Is Not According To Rules: ".center())
            newcustomerlogin()
                
    cus_id=""
    while(len(cus_id)!=10):
        n=random.randrange(0,10)
        cus_id=cus_id+str(n)
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    qry="Select * from customer"
    cu.execute(qry)
    count1=cu.rowcount
    con.commit()
    con.close()
    del qry
    qry = ("INSERT INTO customer "
               "(Name, Account_No, Date_Of_Birth, Address, phone_no, Adhaar_No, PAN_No, Password, balance) "
               "VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)")
    data= (name, cus_id,cus_dob, cus_address, cus_phone,cus_adhar,cus_pan,cus_pas,cus_balance)
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    cu.execute(qry,data)
    count2=cu.rowcount
    con.commit()
    con.close()
    transaction(name, cus_id,cus_balance)
    if count2>count1:
        print("data entered successful!!!")
        inputuser()
        
    else:
        print("data not entered!!!!!")
        inputuser()

print("Hi There !!!")
print("Welcome To MY BANK")

def inputuser():
    print("\n\n\nPlease select the login Type:-")
    print("1 > Admin Login")
    print("2 > Customer Login")
    print("Press Another Number For Creating New Account")
    choice=int(input("Enter Your Choice: "))
    count=1
    try:
        while choice in [1,2]:
            if choice==1:
                adminlogin()
                inputuser()
            if choice==2:
                customerlogin()
                inputuser()
                
        else:
            count=0
            count1=0
            os.system("cls")
            print("New Account :")
            print("Select The Type Of Account: ")
            print("1> admin account")
            print("2> customer account")
            print("Enter your chioce:")
            choice=int(input())
            if choice==1:
                newadminlogin()
                    
            if choice==2:
                newcustomerlogin()
                
    except ValueError:
        print("Please Enter A valid choice!!!")

inputuser()


              
    
