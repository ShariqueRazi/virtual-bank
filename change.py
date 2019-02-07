import pymysql as sql
import os
import datetime
import re
count=0
def clear(name,acc,no):
    global count
    print("Unable to update the details...")
    print("Rolling back all previous changes....")
    if count!=3:
        count+=1
        credentials(name,acc,no)
    else:
        inputuser()
    
def credentials(name,acc,no):
    os.system("cls")
    global count
    if no==2:
        print("What do you want to change?")
        print("1> Name")
        print("2> Date Of Birth")
        print("3> Address")
        print("4> Phone No")
        print("5> Adhaar No")
        print("6> PAN")
        print("7> Password")
        choice=int(input("Enter Your choice:"))
        if choice==1:
            name1=input("Enter the new Account holder name :")
            if name1.isalpha():
                con5=sql.connect("localhost","root","purbalok1","bank")
                cursor=con5.cursor()
                qry="update customer set Name='%s' where Account_No='%s'" %(name1,acc)
                cursor.execute(qry)
                count1=cursor.rowcount
                con5.commit()
                con5.close()
                if count1>0:
                    print("Successfully updated the details...")
                else:
                    print("Unable to update the details...")
                    print("Rolling back all previous changes....")
            else:
                print("Name Entered Is Not According To Rules: ")
                count=count+1
                if count!=3:
                    credentials(name,acc,no)
                else:
                    os.system('cls')
        if choice==2:
            dob=input("Enter the new Account holder Date Of Birth in format 'yy-mm-dd' :")
            year,month,day =dob.split('-')
            isValidDate = True
            try :
                datetime.datetime(int(year),int(month),int(day))
            except ValueError :
                isValidDate = False
            if(isValidDate) :
                qry="update customer set Date_Of_Birth='%s' where Name='%s' and Account_No='%s'"%(dob,name,acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                count=cu.rowcount
                con.commit()
                con.close()
                if count>0:
                    print("Successfully updated the details...")
                else:
                    print("Unable to update the details...")
                    print("Rolling back all previous changes....")
            else:
                print("DOB Entered Is Not According To Rules: ")
                if count!=3:
                    credentials(name,acc,no)
                    count=count+1
                else:
                    inputuser()
        if choice==3:
            address1=input("Enter the new Account holder Address :")
            qry="update customer set Address='%s' where Name='%s' and Account_No='%s'"%(address1,name,acc)
            con=sql.connect("localhost","root","purbalok1","bank")
            cu=con.cursor()
            cu.execute(qry)
            count=cu.rowcount
            con.commit()
            con.close()
            count=count+1
            if count>0:
                print("Successfully updated the details...")
            else:
                clear(name,acc,no)
        if choice==4:
            phone=input("Enter the New Phone No.")
            if len(phone)==10:
                qry="update customer set phone_no='%s' where Name='%s' and Account_No='%s'" %(phone,name,acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                count=cu.rowcount
                con.commit()
                con.close()
                count=count+1
                if count>0:
                    print("Successfully updated the details...")
            else:
                clear(name,acc,no)
        if choice==5:
            adhr=input("Enter The New Adhaar No. :")
            if len(adhr)==10:
                if adhr.isdigit():
                    qry="update customer set adhaar_no='%s' where Name='%s' and Account_No='%s'" %(adhr,name,acc)
                    con=sql.connect("localhost","root","purbalok1","bank")
                    cu=con.cursor()
                    cu.execute(qry)
                    count=cu.rowcount
                    con.commit()
                    con.close()
                    count=count+1
                    if count>0:
                        print("Successfully updated the details...")
                    else:
                        clear(name,acc,no)
                else:
                    clear(name,acc,no)
            else:
                clear(name,acc,no)
        if choice==6:
            pan=input("Enter the new PAN no ")
            if len(pan)==10:
                if pan.isalnum():
                    qry="update customer set PAN_No='%s' where Name='%s' and Account_No='%s'" %(pan,name,acc)
                    con=sql.connect("localhost","root","purbalok1","bank")
                    cu=con.cursor()
                    cu.execute(qry)
                    count=cu.rowcount
                    con.commit()
                    con.close()
                    count=count+1
                    if count>0:
                        print("Successfully updated the details...")
                    else:
                        clear(name,acc,no)
                else:
                    clear(name,acc,no)
            else:
                clear(name,acc,no)
        if choice==7:
            cus_pas=input('Enter the new Password: \nMust be atleast of 8 characters and must contain a special character and a number \n')
            if len(cus_pas) > 7:
                if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',cus_pas):
                    qry="update customer set Password='%s' where Name='%s' and Account_No='%s'" %(cus_pas,name,acc)
                    con=sql.connect("localhost","root","purbalok1","bank")
                    cu=con.cursor()
                    cu.execute(qry)
                    count=cu.rowcount
                    con.commit()
                    con.close()
                    count=count+1
                    if count>0:
                        print("Successfully Updated the details:")
                else:
                    clear(name,acc,no)
            else:
                clear(name,acc,no)
    if no==1:
        print("What do you want to change:")
        print("1> Name")
        print("2> Date Of Birth")
        print("3> Address")
        print("4> Phone no")
        print("5> Password")
        choice=int(input("Enter Your choice:"))
        if choice==1:
            name1=input("Enter the new Account holder name :")
            if name.isalpha():
                qry="update admin set Name='%s' where Name='%s' and Bank_id='%s'" %(name1,name,acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                count1=cu.rowcount
                con.commit()
                con.close()
                if count1>0:
                    print("Successfully updated the details...")
                else:
                    print("Unable to update the details...")
                    print("Rolling back all previous changes....")
            else:
                print("Name Entered Is Not According To Rules: ")
                count=count+1
                if count!=3:
                    credentials(name,acc,no)
                else:
                    sys.exit()
        if choice==2:
            dob=input("Enter the new Account holder Date Of Birth in format 'yy-mm-dd' :")
            year,month,day = dob.split('-')
            isValidDate = True
            try :
                datetime.datetime(int(year),int(month),int(day))
            except ValueError :
                isValidDate = False
            if(isValidDate) :
                qry="update admin set Date_Of_Birth='%s' where Name='%s' and Bank_id='%s'"%(dob,name,acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                count=cu.rowcount
                con.commit()
                con.close()
                if count>0:
                    print("Successfully updated the details...")
                else:
                    print("Unable to update the details...")
                    print("Rolling back all previous changes....")
            else:
                print("DOB Entered Is Not According To Rules: ")
                if count!=3:
                    credentials(name,acc,no)
                    count=count+1
                else:
                    inputuser()
        if choice==3:
            address1=input("Enter the new Account holder Address :")
            qry="update admin set Address='%s' where Name='%s' and Bank_id='%s'"%(address1,name,acc)
            con=sql.connect("localhost","root","purbalok1","bank")
            cu=con.cursor()
            cu.execute(qry)
            count=cu.rowcount
            con.commit()
            con.close()
            count=count+1
            if count>0:
                print("Successfully updated the details...")
            else:
                clear(name,acc,no)
        if choice==4:
            phone=input("Enter the New Phone No.")
            if len(phone)==10:
                qry="update admin set phone_no='%s' where Name='%s' and Bank_id='%s'" %(phone,name,acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                count=cu.rowcount
                con.commit()
                con.close()
                count=count+1
                if count>0:
                    print("Successfully updated the details...")
            else:
                clear(name,acc,no)
        if choice==5:
            pas=input('Enter the new Password: \nMust be atleast of 8 characters and must contain a special character and a number ')
            if len(pas) > 7:
                if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}',pas):
                    qry="update admin set Password='%s' where Name='%s' and Bank_id='%s'" %(pas,name,acc)
                    con=sql.connect("localhost","root","purbalok1","bank")
                    cu=con.cursor()
                    cu.execute(qry)
                    count=cu.rowcount
                    con.commit()
                    con.close()
                    count=count+1
                    if count>0:
                        print('Successfully updated the details...')
                else:
                    clear(name,acc,no)
            else:
                clear(name,acc,no)
            
        
            
        
                    
            
            
            
        
