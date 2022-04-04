try:
    str=input("문자를 입력하세요>>")
except EOFError:
    print("입력문자가 없습니다!!!!!")

except KeyboardInterrupt:
    print("취소됨!!!")
else:
    print("당신이 입력한 문자는 {}".format(str))
finally:
    print("명령을 수행하였습니다")