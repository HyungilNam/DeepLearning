print('시그모이드 함수 구현하기')

import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

print('넘파이 배열도 가능한 브로드캐스트 예제')
t = np.array([1.0, 2.0, 3.0])
print('넘파이 배열 더하기')
print(1.0 + t)
print('넘파이 배열 나누기')
print(1.0/t)

print('시그모이드 함수 그래프로 그리기')
import matplotlib.pylab as plt

p = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(p)
plt.plot(p, y)
plt.ylim(-0.1, 1.1)				#y축 범위 지정
plt.show()
