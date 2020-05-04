class GradeProgram:
    def __init__(self):
        self.hakbunlist = []
        self.namelist = []
        self.korlist = []
        self.englist = []
        self.mathlist = []
        self.totlist = []
        self.avglist = []
        self.gradelist = []

    def readList(self):
        flag = True
        print("프로그램을 종료하려면 학번에 '0'을 입력하시오")
        while flag:
            hakbun = input('학번을 입력하시오: ')
            if hakbun == '0':
                flag = False
            else:
                name = input('이름을 입력하시오: ')
                kor = int(input('국어점수를 입력하시오: '))
                eng = int(input('영어점수를 입력하시오: '))
                math = int(input('수학점수를 입력하시오: '))

                self.hakbunlist.append(hakbun)
                self.namelist.append(name)
                self.korlist.append(kor)
                self.englist.append(eng)
                self.mathlist.append(math)

        return self.hakbunlist, self.namelist, self.korlist, self.englist, self.mathlist

    def calList(self):

        total = 0
        avg = 0.0

        for i in range(0,len(self.korlist)):
            total = self.korlist[i] + self.englist[i] + self.mathlist[i]
            avg = total / 3

            self.totlist.append(total)
            self.avglist.append(avg)

            if avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            elif avg >= 70:
                grade = 'C'
            elif avg >= 60:
                grade = 'D'
            else:
                grade = 'F'

            self.gradelist.append(grade)

        return self.totlist, self.avglist, self.gradelist

    def printList(self):
        print('=' * 70)
        print('번호  이름  국어  영어  수학  총점  평균  학점')
        print('=' * 70)
        for i in range(len(self.hakbunlist)):
            print('%3s %5s %3d  %3d  %3d  %3d  %.2f  %s' % (
                self.hakbunlist[i], self.namelist[i], self.korlist[i], self.englist[i], self.mathlist[i], self.totlist[i], self.avglist[i], self.gradelist[i]))

    def main(self):
        hakbunlist, namelist, korlist, englist, mathlist = self.readList()
        totlist, avglist, hakjumlist = self.calList()
        self.printList()


myGrade = GradeProgram()
myGrade.main()
