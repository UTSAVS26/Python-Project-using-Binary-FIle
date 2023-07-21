import os
import pickle

#===============ADMISSION===============
#Inserting New Admission Data to binary file
def addNewStuRecord():
     import pickle
     admno=input("Enter Admission No.: ")
     name=input("Enter Student Name: ")
     cls=input("Enter Class: ")
     admfee=input("Enter Fees: ")
     fatname=input("Enter your Father's Name: ")
     motname=input("Enter your Mother's Name: ")
     age=input("Enter your Age: ")
     phoneno=input("Enter Phone No.: ")
     email_id=input("Enter Email ID: ")
     beh_data=input("Enter Behavior Data (Good/Bad): ")
     hel_data=input("Enter Health Data (Good/Bad): ")
     L={}
     #Creating a Dictionary to hold a Student Data
     L["Admission No.: "]=admno
     L["Name: "]=name
     L["Class: "]=cls
     L["Admission Fees: "]=admfee
     L["Father's Name: "]=fatname
     L["Mother's Name: "]=motname
     L["Age: "]=age
     L["Phone Number: "]=phoneno
     L["Email ID: "]=email_id
     L["Behavior Data: "]=beh_data
     L["Health Information: "]=hel_data
     #Writing this Dictionary record to file
     f=open("NewStudentData.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n')
     f.close()

     f = open("NewStudentData1.dat","ab")
     data_log = []
     pno = admno
     pname = name
     pcls=cls
     pfee=admfee
     pfatname=fatname
     pmotname=motname
     page=age
     pphoneno=phoneno
     pemail=email_id
     pbeh=beh_data
     phel=hel_data
     data_log.append([pno,pname,pcls,pfee,pfatname,pmotname,page,pphoneno,pemail,pbeh,phel])
     pickle.dump(data_log,f)
     f.close()
     print("New Student Record Added Successfully to Both Text and Binary File.")
    

#Reading the New Student Records of File
def displayNewStuRecord():
     import pickle
     f=open("NewStudentData1.dat","rb+")
     f1=pickle.load(f)
     for x in f1.split():
          print(x)
     f.close()

#Searching a New Student Record based on Roll No. in the File
def searchNewStuRecord():
     import pickle
     f=open("NewStudentData.txt","r")
     roll_find=int(input('Roll no. of the student to find: '))
     currentline = 1
     for line in f:
          if(currentline == roll_find):
               print(line)
               break
          currentline = currentline +1

#Updating the Records of File
def updateNewStuPhone(r,m):
     import pickle
     f=open("NewStudentData1.dat","rb")
     stuLst=[]
     while True:
          try:
               stu=pickle.load(f)
               stuLst.append(stu)
          except EOFError:
               break
     f.close()
     for i in range(len(stuLst)):
          if stuLst[i][0]==r:
               stuLst[i][7]=m
     f=open("NewStudentData1.dat","wb")
     for x in stuLst:
          pickle.dump(x,f)
     print("Phone No. Updated Successfully.")
     f.close()


#===============STUDENT===============     
#Inserting New Student Data to binary file
def addRecord():
     import pickle
     rno=input("Enter Roll No.: ")
     name=input("Enter Student Name: ")
     cls=input("Enter Class: ")
     sec=input("Enter Section of Class: ")
     marks=input("Enter Total Marks: ")
     '''hin_cs=int(input("Enter Marks in Hindi/CS: "))
     eng=int(input("Enter Marks in English: "))
     math_bio=int(input("Enter Marks in Maths/Biology: "))'''
     L={}
     #Creating a Dictionary to hold a Student Data
     L["Roll No.: "]=rno
     L["Name: "]=name
     L["Class: "]=cls
     L["Section: "]=sec
     L["Total Marks: "]=marks
     #Writing this Dictionary record to file
     f=open("StudentData.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n')
     f.close()
     print("One Student Record Added Successfully to File.")
     f = open("StudentData1.dat","ab")
     data_log = []
     pcode = rno
     pname = name
     pcls = cls
     psec = sec
     pmark = marks
     data_log.append([pcode,pname,pcls,psec,pmark])
     pickle.dump(data_log,f)
     f.close()
     print("Student Record Added Successfully to Both Text and Binary File.")

#Reading the Records of File
def displayRecord():
     import pickle
     f=open("StudentData.txt","r")
     f1=f.readlines()
     for x in f1:
          print(x)
     f.close()

#Searching a Record based on Roll No. in the File
def searchRecord():
     import pickle
     f=open("StudentData.txt","r")
     roll_find=int(input('Roll no. of the student to find: '))
     currentline = 1
     for line in f:
          if(currentline == roll_find):
               print(line)
               break
          currentline = currentline +1
      
#Update Marks for a Roll No. in a File
def updateMarks(r,m):
     import pickle
     f=open("StudentData1.dat","rb")
     stuLst=[]
     while True:
          try:
               stu=pickle.load(f)
               stuLst.append(stu)
          except EOFError:
               break
     f.close()
     for i in range(len(stuLst)):
          if stuLst[i][0]==r:
               stuLst[i][4]=m
     f=open("StudentData1.dat","wb")
     for x in stuLst:
          pickle.dump(x,f)
     print("Marks Updated Successfully.")
     f.close()

#Delete a Record from File
def deleteRecord():
     import pickle
     f = open("StudentData.txt","r")
     pc=input("Enter Roll No. to delete Record: ")
     output=[]
     for line in f:
          if not pc in line:
               output.append(line)
     f.close()
     f=open("StudentData.txt","w")
     f.writelines(output)
     f.close()
     print("Record Deleted Successfully.....")


#===============Fees===============     
#Display Fees and Inserting in Binary File
def Seefees():
     f=open("DisplayFees.txt","a+")
     cl=input("Enter Class: ")
     tuition = int(input("Enter fees for Month: "))
     total = 0
     n=int(input("Enter No. of Years you want to See (Total Fees): "))
     print("Year\t", "Fees Per Year")

     for i in range(1,n+1):
          tuition += tuition*12
          #Displays tuition fee for each year
          print(i,'\t',format(tuition, '.2f'))

     total += tuition
     L=str(total)
     print("Total tuition in ",n," years: ₹", format(total,'.2f'),sep = ' ')
     S="Total Tuition Cost for Class "+str(cl)+" in "
     A=str(n)+" years: "
     f.writelines(S)
     f.writelines(A)
     f.writelines(L)
     f.write('\n')
     f.close()

     f=open("DisplayFees1.dat","ab+")
     ps,pa,pl=str(S),str(A),str(L)
     data_log=[]
     data_log.append([ps,pa,pl])
     pickle.dump(data_log,f)
     print("Fees Record Added Successfully to Both Text and Binary File.")

#Depositing Fees and Inserting in Binary File
def Depositfees():
     f=open("DepositFees.txt","a+")
     name=input("Enter Name of Student: ")
     cl=input("Enter Class: ")
     tuition = int(input("How much Fees you want to Deposit: "))
     total = 0
     L={}
     #Creating a Dictionary to Depositing  Student Fees
     L["Name: "]=name
     L["Class: "]=cl
     L["Fees: "]=tuition
     f.close()
     #Writing this Dictionary record to file
     f=open("DepositFees.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n')
     f.close()
     f=open("DepositFees1.dat","ab+")
     data_log=[]
     pname=name
     pcl=cl
     ptuition=tuition
     data_log.append([pname,pcl,ptuition])
     pickle.dump(data_log,f)
     print("Fees Deposit Successfully.....")


#===============Attendance===============     
#Staff Attendance in Binary File
def staffattendancerecord():
     c=input("Enter Teacher Name: ")
     d=input("Enter Date: ")
     e=input("Enter Arriving Time: ")
     g=input("Enter Departure Time: ")
     L={}
     L["Name: "]=c
     L["Date: "]=d
     L["Arriving Time: "]=e
     L["Departure Time: "]=g
     f=open("StaffAttendanceData.txt","a+")
     D=str(L)
     f.write(D)
     f.close()

     f=open("StaffAttendanceData1.dat","ab+")
     pc,pd,pe,pg=c,d,e,g
     data_log=[]
     data_log.append([pc,pd,pe,pg])
     pickle.dump(data_log,f)
     print("Staff Attendance Recorded...")

#Student Attendance in Binary File
def studentattendancerecord():
     c=input("Enter Student Name: ")
     d=input("Enter Class: ")
     e=input("Enter Class Teacher Name: ")
     g=input("Enter Date: ")
     S=input("Enter Present(P)/Absent(A): ")
     L={}
     L["Name: "]=c
     L["Class: "]=d
     L["Class Teacher: "]=e
     L["Date: "]=g
     L["Present(P)/Absent(A): "]=S
     f=open("StudentAttendanceData.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()

     f=open("StudentAttendanceData1.dat","ab+")
     pc,pd,pe,pg=c,d,e,g
     data_log=[]
     data_log.append([pc,pd,pe,pg])
     pickle.dump(data_log,f)
     print("Student Attendance Recorded...")


#===============Exam Management===============     
#Exam Datesheet in Binary File
def examdatesheet():
     c=input("Enter Class (9th/10th/11th/12th): ")
     d=input("Enter 1st Exam Date: ")
     e=input("Enter 1st Subject Name: ")
     g=input("Enter 2nd Exam Date: ")
     h=input("Enter 2nd Subject Name: ")
     i=input("Enter 3rd Exam Date: ")
     j=input("Enter 3rd Subject Time: ")
     k=input("Enter 4th Exam Date: ")
     l=input("Enter 4th Subject Time: ")
     m=input("Enter 5th Exam Date: ")
     n=input("Enter 5th Subject Time: ")
     L={}
     L["Class: "]=c
     L["1st Exam Date: "]=d
     L["1st Subject Name: "]=e
     L["2nd Exam Date: "]=g
     L["2nd Subject Name: "]=h
     L["3rd Exam Date: "]=i
     L["3rd Subject Name: "]=j
     L["4th Exam Date: "]=k
     L["4th Subject Name: "]=l
     L["5th Exam Date: "]=m
     L["5th Subject Name: "]=n
     f=open("ExamDatesheet.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()

     f=open("ExamDatesheet1.dat","ab+")
     pc,pd,pe,pg,ph,pi,pj,pk,pl,pm,pn=c,d,e,g,h,i,j,k,l,m,n
     data_log=[]
     data_log.append([pc,pd,pe,pg,ph,pi,pj,pk,pl,pm,pn])
     pickle.dump(data_log,f)
     f.close()
     print("Exam Datesheet Created Successfully...")
     
#Teacher In-Charge in Binary File
def teacherincharge():
     print("Total No. of Rooms Free For Exams = 15")
     c=input("Enter Room Number: ")
     d=input("Enter Teacher Name: ")
     e=input("Enter Class (9th/10th/11th/12th): ")
     if e=='9th':
          print("\tTotal No.of Students of Class 9th: 60")
     elif e=='10th':
          print("\tTotal No.of Students of Class 10th: 60")
     elif e=='11th':
          print("\tTotal No.of Students of Class 11th: 55")
     elif e=='12th':
          print("\tTotal No.of Students of Class 12th: 55")
     print("Enter Total No. Of Students who Sit in Room No.",c,": ",sep=' ')
     g=input()
     L={}
     L["Room Number: "]=c
     L["Teacher Name: "]=d
     L["Class: "]=e
     L["Siting Arrangement in that Room: "]=g
     f=open("TeacherInChargeData.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()

     f=open("TeacherInChargeData1.dat","ab+")
     pc,pd,pe,pg=c,d,e,g
     data_log=[]
     data_log.append([pc,pd,pe,pg])
     pickle.dump(data_log,f)
     print("Teacher In Charge Record Added Successfully...")


#===============Result Management===============     
#Result in Binary File
def result():
     c=input("Enter Student Name: ")
     d=input("Enter Class: ")
     e=input("Enter Admission No.: ")
     S=input("Enter your Father's Name: ")
     g=input("Enter your Mother's Name: ")
     h=input("Enter your Age: ")
     i=input("Enter Phone No.: ")
     j=input("Enter Behavior Data (Good/Bad): ")
     k=input("Enter Health Data (Good/Bad): ")
     L={}
     L["Name: "]=c
     L["Class: "]=d
     L["Admission No.: "]=e
     L["Father's Name: "]=S
     L["Mother's Name: "]=g
     L["Age: "]=h
     L["Phone Number: "]=i
     L["Behavior Data: "]=j
     L["Health Information: "]=k
     f=open("StudentResult.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()
     print('\n')
     f=open("StudentResult1.dat","ab+")
     pc,pd,pe,pS,pg,ph,pi,pj,pk=c,d,e,S,g,h,i,j,k
     data_log=[]
     data_log.append([pc,pd,pe,pS,pg,ph,pi,pj,pk])
     pickle.dump(data_log,f)
     f.close()
     ch=input("You Want to See the Report Card or Not (y/n): ")
     while ch=='y':
          B,C,D,E,F,G,H,I,J,K="REPORT CARD","NAME=","CLASS=","ADMISSION NO.=","FATHER'S NAME=","MOTHER'S NAME=","AGE=","PHONE NO.=","BEHAVIOUR DATA=","HEALTH INFORMATION="
          print("<>"*50)
          print("\t\t\t\t","REPORT CARD","\n")
          print(C,c,'\t\t',D,d,'\t\t',E,e,'\n',F,S,'\t\t',G,g,'\n',H,h,'\t\t\t\t\t\t',I,i,'\n',J,j,'\t\t\t\t\t',K,k)
          print("<>"*50)
          print("--"*85)
          ch='n'     


#===============Achievement Management===============     
#Achievement Record in Binary File
def achievementrecord():
     print("In Which Field You Want to Enter Record: ")
     print("\t1 Academic Excellence Award")
     print("\t2 Student of the Year")
     print("\t3 Participating Certificate")
     print("\t4 Teamwork Award")
     choice=int(input("Enter Your Choice: "))
     if choice==1:
          c=input("Enter Student Name: ")
          d=input("Enter Class: ")
          e=input("Enter Class Position: ")
          S=input("Enter Class Teacher Name: ")
          h=input("Enter your Age: ")
          i=input("Enter Phone No.: ")
          L={}
          L["Name: "]=c
          L["Class: "]=d
          L["Class Position: "]=e
          L["Class Teacher: "]=S
          L["Age: "]=h
          L["Phone Number: "]=i
          print('\n')
          ch=input("You Want to See the Record or Not (y/n): ")
          f=open("AcademicExcellenceAwardList.txt","a+")
          D=str(L)
          f.write(D)
          f.write('\n\n')
          f.close()
          f=open("AcademicExcellenceAwardList1.dat","ab+")
          pc,pd,pe,pS,ph,pi=c,d,e,S,h,i
          data_log=[]
          data_log.append([pc,pd,pe,pS,ph,pi])
          pickle.dump(data_log,f)
          f.close()
          while ch=='y':
               B,C,D,E,F,G,H="ACADEMIC EXCELLENCE AWARD","NAME=","CLASS=","CLASS POSITION=","CLASS TEACHER=","AGE=","PHONE NO.="
               print("<>"*50)
               print("\t\t\t",B,"\n")
               print(C,c,'\t\t\t',D,d,'\t\t\t',E,e,'\n',F,S,'\t\t',G,h,'\t\t\t',H,i)
               print("<>"*50)
               ch='n'
     elif choice==2:
          c=input("Enter Student Name: ")
          d=input("Enter Class: ")
          e=input("Enter Principal Name: ")
          S=input("Enter Class Teacher Name: ")
          h=input("Enter your Age: ")
          i=input("Enter Phone No.: ")
          L={}
          L["Name: "]=c
          L["Class: "]=d
          L["Principal Name: "]=e
          L["Class Teacher Name: "]=S
          L["Age: "]=h
          L["Phone Number: "]=i
          print('\n')
          ch=input("You Want to See the Record or Not (y/n): ")
          f=open("StudentOfTheYear.txt","a+")
          D=str(L)
          f.write(D)
          f.write('\n\n')
          f.close()
          f=open("StudentoFTheYear1.dat","ab+")
          pc,pd,pe,pS,ph,pi=c,d,e,S,h,i
          data_log=[]
          data_log.append([pc,pd,pe,pS,ph,pi])
          pickle.dump(data_log,f)
          f.close()
          while ch=='y':
               B,C,D,E,F,G,H="STUDENT OF THE YEAR","NAME=","CLASS=","PRINCIPAL NAME=","CLASS TEACHER NAME=","AGE=","PHONE NO.="
               print("<>"*50)
               print("\t\t\t\t\t\t",B,"\n")
               print(C,c,'\t\t\t',D,d,'\t\t\t',E,e,'\n',F,S,'\t\t',G,h,'\t\t\t',H,i)
               print("<>"*50)
               ch='n'
     elif choice==3:
          c=input("Enter Student Name: ")
          d=input("Enter Class: ")
          e=input("Enter Class Teacher Name: ")
          S=input("Enter Field Name (Debate/Story Writing/Poster Making/Fancy Dress/Any other Field): ")
          h=input("Enter your Age: ")
          i=input("Enter Phone No.: ")
          L={}
          L["Name: "]=c
          L["Class: "]=d
          L["Class Teacher Name: "]=e
          L["Field Of Achievement: "]=S
          L["Age: "]=h
          L["Phone Number: "]=i
          print('\n')
          ch=input("You Want to See the Record or Not (y/n): ")
          f=open("ParticipatingAwardData.txt","a+")
          D=str(L)
          f.write(D)
          f.write('\n\n')
          f.close()
          f=open("ParticipatingAwardList1.dat","ab+")
          pc,pd,pe,pS,ph,pi=c,d,e,S,h,i
          data_log=[]
          data_log.append([pc,pd,pe,pS,ph,pi])
          pickle.dump(data_log,f)
          f.close()
          while ch=='y':
               B,C,D,E,F,G,H="PARTICIPATING CERTIFICATE","NAME=","CLASS=","CLASS TEACHER NAME=","FIELD OF ACHIEVEMENT=","AGE=","PHONE NO.="
               print("<>"*50)
               print("\t\t\t\t\t\t",B,"\n")
               print(C,c,'\t\t\t\t',D,d,'\n',E,e,'\t\t',F,S,'\n',G,h,'\t\t\t\t\t',H,i)
               print("<>"*50)
               ch='n'
     elif choice==4:
          c=input("Enter Student Name: ")
          d=input("Enter Class: ")
          e=input("Enter Class Teacher Name: ")
          S=input("Enter Field Name (Conflict resolution/Decision-making/Problem-solving/Any other Field): ")
          g=input("Enter Member's Name (Using Commas): ")
          L={}
          L["Name: "]=c
          L["Class: "]=d
          L["Class Teacher Name: "]=e
          L["Field Of Achievement: "]=S
          L["Member's Name: "]=g
          print('\n')
          ch=input("You Want to See the Record or Not (y/n): ")
          f=open("TeamworkAwardData.txt","a+")
          D=str(L)
          f.write(D)
          f.write('\n\n')
          f.close()
          f=open("TeamworkAwardData1.dat","ab+")
          pc,pd,pe,pS,pg=c,d,e,S,g
          data_log=[]
          data_log.append([pc,pd,pe,pS,pg])
          pickle.dump(data_log,f)
          f.close()
          while ch=='y':
               B,C,D,E,F,G="TEAMWORK AWARD","NAME=","CLASS=","CLASS TEACHER NAME=","FIELD OF ACHIEVEMENT=","MEMBER'S NAME="
               print("<>"*50)
               print("\t\t\t\t\t\t",B,"\n")
               print(C,c,'\t\t\t\t',D,d,'\n',E,e,'\t\t',F,S,'\n',G,g)
               print("<>"*50)
               ch='n'
     else:
          print("Invalid Choice.")


#===============BOOKS RECORD===============     
#Old Stock in Binary File
def oldstock():
     c=input("Enter 1st Book Name: ")
     d=input("Enter 1st book Quantity: ")
     e=input("Enter 2nd Book Name: ")
     g=input("Enter 2nd book Quantity: ")
     h=input("Enter 3rd Book Name: ")
     i=input("Enter 3rd book Quantity: ")
     L={}
     L["1st Book Name: "]=c
     L["1st Book Quantity: "]=d
     L["2nd Book Name: "]=e
     L["2nd Book Quantity: "]=g
     L["3rd Book Name: "]=h
     L["3rd Book Quantity: "]=i
     f=open("OldStock.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()
     f=open("OldStock1.dat","ab+")
     pc,pd,pe,pg,ph,pi=c,d,e,g,h,i
     data_log=[]
     data_log.append([pc,pd,pe,pg,ph,pi])
     pickle.dump(data_log,f)
     f.close()

#New Stock in Binary File
def newstock():
     c=input("Enter 1st Book Name: ")
     d=input("Enter 1st book Quantity: ")
     e=input("Enter 2nd Book Name: ")
     g=input("Enter 2nd book Quantity: ")
     h=input("Enter 3rd Book Name: ")
     i=input("Enter 3rd book Quantity: ")
     L={}
     L["1st Book Name: "]=c
     L["1st Book Quantity: "]=d
     L["2nd Book Name: "]=e
     L["2nd Book Quantity: "]=g
     L["3rd Book Name: "]=h
     L["3rd Book Quantity: "]=i
     f=open("NewStock.txt","a+")
     D=str(L)
     f.write(D)
     f.write('\n\n')
     f.close()
     f=open("NewStock1.dat","ab+")
     pc,pd,pe,pg,ph,pi=c,d,e,g,h,i
     data_log=[]
     data_log.append([pc,pd,pe,pg,ph,pi])
     pickle.dump(data_log,f)
     f.close()


while True:
     print("\n\t\t======================================")
     print("\t\t          STUDENT MANAGEMENT SYSTEM          ")
     print("\t\t=======================================")
     print("\t\t\t1 Admission")
     print("\t\t\t2 Student")
     print("\t\t\t3 Fees")
     print("\t\t\t4 Attendance")
     print("\t\t\t5 Exam Management")
     print("\t\t\t6 Result Management")
     print("\t\t\t7 Achievement Record")
     print("\t\t\t8 Books Record")
     print("\t\t\t9 Exit")
     print("\t\t______________________________________")
     choice=int(input("\nEnter your Choice: "))
     if choice==1:
          print("Type 1 to Add New Student Data to File.")
          print("Type 2 to Display All New Student Data to File.")
          print("Type 3 to Search a Student Data to File.")
          print("Type 4 to Update Phone Number to File.")
          print("Type 5 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               addNewStuRecord()
          elif ch==2:
               displayNewStuRecord()
          elif ch==3:
               searchNewStuRecord()
          elif ch==4:
               r=input("Enter Roll No. of Student to Update Phone No.: ")
               m=int(input("Enter New Phone No. to Update: "))
               updateNewStuPhone(r,m)
          elif ch==5:
               continue
     elif choice==2:
          print("Type 1 to Add New Student Data to File.")
          print("Type 2 to Display All Student Data to File.")
          print("Type 3 to Search a Student Data to File.")
          print("Type 4 to Update Student Marks to File.")
          print("Type 5 to Delete Student Record.")
          print("Type 6 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               addRecord()
          elif ch==2:
               displayRecord()
          elif ch==3:
               searchRecord()
          elif ch==4:
               r=input("Enter Roll No. of Student to Update Marks: ")
               m=int(input("Enter Marks to Update: "))
               updateMarks(r,m)
          elif ch==5:
               deleteRecord()
          elif ch==6:
               continue
     elif choice==3:
          print("Type 1 to See Fees According to Class.")
          print("Type 2 to Display If Deposit.")
          print("Type 3 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               Seefees()
          elif ch==2:
               Depositfees()
          elif ch==3:
               continue
     elif choice==4:
          print("Type 1 to Staff Attendance.")
          print("Type 2 to Students Attendance.")
          print("Type 3 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               staffattendancerecord()
          elif ch==2:
               studentattendancerecord()
          elif ch==3:
               continue
     elif choice==5:
          print("Type 1 to Exam Datesheet.")
          print("Type 2 to Teacher In-Charge in Room.")
          print("Type 3 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               examdatesheet()
          elif ch==2:
               teacherincharge()
          elif ch==3:
               continue
     elif choice==6:
          print("Type 1 to Add and Display Result.")
          print("Type 2 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               result()
          elif ch==2:
               continue
     elif choice==7:
          print("Type 1 to Add and Display Achievement Record.")
          print("Type 2 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               achievementrecord()
          elif ch==2:
               continue
     elif choice==8:
          print("Type 1 to Add Details of Old Stock.")
          print("Type 2 to Add Details of New Stock.")
          print("Type 3 Exit.")
          ch=int(input("\nEnter your Choice: "))
          if ch==1:
               oldstock()
          elif ch==2:
               newstock()
          else:
               continue
     elif choice==9:
          exit()
