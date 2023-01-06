#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, mid, final) :
    #사전에 학생 정보 저장하는 코딩 
    score1 = int(mid)
    score2 = int(final)
    studentList.append([name, score1, score2])

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(studentList)):
        if len(studentList[i]) != 4:
          avg = (studentList[i][1] + studentList[i][2]) / 2
          if avg >= 90:
              grade = 'A'
          elif 80 <= avg < 90:
              grade = 'B'
          elif 70 <= avg < 80:
              grade = 'C'
          else :
              grade = 'D'
          studentList[i].append(grade)

##############  menu 3
def Menu3() :
    #출력 코딩
    print("-------------------------------")
    print("name        mid    final  grade")
    print("-------------------------------")
    for i in range(len(studentList)):
        print("{0:<9}   {1:<4}   {2:<4}   {3:<3}".format(studentList[i][0], studentList[i][1], studentList[i][2], studentList[i][3]))

##############  menu 4
def Menu4(studentName):
    #학생 정보 삭제하는 코딩
    for i in range(len(studentList)):
        if studentName == studentList[i][0] :
          del studentList[i]
          break

#학생 정보를 저장할 변수 초기화
studentList = []
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        try:
            name, mid, final = map(str, input('Enter name mid-score final-score : ').split())
            if '.' in mid or '.' in final:
                raise Exception('Score is not positive integer!')
            for i in range(len(studentList)):
              if studentList[i][0] == name:
                raise Exception('Already exist name!')
        except ValueError as e:
            print("Num of data is not 3!")
        except Exception as e:
            print(e)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        else:
            Menu1(name, mid, final)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #"Grading to all students." 출력
        try:
            if len(studentList) == 0:
                raise Exception('No student data!')
            print("Grading to all students")
        except Exception as e:
            print(e)
        #예외사항이 아닌 경우 2번 함수 호출
        else:
            Menu2()

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        try:
            if len(studentList) == 0:
                raise Exception('No student data!')
            for i in range(len(studentList)):
                if len(studentList[i]) != 4:
                  raise Exception("There is a student who didn't get grade")
        except Exception as e:
            print(e)
        #예외사항이 아닌 경우 3번 함수 호출       
        else:
            Menu3()    
            
    elif choice == "4" :
        try:
            if len(studentList) == 0:
                raise Exception ('No Student data!')
            studentName = input('Enter the name to delete : ')
            studentNameList = []
            for i in studentList:
                studentNameList.append(i[0])
            if studentName not in studentNameList:
                raise Exception ('Not exist name')
        except Exception as e:
            print(e)
        else:
            Menu4(studentName)
            print("{0} student information is deleted".format(studentName))
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!")
        break
        

    else :
        print("Wrong number. Choose again.")
