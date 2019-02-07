import os
import pymysql as sql
def loans(cus_name,cus_acc):
    os.system("cls")
    qry="select * from loans where Name='%s' and Account_No='%s'"%(cus_name,cus_acc)
    print("Press 1 To Take Loan")
    print("Press 2 To Repay Loan")
    n=int(input("Enter your choice: "))
    if n==1:
        print("Enter the Loan Details: ")
        print("The rate-of-interest  are given below:)")
        print("1: Rs 10000-50000      rate-of-interest=2% ")
        print("2: Rs 50000-100000      rate-of-interest=5% ")
        print("3: Rs 100000-200000      rate-of-interest=8% ")
        print("4: Rs 200000-2000000      rate-of-interest=10% ")
        print("5: Rs 2000000    rate-of-interest=12% ")
        loan_amount=int(input("Enter the loan amount"))
        purpose=input("Enter the purpose of loan:")
        duration=int(input("Enter the duration of repayment:"))
        if loan_amount>=10000 and loan_amount<50000:
            loan_amount1=loan_amount+loan_amount*.02
            data=(cus_name,cus_acc,loan_amount,purpose,duration,2,loan_amount1,0)
        if loan_amount>=50000 and loan_amount<100000:
            loan_amount1=loan_amount+loan_amount*.05
            data=(cus_name,cus_acc,loan_amount,purpose,duration,5,loan_amount1,0)
        if loan_amount>100000 and loan_amount<200000:
            loan_amount1=loan_amount+loan_amount*.08
            data=(cus_name,cus_acc,loan_amount,purpose,duration,8,loan_amount1,0)
        if loan_amount>200000 and loan_amount<2000000:
            loan_amount1=loan_amount+loan_amount*.10
            data=(cus_name,cus_acc,loan_amount,purpose,duration,10,loan_amount1,0)
        if loan_amount>2000000:
            loan_amount1=loan_amount+loan_amount*.12
            data=(cus_name,cus_acc,loan_amount,purpose,duration,12,loan_amount1,0)

        con=sql.connect("localhost","root","purbalok1","bank")
        cu=con.cursor()
        qry = ("INSERT INTO loan (Name, Account_No, Loan_Taken, Purpose, Duration, Rate_Of_Interest, Money_To_Repay,Money_Paid) "
               "VALUES (%s, %s, %s, %s, %s, %s,%s,%s)")
    
        cu.execute(qry,data)
        con.commit()
        con.close()

    if n==2:
        row=0
        amount1=int(input("Enter the amount you want to repay:"))
        qry="select Money_To_Repay from loan where Name='%s' and Account_No='%s'"%(cus_name,cus_acc)
        con=sql.connect("localhost","root","purbalok1","bank")
        cu=con.cursor()
        cu.execute(qry)
        row=cu.rowcount
        balance=cu.fetchone()
        con.commit()
        con.close()
        del cu
        if row>0:
            if amount1> int(balance[0]):
                print("1:Please Enter a valid amount.......Please retry....")
                loans(cus_name,cus_acc)
            else:
                qry1="select Money_Paid from loan where Name='%s' and Account_No='%s' "%(cus_name,cus_acc)
                con1=sql.connect("localhost","root","purbalok1","bank")
                cu=con1.cursor()
                cu.execute(qry1)
                money=cu.fetchone()
                con1.commit()
                con1.close()
                qry="update loan set Money_To_Repay='%s',Money_Paid='%s' where Name='%s' and Account_No='%s'"%(str(int(balance[0])-amount1),str(int(money[0])+amount1),cus_name,cus_acc)
                con=sql.connect("localhost","root","purbalok1","bank")
                cu=con.cursor()
                cu.execute(qry)
                con.commit()
                con.close()
        else:
            print("Sorry No record found with given details:")
            os.system('cls')
