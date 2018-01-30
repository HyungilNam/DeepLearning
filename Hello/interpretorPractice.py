
print('<<<리스트 예시>>>')
print('리스트 생성')
a = [1, 2, 3, 4, 5]
print(a)
print('리스트 길이 출력')
print(len(a))
print('첫 원소에 접근')
print(a[0])
print('다섯번째 원소에 접근')
print(a[4])
print('다섯번째 원소 변경 후 출력')
a[4] = 99
print(a)
print('----------------------------------------------')
print('<<<딕셔너리 예시>>>')
print('딕셔너리 생성')
me = {'height':180}
print(me)
print('원소에 접근')
print(me['height'])
print('새 원소 추가')
me['weight'] = 70
print(me)
print('----------------------------------------------')
print('<<<bool 예시>>>')
print('배고프다가 hungry = True, 졸리지 않다가 sleepy = False')
hungry = True		#배가 고프다
sleepy = False		#졸리지 않다
print('hungry의 자료형 >>>' + str(type(hungry)))
print('hungry 반대 출력 >>>' + str(not hungry))
print('배가 고프다 그리고 졸리지 않다 >>>'+str(hungry and sleepy))
print('배가 고프다 또는 졸리지 않다 >>>'+str(hungry or sleepy))
print('----------------------------------------------')
print('<<<if문 예시>>>')
if hungry:
    print('hungry가 True인 경우 출력된 결과임!')

print('hungry 값을 false로 변경 후')
hungry = False
if hungry:
    print("I'm hungry")
else:
    print('hungry 값이 False인 경우에 출력된 결과임!')
print('----------------------------------------------')
print('<<<for문 예시>>>')
print('[1, 2, 3을 for문을 돌면서 출력]')
for i in [1, 2, 3]:
    print(i)
print('----------------------------------------------')
print('<<<함수  예시>>>')
def hello():
    print("Hello World!")

print('함수 결과 출력')
hello()

def hello(object):
    print("Hello " + object + " !")

print('+연산으로 문자열을 붙인 함수 예시')
hello("cat")

