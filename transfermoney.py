import pymysql as sql
import datetime as dt
import os
import sys
count=1
def transfermoney(cus_name,cus_acc):
    global count
    tran_name=input("Enter the customer name whom you want to transfer the money: ")
    tran_acc=input("Enter the Account no. of the customer: ")
    qry="select balance from customer where Name='%s' and Account_No='%s'"%(tran_name,tran_acc)
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    cu.execute(qry)
    row=cu.rowcount
    con.commit()
    del qry
    con.close()
    qry ="select balance from customer where Name='%s' and Account_No='%s'" %(cus_name,cus_acc)
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    cu.execute(qry)
    balance=cu.fetchone()
    con.commit()
    con.close()
    del qry
    if row>0:
        del row
        if int(balance[0])>500:
            tran_count=0
            qry="select balance from customer where Name='%s' and Account_No='%s'"%(tran_name,tran_acc)
            con=sql.connect("localhost","root","purbalok1","bank")
            cu=con.cursor()
            cu.execute(qry)
            balance1=cu.fetchone()
            row=cu.rowcount
            tran_count=cu.fetchone()
            con.commit()
            con.close()
            tran_amount=int(input("Enter the amount to transfer: "))
            print("Your available account balance is : %d" %(int(balance[0])))
            if tran_amount>int(balance[0]) and count!=3:
                print("Please Enter A Correct Amount:")
                print("Rolling back all previous settings...")
                transfermoney(cus_name,cus_acc)
                count=count+1
        
            elif tran_amount>int(balance[0]) and count==3:
                print("Transaction Failed!!!")
                inputuser()

            else:
                con1=sql.connect("localhost","root","purbalok1","bank")
                cu=con1.cursor()
                qry="update customer set balance='%s' where Name='%s' and Account_No='%s'"%(str(int(balance[0])-int(tran_amount)),cus_name,cus_acc)
                cu.execute(qry)
                con1.commit()
                con1.close()
                del cu
                con1=sql.connect("localhost","root","purbalok1","bank")
                cu=con1.cursor()
                qry="update customer set balance='%s' where Name='%s' and Account_No='%s'"%(str(int(balance1[0])+int(tran_amount)),tran_name,tran_acc)
                cu.execute(qry)
                con1.commit()
                con1.close()
                del cu
                con1=sql.connect("localhost","root","purbalok1","bank")
                cu=con1.cursor()
                qry="update transaction set balance='%s',Money_Transfered_To='%s',Transfer_Date='%s',Transfered_Amount='%s' where Name='%s' and Account_No='%s' "%(str(int(balance[0])-int(tran_amount)),tran_acc,str(dt.date.today()),tran_amount,cus_name,cus_acc)
                cu.execute(qry)
                con1.commit()
                con1.close()
                del cu
                con1=sql.connect("localhost","root","purbalok1","bank")
                cu=con1.cursor()
                qry="update transaction set balance='%s',Transfer_Date='%s',Transfered_Amount='%s' where Name='%s' and Account_No='%s' "%(str(int(balance1[0])+int(tran_amount)),str(dt.date.today()),tran_amount,tran_name,tran_acc)
                cu.execute(qry)
                con1.commit()
                con1.close()
                print("Success!!!")
                del cu
        else:
            print("Your Account balance is Lower than required!!!")
            sys.exit()
    else:
        print("No record found with given details....")
        print("Rolling back all previous changes...")
        sys.exit()
            
        
    
