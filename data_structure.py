a = float(input("정수 1 입력하시오"))
b = float(input("정수 2 입력하시오"))
c = input("연산자 입력하시오")

if c == '*' :
    d = a*b
elif c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '/':
    d = a//b
elif c == '**':
    d = a**b
else :
    print("시벌로마 제대로 입력해라")

print("결과는 : ", d , " 입니다")
#--------------------------------------------------
'''------------------------------------------------'''
def summer(n) :
    for a in range (1,101,2) :
        n += a

    return n

n = int(input("insert number"))
print("result is : ", summer(n))
