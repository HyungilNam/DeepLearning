print('matplotlib 예시')

#pyplot의모듈 및 추가 기능
print('sin함수와 cos함수 예시로 pyplot의 기능 알아보기')
import numpy as np
import matplotlib.pyplot as plt

	#데이터 준비
x = np.arange(0, 6, 0.1)	#0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

	#그래프 그리기
plt.plot(x, y1, label = 'sin')
plt.plot(x, y2, linestyle="--", label="cos")	#cos 함수는 점선으로 그리기
plt.xlabel("x")					#x축 이름	
plt.ylabel("y")					#y축 이름
plt.title('sin & cos')				#제목
plt.legend()
plt.show()

print('pop-up창 실행 후 종료 \n')


#이미지 표시하기
print('pyplot을 이용한 이미지 표시예제')

#import matplotlib.pyplot as plt			#위에서 선언했으므로 
from matplotlib.image import imread

img = imread('/Users/namhyeongil/anaconda3/pkgs/libxml2-2.9.4-hbd0960b_5/share/doc/libxml2-2.9.4/html/tutorial/images/callouts/1.png') 		#이미지 읽어오기('경로확인!')

plt.imshow(img)
plt.show()

print('pop-up창 실행 후 종료 \n')
