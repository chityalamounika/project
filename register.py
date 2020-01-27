import pymysql
class MobileException(Exception):
      pass
class EmailException(Exception):
      pass
      
class userregister:
      def __init__(self):
            self.con=None
            self.cur=None
            self.fname=None
            self.fn=None
            self.ln=None
            self.mobile=None
            self.email=None
            self.dob=None
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='app',port=3308)
            self.cur=self.con.cursor()
      def createuser(self):
            self.fn=input("enter first name:")
            self.ln=input("enter last name:")
            while True:
                  self.mobile=input('enter mobile number')
                  try:
                        self.cur.execute("SELECT MobileNo FROM Register")
                        result=self.cur.fetchall()
                        for x in result:
                              for y in x:
                                    if y==self.mobile:
                                          raise MobileException
                        break
                  except MobileException:
                        print('mobile number is already exists\n press cnt^n to exit')
            self.dob=input("enter dob:")
            while True:
                  self.email=input('enter the email')
                  try:
                        self.cur.execute("SELECT Email FROM Register")
                        result=self.cur.fetchall()
                        for x in result:
                              for y in x:
                                    if y==self.email:
                                          raise EmailException
                        break
                  except EmailException:
                        print('this email is already exists\n press cnt^n to exit')
            self.fname=str(self.fn+' '+self.ln)
            sql="insert into register(Firstname,Lastname,Fullname,Mobileno,email,DOB)VALUES(%s,%s,%s,%s,%s,%s)"
            values=[self.fn,self.ln,self.fname,self.mobile,self.email,self.dob]
            self.cur.execute(sql,values)
            self.con.commit()
            self.con.close()
            print("user registered")
            
                  
