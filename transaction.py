def transaction1(accno,name):
    con=sql.connect("localhost","root","purbalok1","bank")
    cu=con.cursor()
    qry="select * from transaction where Account_no='%s' and Name='%s'"%(accno,name)
    cu.execute(qry)
    con.commit()
    cu.close()
    
    
