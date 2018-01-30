#perceptron practice1

#AND 게이트

print('AND 게이트 예제 결과 출력')
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(AND(0, 0))	#0 출력
print(AND(1, 0))	#0 출력
print(AND(0, 1))	#0 출력
print(AND(1, 1))	#1 출력
print('\n')


print('가중치와 편향 도입 예제 출력')
import numpy as np
x = np.array([0, 1])		#입력
w = np.array([0.5, 0.5])	#가중치
b = -0.7			#편향
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b)
print('\n')

print('가중치와 편향을 도입한 AND 게이트 예제 결과 출력')
def AND2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND2(0, 0))
print(AND2(1, 0))
print(AND2(0, 1))
print(AND2(1, 1))
print('\n')

print('NAND 게이트와 OR 게이트 예제 결과 출력')
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])		#AND와 가중치(w와 b)만 다르다!!!
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(NAND(0, 0))
print(NAND(1, 0))
print(NAND(0, 1))
print(NAND(1, 1))
print('\n')

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])          #AND와 가중치(w와 b)만 다르다!!!
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(OR(0, 0))
print(OR(1, 0))
print(OR(0, 1))
print(OR(1, 1))
print('\n')


print('기존의 게이트들을 조합하여 XOR 게이트 만들기!')
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND2(s1, s2)
    return y

print(XOR(0, 0))  #0 출력
print(XOR(1, 0))  #0 출력
print(XOR(0, 1))  #0 출력
print(XOR(1, 1))  #0 출력
print('\n')

