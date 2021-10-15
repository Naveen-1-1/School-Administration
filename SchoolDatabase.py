from pickle import *
from datetime import date,timedelta
import random
import os

class School(object):
    
    def __init__(self):
        
        self.name=None
        self.adminno=0
        self.gradepassed=0
        self.grade=0
        self.d_o_b=None
        self.contact1=0
        self.contact2=0
        self.father=None
        self.mother=None
        self.emirate=None
        self.area=None
        self.buspoint=None
        self.busno=0

    def allot(self):
        
        print "Following are the buses allotted to specific areas."
        print "If your area doesn't have a bus allotted to it, you may use the bus of the nearest allotted area or register as OT(Own Transport)."
        dict={"Bur Dubai":1, "Deira":2,"Qusais":3,"Karama":4, "Al Khan":11, "Al Nahda":12,"Abu Shagarah":13,"Rolla":14, "Al Bustan":21,"Manama":22,"Garden City":23,"Al Dhaid":24}
        print "Area\t\tBus Allotted"
        for i in dict:
            print ("%-15s%5.2s"%(i,dict[i]))
        print "Please enter the exact area as shown in the above table (Case Sensitive)."    
        self.buspoint=raw_input("enter pickup/dropoff bus point")
        if self.buspoint in dict:
            self.busno=dict.get(self.buspoint)
        elif self.buspoint.upper()=="OT":
            self.busno="OT"
            print "You have been registered as OT(Own Transport)."
        else:
            print "Sorry, there is no bus allotted to your area."
        if self.gradepass.upper()=='KG2':
            self.grade=1
        else:
            self.grade=int(self.gradepass)+1

    def inputval(self):

        print "Admission Number:", random.randint(1000,9000)
        print "Kindly fill out this interactive admission form to register your child's name with the school"
        self.adminno=input("Enter the admission number provided to you:")
        self.name=raw_input("Name of student:")
        self.d_o_b=raw_input("Date of Birth:")
        self.gradepass=raw_input("Grade Passed:")
        self.father=raw_input("Father's name:")
        self.mother=raw_input("Mother's name:")
        self.contact1=raw_input("Contact Number:")
        self.contact2=raw_input("Secondary Contact Number:")
        self.emirate=raw_input("Residence Emirate:")
        self.area=raw_input("Residence Area (e.g. Bur Dubai, Deira, Abu Shagarah):")
        self.allot()

    def outputval(self):

        print "\nRecorded Details".center(48,"*")
        print "Admission Number:",self.adminno
        print "Name of student:", self.name
        print "Date of Birth:", self.d_o_b
        print "Grade:", self.grade
        print "Father's name:", self.father
        print "Mother's name:", self.mother
        print "Contact Number:", self.contact1
        print "Secondary Contact Number:", self.contact2
        print "Residence Emirate:", self.emirate
        print "Residence Area:", self.area
        print "Bus Number:", self.busno


def OnlineAdministrationRecords():
    
    S=School()
    
    def storedata():

        f=open("StudentDets.dat",'ab')
        S.inputval()
        dump(S,f)
        f.close()

    def readdata():

        f=open("StudentDets.dat", 'rb')
        admin_no=input("enter admission number")
        flag=0
        try:
            while True:
                S=load(f)
                if admin_no==S.adminno:
                    S.outputval()
                    flag=1
        except EOFError:
            pass
        f.close()
        if flag==0:
            print "Sorry this admission number is invalid and/or doesn't exist."
                
    def allschooldata():

        f=open("StudentDets.dat",'rb')
        pas=raw_input("Enter school staff password:")
        if pas=="ooehs123":
            grade=input("enter grade for which recorded details to be viewed:")
            try:
                while True:
                    S=load(f)
                    if grade==S.grade:
                        S.outputval()
                           
            except EOFError:
                pass
        else:
            print "Sorry, this information is confidential and only school staff can view it."
        f.close()

    while True:
        print """\n\nWelcome to the Online Administration Records.
In this section you can:
(1)Apply for new admission
(2)View admission details
(3)View grade-wise admission details(For staff user)
(4)Exit Administration Section"""
        
        choice=input("Enter your choice (1/2/3/4):")
        if choice==1:
                storedata()
        elif choice==2:
                readdata()
        elif choice==3:
                allschooldata()
        elif choice==4:
                print "We hope the online administration records have been useful to you."
                print "Goodbye."
                break
        else:
                print "Wrong choice"
             

################################################################################# END OF SECTION 1
    
class Fees:
    
    def __init__(self):
        
        self.adminnof =0
        self.namef =0
        self.gradef =0
        self.months =0
        self.amount =0
        self.amount_tot =0
        self.medical =0

    def inputfee(self):

        self.adminnof=input("Admission Number:")
        self.namef=raw_input("Name:")
        self.gradef=raw_input("Grade:")
        self.months=input("Number of months to be paid:")
        self.medical=250.0                      
        self.amount_tot=(self.amount*self.months)+self.medical

    def outputfee(self):

        print "Tuition Fees:", self.amount*self.months
        print "Medical Fees:", self.medical
        print "Total Amount:", self.amount_tot
        print '\n\n'
        card=raw_input("Credit/Debit Card Number:")
        password=raw_input("Password:")
        print "Transacting......"
        print "Amount has been retreived"

A=Fees()

def OnlineFeeRecords():
    
    def payfees():

        f=open("Fees.dat",'ab')
        A.inputfee()
        dump(A,f)
        f.close()

    def viewfeerecord():
        
        f=open("Fees.dat", 'rb')
        f1=open("StudentDets.dat", 'rb')
        admin_no=input("Please enter your admission number to view your fee details:")
        flag=0
        try:
            while True:
                A=load(f)
                S=load(f1)
                if admin_no==S.adminno:
                    MonthlyFees={'1':1440, '2':1440, '3':1600, '4':1600,'5':1680,'6':1680,'7':1680,'8':1680,'9':1760,'10':1760,'11':1800, '12':1800}
                    A.amount=float(MonthlyFees.get(str(S.grade)))
                    print "Receipt".center(48,"*")
                    print "Admission Number:", S.adminno
                    print "Name:", S.name
                    print "Grade:", S.grade
                    A.outputfee()                
                    flag=1
        except EOFError:
            pass
        if flag==0:
            print "Sorry, the admission number entered is invalid and/or does not exist."
        f.close()
        
        
    def allfeedata():

        f=open("Fees.dat",'rb')
        f1=open("StudentDets.dat", 'rb')
        pas=raw_input("Enter school staff password:")
        if pas=="ooehs123":
            grade=input("enter grade for which fee records to be viewed:")
            try:
                while True:
                    A=load(f)
                    S=load(f1)
                    if grade==S.grade:
                        print "Admission Number:", S.adminno
                        print "Tuition Fees:", A.amount*A.months
                        print "Medical Fees:", A.medical
                        print "Total Amount:", A.amount_tot
                        print '\n\n'
            except EOFError:
                pass
        else:
            print "Sorry, this information is confidential and only school staff can view it."
        f.close()

    while True:
            print """\n\nWelcome to the Online Fee Records.
In this section you can:
(1)Pay fees
(2)View your fee record
(3)View grade-wise fee details(For staff user)
(4)Exit Fee Section"""
            
            choice=input("Enter your choice (1/2/3/4):")
            if choice==1:
                    payfees()
                    print '\n'
                    viewfeerecord()
            elif choice==2:
                    viewfeerecord()
            elif choice==3:
                    allfeedata()
            elif choice==4:
                    print "We hope the online fee records have been useful to you."
                    print "Goodbye."
                    break
            else:
                    print "Wrong choice"

################################################################################# END OF SECTION 2
    
class Science:

        def __init__(self):

            self.adminno=input("enter administration number:")
            self.name=raw_input("enter name:")
            self.grade=input("enter grade:")
            self.English_marks=input("Enter English marks  : ")
            self.Physics_marks=input("Enter Physics marks  : ")
            self.Chemistry_marks=input("Enter Chemistry marks: ")
            self.Option1=raw_input("Enter Optional Subject 1: ").capitalize()
            self.Option1_marks=input("Enter Optional Subject 1 marks: ")
            self.Option2=raw_input("Enter Optional Subject 2: ").capitalize()
            self.Option2_marks=input("Enter Optional Subject 2 marks: ")
            self.total=self.English_marks+self.Physics_marks+self.Chemistry_marks+self.Option1_marks+self.Option2_marks
            self.Percentage=(self.total/500.0)*100

        def DisplayS(self):
            
            print "\n\n"
            print "PROGRESS REPORT".center(48,"*")
            print "Admission Number:", self.adminno
            print "Name:", self.name
            print "Grade:", self.grade
            print "\n\tMARKS\n"
            print "English      : ",self.English_marks
            print "Physics      : ",self.Physics_marks
            print "Chemistry    : ",self.Chemistry_marks
            print self.Option1+'     : ',self.Option1_marks
            print self.Option2+'        : ',self.Option2_marks
            print "\n Overall percentage: ",self.Percentage,"%"

class Commerce:

        def __init__(self):
            
            self.adminno=input("enter administration number:")
            self.name=raw_input("enter name:")
            self.grade=input("enter grade:")
            self.English_marks=input("Enter English marks  : ")
            self.Economics_marks=input("Enter Economics marks  : ")
            self.Accountancy_marks=input("Enter Accountancy marks: ")
            self.Option1=raw_input("Enter Optional Subject 1: ").capitalize()
            self.Option1_marks=input("Enter Optional Subject 1 marks: ")
            self.Option2=raw_input("Enter Optional Subject 2: ").capitalize()
            self.Option2_marks=input("Enter Optional Subject 2 marks: ")
            self.total=self.English_marks+self.Economics_marks+self.Accountancy_marks+self.Option1_marks+self.Option2_marks
            self.Percentage=(self.total/500.0)*100

        def DisplayC(self):

            print "\n\n"
            print "PROGRESS REPORT".center(48,"*")
            print "Admission Number:", self.adminno
            print "Name:", self.name
            print "Grade:", self.grade            
            print "\n\tMARKS\n"
            print "English      : ",self.English_marks
            print "Economics    : ",self.Economics_marks
            print "Accountancy  : ",self.Accountancy_marks
            print self.Option1+': ',self.Option1_marks
            print self.Option2+': ',self.Option2_marks
            print "\nOverall Percentage: ",self.Percentage,"%"                

class Humanities:

        def __init__(self):
            
            self.adminno=input("enter administration number:")
            self.name=raw_input("enter name:")
            self.grade=input("enter grade:")
            self.English_marks=input("Enter English marks  : ")
            self.History_marks=input("Enter History marks  : ")
            self.PoliticalScience_marks=input("Enter Political Science marks: ")
            self.Sociology_marks=input("Enter Sociology marks: ")
            self.Psychology_marks=input("Enter Psychology marks: ")
            self.total=self.English_marks+self.History_marks+self.PoliticalScience_marks+self.Sociology_marks+self.Psychology_marks
            self.Percentage=(self.total/500.0)*100

        def DisplayH(self):

            print "\n\n"
            print "PROGRESS REPORT".center(48,"*")
            print "Admission Number:", self.adminno
            print "Name:", self.name
            print "Grade:", self.grade
            print "\n\tMARKS\n"
            print "English          : ",self.English_marks
            print "History          : ",self.History_marks
            print "Political Science: ",self.PoliticalScience_marks
            print "Sociology        : ",self.Sociology_marks
            print "Psychology       : ",self.Psychology_marks
            print "\nOverall Percentage: ",self.Percentage,"%"

class MiddleSchool:

        def __init__(self):
            
            self.adminno=input("enter administration number:")
            self.name=raw_input("enter name:")
            self.grade=input("enter grade:")
            self.english=input("Enter English marks  : ")
            self.math=input("Enter  Maths marks  : ")
            self.science=input("Enter  science marks  : ")
            self.social=input("Enter  Social Studies marks  : ")
            self.language=input("Enter  Second Language marks  : ")
            self.totalpercent=float((self.english+self.math+self.science+self.social+self.language)/5)

        def display(self):

            print "\n\n"
            print "PROGRESS REPORT".center(48,"*")
            print "Admission Number:", self.adminno
            print "Name:", self.name
            print "Grade:", self.grade
            print "\n\tMARKS\n"
            print "English          : ",self.english
            print "Maths            : ",self.math
            print "Science          : ",self.science
            print "Social           : ",self.social
            print "Secondlanguage   : ",self.language
            print "\nOverall Percentage: ",self.totalpercent,"%"


def OnlineMarkRecords():

    def inputmarks():
        
        f=open("Marks.dat",'ab')                                
        pas=raw_input("enter school staff password to enter student marks:")
        if pas=='ooehs123':
            grade=input("enter grade for which marks are to be entered:")
            n=input("enter number of students")
            if grade<=10:
                for i in range(n):
                    Q=MiddleSchool()
                    dump(Q,f)
                    print '\n'                    
            elif grade==11 or grade==12:
                print "\n\t\tSTREAMS"
                print "S)Science"
                print "C)Commerce"
                print "H)Humanities"          
                print "Stream Taken (Science, Commerce, Humanitaries) "+"(S/C/H): ",
                stream=raw_input().upper()
                for i in range (n):
                    if stream=='S':
                        Q=Science()
                        dump(Q,f)
                        print '\n'
                    elif stream=='C':
                        Q=Commerce()
                        dump(Q,f)
                        print '\n'
                    elif stream=='H':
                        Q=Humanities()
                        dump(Q,f)
                        print '\n'
            else:
                print "Our school has grades from 1-12. Marks cannot be entered for any other grades."
        f.close()
                

    def outputmarks():
        
        f=open("Marks.dat",'rb')
        admin_no=input("Admission Number:")
        grade=input("Grade:")
        stream=raw_input("Stream Taken (Science, Commerce, Humanitaries)(S/C/H):")
        flag=0
        try:
            while True:
                Q=load(f)                                                
                if Q.adminno==admin_no:
                    if grade<=10:                      
                            Q.display()
                            print "*"*50
                    elif grade==11 or grade==12:
                        if stream=='S':
                                    Q.DisplayS()
                                    print "*"*50
                        elif stream=='C':
                                Q.DisplayC()
                                print "*"*50
                        elif stream=='H':
                                Q.DisplayH()
                                print "*"*50
                    flag=1
        except EOFError:
            pass
        if flag==0:
            print "Sorry, the admission number entered is invalid and/or does not exist."
        f.close()
        
        
    def allmarksdata():
            f=open("Marks.dat",'rb')
            flag=0
            pas=raw_input("Enter school staff password:")
            if pas=="ooehs123":
                grade=input("enter grade for which mark records are to be viewed:")
                try:
                    while True:
                        Q=load(f)                                                             
                        if grade<=10:
                            Q.display()
                            print '\n'
                        else:
                            stream=raw_input("Stream Taken (Science, Commerce, Humanitaries)(S/C/H):")
                            if stream=='S':
                                Q.DisplayS()
                                print "*"*50
                            elif stream=='C':                                
                                Q.DisplayC()
                                print "*"*50
                            elif stream=='H':                                
                                Q.DisplayH()
                                print "*"*50                                
                except EOFError:
                    pass
                flag=1
            else:
                print "Sorry, this information is confidential and only school staff can view it."
            f.close()
            
    while True:
            print """\n\nWelcome to the Online Results.
In this section you can:
(1)Input marks of student (For staff user)
(2)View your result
(3)View grade-wise academic results(For staff user)
(4)Exit result section"""
            
            choice=input("Enter your choice (1/2/3/4):")
            if choice==1:
                    inputmarks()
            elif choice==2:
                    outputmarks()
            elif choice==3:
                    allmarksdata()
            elif choice==4:
                    print "We hope the online fee records have been useful to you"
                    print "Goodbye."
                    break
            else:
                    print "Wrong choice"


################################################################################# END OF SECTION 3

class Library():

    def __init__(self):
        self.adminno=0
        self.issue_date=date.today()
        self.exp_return_date=0
        self.return_date=0
        self.fine=0
        self.title=None

    def inputlibrary(self,adno):
        self.adminno=adno
        self.issue_date=date.today()
        self.title=raw_input("enter book title:")
        self.exp_return_date=date.today()+timedelta(days=10)
        self.return_date=0
        self.fine=0

    def outputlibrary(self):
##        S.outputval()
        print " Admission No:",self.adminno
        print "Title of Book:", self.title
        print "Date of issue of book:", self.issue_date
        print "Date of return of book:", self.exp_return_date
        if self.return_date<>0:
            print self.return_date
        if self.fine<>0:
            print self.fine
            
    def outputlibrarytab(self):
        print self.adminno,"\t\t", self.title, "\t\t", self.issue_date,"\t\t",self.exp_return_date

p=Library()
            
def OnlineLibraryRecords():
    
    def issue_book():
        flag=0
        try:
            f=open("Book.dat", "ab+")
            admin_no=input("Admission Number:")
            while True:
                p=load(f)
                p.outputlibrary()
                if p.adminno==admin_no:
                    print " You have already taken the book. Only one book is allowed.\n You can return and take another book"
                    flag=1
                    break
        except EOFError:
            pass
        except IOError:
            print "File not created"

        f.close()
        if flag==1:
            return
        Novels={'Clay':'Claire North', 'The Great Gatsby':'Scott Fitzgerald', 'Inferno': 'Dan Brown', 'Triple': 'Ken Follett', 'Nature Girl':'Carl Haaisen', 'The Alchemist':'Paulo Coehlo','Paper Towns':'John Green','Lone Eagle':'Danielle Steele'}
        print '\n'
        print """We have a qualitative selection of books at our library.
    Please choose any ONE of the following as only one book per student is allowed."""
        print "Book Name\t\t\tAuthor"
        for i in Novels:
            print ("%-15s%25s"%(i,Novels[i]))
        print "Please enter the exact book title as shown in the above table (Case Sensitive)."
        p=Library()
        f=open("Book.dat", "ab")
        p.inputlibrary(admin_no)
        p.outputlibrary()
        dump(p,f)
        print "Your book has been issued. Good choice!"
        f.close()
        
    def display_records():
            f=open("Book.dat","rb")
            admin_no=input("Admission Number:")
            flag=0
            try:
                while True:
                    p=load(f)
                    if admin_no==p.adminno:
                        p.outputlibrary()
                        flag=1
            except EOFError:
                pass
            if flag==0:
                print "Sorry, the admission number entered is invalid and/or does not exist."
            f.close()
            
    def alllibrarydata():
        try:
            f=open("Book.dat","rb")
            print "Admin No \tTitle of Book\tDate of issue of book\t Date of return of book"
            while True:
                p=load(f)
                p.outputlibrarytab()
        except EOFError:
            f.close()
        except EOFError:
            print " No records"

    def return_book():
        f=open("Book.dat", 'rb')
        f1=open("newlib.dat",'wb')
        admin_no=input("Admission Number:")
        flag=0
        try:
            while True:
                p=load(f)
                if p.adminno==admin_no:
                    p.title=raw_input("enter title of book to be  returned:")
                    p.return_date=date.today()
                    if p.return_date>p.exp_return_date:
                        p.fine=abs(p.return_date-p.exp_return_date).days*2
                    if int(p.fine)>0:
                        print "Please pay the fine:",p.fine
                    flag=1
                else:
                    dump(p,f1)
        except EOFError:
            pass
        if flag==0:
            print "Sorry, the admission number entered is invalid and/or does not exist."
        f.close()
        f1.close()
        os.remove("Book.dat")
        os.rename("newlib.dat","Book.dat")
    
    while True:
            print """\n\nWelcome to the Online Library Records.
    In this section you can:
    (1)Issue books from the library
    (2)Return books to the library
    (3)Display your library records
    (4)Display all records of the library
    (5)Exit Library Section"""
            choice=input("Enter your choice (1/2/3/4/5):")
            if choice==1:
                    issue_book()
            elif choice==2:
                    return_book()
            elif choice==3:
                    display_records()
            elif choice==4:
                    alllibrarydata()        
            elif choice==5:
                    print "We hope the online library records have been useful to you"
                    print "Goodbye."
                    break
            else:
                    print "Wrong choice"
                
################################################################################# END OF SECTION 4
                                
def uniformsale():
    f=open("StudentDets.dat",'rb')
    admin_no=input("Admission Number:")
    flag=0
    try:
        while True:
            S=load(f)
            if S.adminno==admin_no:
                Uniform={'Skirt':30.00,'Shirt':20.00,'Beige Socks':10.00,'Brown Shoes':25.00,'Tie':12.00,'Belt':10.00,'Sweater':30.00,'Blazer':35.00, 'House T-Shirt':20.00, 'TrackPants':27.00,'White Socks':10.00,'White Shoes':25.00, 'Scrunchie':5.00,'Cream Scarf':15.00,'HeadBand':5.00}
                uni_list=list()
                uni_total=0.0
                while True:
                    print '\n'
                    print "Welcome to the online uniform store of our school. You may choose from the items given below."
                    print "We ensure the best quality material."
                    print "Product\t\tPrice"
                    for i in Uniform:
                            print ("%-15s%5.2f"%(i,Uniform[i]))
                    print "Please enter the exact item as shown in the above table (Case Sensitive)."
                    p=raw_input("Uniform item:")
                    qty=input("Quantity of item:")
                    uni_list.append((p,qty))
                    ch=raw_input("do you want to purchase anything else?(y/n)")
                    if ch=='n' or ch=='N':
                            break                
                print "Item\t\tPrice\tQuantity\tTotal Price"
                for i in uni_list:
                    a=i[0]
                    print("%-15s%5.2f%10d%15.2f"%(i[0], Uniform.get(a,0),i[1], Uniform.get(a,0)*i[1]))
                    uni_total+=Uniform.get(a,0)*i[1]
                print "Total amount \t\t\t\t", uni_total
                flag=1
    except EOFError:
        pass
    if flag==0:
        print "Sorry, the admission number entered is invalid and/or does not exist."
    f.close()
                         
def booksale():
    f=open("StudentDets.dat",'rb')
    admin_no=input("Admission Number:")
    flag=0
    try:
        while True:
            S=load(f)
            if S.adminno==admin_no:
                Books1to10={'Science':25.00,'Social Studies':25.00,'English':22.00,'Math':25.00, 'EVS':30.00, 'Hindi':35.00, 'French':34.50}
                Science={'Physics':22.00,'Chemistry':22.00,'Biology':22.00,'Computer':20.00,'Math':22.00,'English':20.00,'HomeScience':22.00}
                Commerce={'Accountancy':22.00,'Economics':22.00,'Marketing':22.00,'Business':24.00,'Math':22.00,'English':20.00,'Informatics':22.00}
                Humanitaries={'History':22.00,'Sociology':22.00,'Psychology':22.00,'History':20.00,'Political Science':20.00,'English':20.00}
                if S.grade in [1,2,3,4,5,6,7,8,9,10]:
                    d= Books1to10
                elif S.grade in [11,12]:
                    stream=raw_input("Stream (Science, Commerce, Humanitaries)(S/C/H)")
                    if stream=="S":
                        d=Science
                    elif stream=="C":
                        d=Commerce
                    elif stream=="H":
                        d=Humanitaries
                
                book_list=list()
                book_total=0.0
                while True:
                    print '\n'
                    print "Welcome to the online book store of our school. You may choose from the items given below."
                    print "We ensure the best quality books."
                    print "Book Title\tPrice"
                    for i in d:
                        print ("%-15s%5.2f"%(i,d[i]))
                    print "Please enter the exact item as shown in the above table (Case Sensitive)."
                    p=raw_input("Book required:")
                    qty=input("Quantity of item:")
                    book_list.append((p,qty))
                    ch=raw_input("do you want to purchase anything else?(y/n)")
                    if ch=='n' or ch=='N':
                            break                
                print "Book Title\tPrice\tQuantity\tTotal Price"
                for i in book_list:
                        a=i[0]
                        print("%-15s%5.2f%10d%15.2f"%(i[0],d.get(a,0),i[1], d.get(a,0)*i[1]))
                        book_total+=d.get(a,0)*i[1]
                print "Total amount \t\t\t\t", book_total
                flag=1
    except EOFError:
        pass
    if flag==0:
        print "Sorry, the admission number entered is invalid and/or does not exist."
    f.close()


################################################################################# END OF SECTION 5
                
while True:
    print '\n'
    print "*"*50
    print """Welcome to our school's online forum.
How may we help you?

(1)Online Admission Details
(2)Online Uniform Purchase
(3)Online Book Store
(4)Online Fee Payment
(5)Online Report
(6)Online Library Records
(7)Exit Forum

Note: Your data security matters most to us at this school.
Thus your admission number is your key to all the sections of program."""
    print '\n'
    choice=input("enter your choice (1/2/3/4/5/6/7):")
    if choice==1:
        OnlineAdministrationRecords()
    elif choice==2:
        uniformsale()
    elif choice==3:
        booksale()
    elif choice==4:
        OnlineFeeRecords()
    elif choice==5:
        OnlineMarkRecords()
    elif choice==6:
        OnlineLibraryRecords()
    elif choice==7:
        print """You have left the online forum.
We hope you have been able to benefit from all sections of this forum.
Have a nice day. Goodbye."""
        break
    else:
        print "Wrong choice"
        
######################################################################## END OF PROGRAM        