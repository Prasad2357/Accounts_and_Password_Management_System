1

print("\n\nWELCOME TO PASSWORDS AND ACCOUNTS MANAGEMENT SYSTEM\n")




from datetime import date
import random
import string
import base64 
import os


def user_id():
    a=1
    b=0
    c=0
    print(" 1)Create your own user id" + "\n [user id should be alphanumeric only]")
    while a <= 10:
        global userid
        userid= input("\n Create your user id: ")
        if os.path.exists(userid + "info.txt")==False:
          if userid.isalnum():
             if len(userid)>=6:
                 for p in userid:
                     if p.isdigit():
                         b+=1
                     if p.isalpha():
                         c+=1
                 if c>=1 and b>=1:
                   break
                 elif c==0 and b>=1:
                   print(" user id should contain at least one alphabet!!!")
                   continue
                 elif b==0 and c>=1:
                   print(" user id should contain at least one digit!!!")
             else:
               print(" user id should contain at least 6 characters!!!")
               continue
          else:
             print(" user id should be alphanumeric only!!!")
             continue
        else:
            print(" userid already exists, try another!!!")




def password1():
    n=0
    while n<10:
        password1 = input("\n Create your Password: ")
        if len(password1)>=6:
            password2 = input(" Confirm your password: ")
            if password1 == password2:
                passwordED= password2.encode("ascii")
                password3 = base64.b64encode(passwordED)
                global password
                password= password3.decode("ascii")
                break
            else:
                print(" Passwords do not match, please try again!!!")
        else:
            print("Password should contain at least 6 characters!!!")
            continue




def captcha():
    n=0
    while n<=10:
        X=random.randint(0,9)
        Y=random.randint(0,9)
        X1=random.choice(string.ascii_letters)
        Y1=random.choice(string.ascii_letters)
        C=str(X)+X1+str(Y)+Y1
        print("\n CAPTCHA=  ",C)
        cap=input(" Enter above CAPTCHA: ")
        if cap==C:
            break
        else:
            print(" Invalid captcha, please try again!!!")
            continue




def username():
    print("\n ENTER YOUR NAME")
    g = 0

    while g <= 10:
        f = input("\n Enter First Name: ")
        if f.isalpha():
          break
        else:
          print(" Invalid Name, please try again!!!")
          continue

    while g <= 10:
        m = input("\n Enter Middle Name: ")
        if m.isalpha():
         break
        else:
         print(" Invalid Name, please try again!!!")
         continue

    while g <= 10:
        l = input("\n Enter Last Name: ")
        if l.isalpha():
         break
        else:
            print(" Invalid Name, please try again!!!")
            continue

    F = f.capitalize()
    M = m.capitalize()
    L = l.capitalize()
    global Username
    Username = F + " " + M + " " + L




def Date_of_Birth():
    today = date.today()
    today1 = str(today)
    d = today1[-2:]
    m = today1[5:7]
    y = today1[0:4]
    d1 = int(d)
    m1 = int(m)
    y1 = int(y)
    g = 0
    print("\n ENTER YOUR DATE OF BIRTH")
    while g <= 0:
        dd = input("\n date: ")
        if dd.isdigit():
            dd1 = int(dd)
            if dd1 >= 1 and dd1 <= 31:
                mm = input("\n month: ")
                if mm.isdigit():
                    mm1 = int(mm)
                    if mm1 >= 1 and mm1 <= 12:
                        if (dd1 >= 1 and dd1 <= 31) and (mm1 == 1 or mm1 == 3 or mm1 == 5 or mm1 == 7 or mm1 == 8 or mm1 == 10 or mm1 == 12):
                            yyyy = input("\n year: ")
                            if yyyy.isdigit():
                                yyyy1 = int(yyyy)
                                if (yyyy1 >= 1900 and yyyy1 < y1):
                                    break
                                elif yyyy1==y1 and m==1 and dd1<d1:
                                    break
                                elif yyyy1==y1 and mm1<m1:
                                    break
                                elif yyyy1==y1 and mm1==m1 and dd1<=d1:
                                    break
                                else:
                                    print(" Invalid date, please try again!!!")
                                    continue
                            else:
                                print(" Invalid date, please try again!!!")
                                continue
                        elif (dd1 >= 1 and dd1 <= 30) and (mm1 == 4 or mm1 == 6 or mm1 == 9 or mm1 == 11):
                            yyyy = input("\n year: ")
                            if yyyy.isdigit():
                                yyyy1 = int(yyyy)
                                if (yyyy1 >= 1900 and yyyy1 < y1):
                                    break
                                elif yyyy1 == y1 and mm1 < m1:
                                    break
                                elif yyyy1 == y1 and mm1 == m1 and dd1 <= d1:
                                    break
                                else:
                                    print(" Invalid date,please try again!!")
                                    continue
                            else:
                                print(" Invalid date, please try again!!!")
                                continue

                        elif mm1 == 2 and (dd1 >= 1 and dd1 <= 29):
                            yyyy = input("\n year: ")
                            if yyyy.isdigit():
                                yyyy1 = int(yyyy)
                                if (yyyy1 >= 1900 and yyyy1 < y1):
                                    if yyyy1 % 400 != 0 and yyyy1 % 100 == 0 and dd1 >= 1 and dd1 <= 28:
                                        break
                                    elif yyyy1 % 4 != 0 and yyyy1 % 100 != 0 and dd1 >= 1 and dd1 <= 28:
                                        break


                                    elif yyyy1 % 4 == 0 and yyyy1 % 400 == 0 and dd1>=1 and dd1<=29:
                                            break

                                    elif  yyyy1 % 4 == 0 and yyyy1 % 100 != 0 and dd1<=29 and dd1>=1:
                                        break
                                    else:
                                        print(" Invalid date,please try again!!")
                                        continue
                                elif yyyy1 == y1 and mm1 == m1 and dd1 <= d1:
                                    break
                                elif yyyy1==y1 and mm1<m1:
                                    break
                                else:
                                    print(" Invalid date,please try again!!")
                                    continue
                            else:
                                print(" Invalid date, please try again!!!")
                                continue
                        else:
                            print(" Invalid date, please try again!!!")
                            continue
                    else:
                      print(" Invalid date, please try again!!!")
                      continue
                else:
                    print(" Invalid date, please try again!!!")
                    continue
            else:
              print(" Invalid date, please try again!!!")
              continue
        else:
          print(" Invalid date, please try again!!!")
          continue
    global Date
    Date=dd+"/"+mm+"/"+yyyy




def MobileNumber():
    global mobile_no
    j = 0
    while j <= 10:
        global mobile_no
        mobile_no = input("\n Enter your mobile number: ")
        for i in mobile_no:
            if len(mobile_no) == 10 and 48 <= ord(i) <= 57 and (
                    mobile_no[0] == "9" or mobile_no[0] == "8" or mobile_no[0] == "7" or mobile_no[0] == "6"):
                pass
            else:
                print(" Invalid mobile number, please try again!!!")
                break
        else:
            break




def Email():
    global email_id
    k = 1
    while k <= 10:
        email_address = str(input("\n Enter your email id: "))
        email_id = email_address.lower()
        X = "@" in email_id
        Y = ("gmail.com" in email_id) or (".ac.in" in email_id) or ("yahoo.com" in email_id) or (
                "outlook.com" in email_id)
        if X and Y == True:
            break
        else:
            print(" Invalid email address, please try again!!!")
        n = len(email_address)
        if ("gmail.com" in email_id) or ("yahoo.com" in email_id):
            email_id = email_address.replace(email_address[n - 9:n], "gmail.com")
        elif "outlook.com" in email_id:
            email_id = email_address.replace(email_address[n - 11:n], "outlook.com")
        elif ".ac.in" in email_id:
            email_id = email_address.replace(email_address[n - 6:n], ".ac.in")




def signup():

    # User id
    user_id()

    #password
    password1()

    #captcha
    captcha()

    # Username
    username()

    # Date of Birth
    Date_of_Birth()

    # MOBILE NO
    MobileNumber()

    # Email
    Email()

    with open(userid + 'info.txt', 'a') as f:
        f.write(" Welcome to Passwords and Accounts Management System\n")

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n user id               : " + userid)

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n Password              : " + password)

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n Username              : " + Username)

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n Date of Birth         : " + Date)

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n Mobile Number         : " + "+91" + mobile_no)

    with open(userid + 'info.txt', 'a') as f:
        f.write("\n Email Address         : " + email_id)




def login():
    g = 0
    while g <= 10:
        user_id = input("\n Enter your user id: ")
        password1 = input("\n Enter your password: ")
        password2=password1.encode("ascii")
        password3 = base64.b64encode(password2)
        password = password3.decode("ascii")
        captcha()
        if os.path.exists(user_id + "info.txt") and os.path.getsize(user_id+"info.txt")!=0:
            file = open(user_id + "info.txt")
            info = file.readlines()
            if (info[2] == " user id               : " + user_id + "\n") and (
                    info[3] == " Password              : " + password + "\n"):
                with open(user_id+'info.txt', 'r') as f:
                    for lines in f.readlines():
                        print(lines.rstrip())
                break
            else:
                print(" invalid credentials, please try again!!!")
                continue
        else:
            print(" invalid credentials, please try again!!!")
            continue




def add_account():
    g=0
    while g <= 10:
        user_id = input("\n Enter your user id: ")
        password1 = input("\n Enter your password: ")
        password2 = password1.encode("ascii")
        password3 = base64.b64encode(password2)
        password = password3.decode("ascii")
        captcha()
        if os.path.exists(user_id + "info.txt") and os.path.getsize(user_id+"info.txt")!=0:
            file = open(user_id + "info.txt")
            info = file.readlines()
            if (info[2] == " user id               : " + user_id + "\n") and (
                    info[3] == " Password              : " + password + "\n"):
              global account_name
              account_name = input("\n Enter account name: ")
              account_id = input("\n Enter account id: ")
              for i in range(3):
                  password1 = input("\n Enter your Password of "+account_name+": ")
                  password2 = input(" Confirm Password: ")
                  if password1 == password2:
                      passwordED = password2.encode("ascii")
                      password3 = base64.b64encode(passwordED)
                      password = password3.decode("ascii")
                      break
                  else:
                     print(" Password does not match!!!")
                     continue
              else:
                  print(" Your session has been expired!!!")
                  break

              Important_information = input(" Other information: ")

              with open(user_id + 'info.txt', 'a') as f:
                  f.write("\n\n Account Name          : "+account_name)

              with open(user_id + 'info.txt', 'a') as f:
                  f.write("\n Password              : "+password)

              with open(user_id + 'info.txt', 'a') as f:
                  f.write("\n Account id            : " + account_id)

              with open(user_id + 'info.txt', 'a') as f:
                  f.write("\n Other information     : " + Important_information)
                  break

            else:
                print(" invalid credentials, please try again!!!")
                continue
        else:
            print(" invalid credentials, please try again!!!")
            continue




def knowpassword():
    login()

    Unknown_password1=input("\n Enter the encoded password shown above: ")
    Unknown_password2 = Unknown_password1.encode("ascii")
    Unknown_password3 = base64.b64decode(Unknown_password2)
    known_password=Unknown_password3.decode("ascii")

    print("\n Your password is "+ known_password)




g=0
h=0
import os
def delete():
 while g<=10:
     user_id = input("\n Enter your user id: ")
     password1 = input("\n Enter your password: ")
     password2 = password1.encode("ascii")
     password3 = base64.b64encode(password2)
     password = password3.decode("ascii")
     captcha()
     if os.path.exists(user_id+"info.txt") and os.path.getsize(user_id+"info.txt")!=0:
       file=open(user_id+"info.txt")
       info1=file.readlines()
       if (info1[2] == " user id               : " + user_id + "\n") and (info1[3] == " Password              : " + password + "\n"):
           file=open(user_id+"info.txt","r+")
           file.truncate(0)
           file.close()
           break
       else:
           print(" Invalid credentials, please try again!!!")
           continue
     else:
         print(" Invalid credentials, please try again!!!")
         continue




a=0
while a<=10:
    n = input("\n Enter... \n 1 to create account in passwords and accounts management system \n 2 to log in your account\n 3 to add an account\n 4 to know your passwords  \n 5 to delete account \n 6 for exit \n")

    if n == "1":
        signup()
        print("\n Your account has been successfully created!!!")
        continue

    elif n == "2":
         login()
         print("\n You have been successfully logged in!!!")
         continue

    elif n=="3":
        add_account()
        print("\n"+" Your "+account_name+" account has been successfully added!!!")
        continue

    elif n=="4":
        knowpassword()
        continue

    elif n == "5":
         delete()
         print(" Your account has been successfully deleted!!!")
         continue

    elif n=="6":
        break

    else:
        print("\n Invalid Mode, please try again!!!")
        continue

