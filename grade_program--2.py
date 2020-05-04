class Student :
    def __init__ (self) :
        self.hakbunlist = []
        self.namelist = []
        self.korlist = []
        self.englist = []
        self.mathlist = []

        flag = True
        print("프로그램을 종료하려면 학번에 '0'을 입력하시오")

        while flag:
            hakbun = input("학번을 입력하시오 : ")
            if hakbun == '0':
                flag = False

            else:
                name = input("이름을 입력하시오 : ")
                kor = int(input("국어 점수를 입력하시오 : "))
                eng = int(input("영어 점수를 입력하시오 : "))
                math = int(input("수학 점수를 입력하시오 : "))

                self.hakbunlist.append(hakbun)
                self.namelist.append(name)
                self.korlist.append(kor)
                self.englist.append(eng)
                self.mathlist.append(math)

        self.totlist = []
        self.avglist = []
        self.gradelist = []

        total = 0
        avg = 0.0

        for i in range(len(self.korlist)) :
            total = self.korlist[i] + self.englist[i] + self.mathlist[i]
            avg = total / 3.0

        if avg >= 90 :
            grade = 'A'
        elif avg >= 80 :
            grade = 'B'
        elif avg >= 70 :
            grade = 'C'
        elif avg >= 60 :
            grade = 'D'
        else :
            grade = 'F'
        self.gradelist.append(grade)

        # return self.hakbunlist, self.namelist, self.korlist, self.englist, self.mathlist

    def main(self):
        print('=' * 70)
        print(" 번호\t\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
        print('=' * 70)
        for i in range(len(self.hakbunlist)):
            print('%3s\t%5s\t%3d\t\t%3d\t\t%3d\t\t%3d\t\t%.2f\t\t%s'% (
                self.hakbunlist[i], self.namelist[i], self.korlist[i], self.mathlist[i], self.totlist[i], self.avglist[i], self.gradelist[i]))


score = Student()

if __name__ == '__main__':
    score.main()


