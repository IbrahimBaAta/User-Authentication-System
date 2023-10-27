print("Bismilla Hir Rahman Nir Raheem")
"""
I am not using database for now..
this code is only to check code_flexibility


"""


from csv import DictWriter, DictReader
from random import randint

with open("codeFlexer.csv","r") as db:
    dbReader = list(DictReader(db))
    def NewUsr():
            UserName = input("Name : ")
            if all([row["UserName"]!= UserName  for row in dbReader]):
                while True:
                    try:
                        MobileNo = int(input("Mobile No : "))
                        if len(str(MobileNo)) == 10:
                            if not all([int(row["MobileNo"])!= MobileNo  for row in dbReader]):
                                yesOrno = input(f"The given MobileNo has taken Already\nWant to continue this number {MobileNo} Y/N " )
                                if yesOrno.upper() == "Y":
                                    break
                                elif yesOrno.lower() =="n":
                                    continue
                                else:
                                    print("Use only Y/N")
                            break
                        print("10 digit number needed \nDont Use Contrycode")
                    except ValueError:
                        print("invalid Input, Use numbers")
                while True:
                    Passwrd = input("Password : ")
                    ConfirmPasswrd = input("Confirm Password : ")
                    if Passwrd == ConfirmPasswrd:
                        with open("codeFlexer.csv","a") as db:
                            headers = DictWriter(db,fieldnames=["UserName","MobileNo","Passwrd"])
                            # headers.writeheader()  
                            headers.writerow({
                                "UserName":UserName,
                                "MobileNo":MobileNo,
                                "Passwrd":Passwrd
                            })
                        return "Account created"
                    print("PasswordDoesnotmatch")
            return "Account Exist"


    def Forgot(mobile,p=False):
            for i in dbReader:
                if int(i["MobileNo"]) == mobile:
                    if p != True:
                        print(f"Athentication ID --> {(i['UserName'])} ")
                    elif p == True:
                        while True:
                            otp=randint(10000,99999)
                            print(otp)
                            userotp = input("OTP : ")
                            if otp == int(userotp):
                                Passwrd = input("Password : ")
                                ConfirmPasswrd = input("Confirm Password : ")
                                if Passwrd == ConfirmPasswrd:                                  
                                    i["Passwrd"] = Passwrd
                                    print("ServerDown Try again later")
                                    break # i am not using return because of some specific reasons
                                print("Password Doesnot Matched")
                                   
                    
                    
    def ExUsr():
            all1 = []
            UserName = input("User Name : ")
            for i in dbReader:
                if i["UserName"] == UserName:
                    passwrd = input("Password : ")
                    if i["Passwrd"] == passwrd:
                        return ("Credentials Matched\nNow you have complete access of this account")
                    return "incorrect password"
                elif i["UserName"] != UserName:
                    all1.append(i["UserName"]==UserName)
            if not all(all1):
                print("User Doesnt Exists")
                Y_N = input("If You Want To Join Our Community Y/N : ")
                if Y_N.upper()=="Y":
                    return NewUsr()
                return "Have A SaVE Life.."


def loadPage():
    try:
        choice = int(input("""
    Account Manager..
    -------------------
    1. Want To Join Our Community
    2. Want To Access Your Account
    3. Forgot Your Authentiction ID
    4. Forgot Your Password
    5. Exit..
    $. """))
        if choice == 1:
            print(NewUsr())
        elif choice == 2:
            print(ExUsr() )  
        elif choice == 3:
            no = int(input("MobileNO: "))
            print(Forgot(no))
            
        elif choice == 4:
            no = int(input("MobileNO: "))
            print(Forgot(no,p=True))
        elif choice == 5:
            return "\t Have A Good Life.."
        else:
            print("WrongInput")
    except ValueError as error: print(error,"invalid Input use int()")
    





if __name__ == "__main__":
    loadPage()
    