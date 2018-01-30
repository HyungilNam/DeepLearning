
print('클래스 생성')
class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + " !")

    def goodbye(self):
        print("Good-bye " + self.name + " !")


print('클래스 테스트')
m = Man('남현길')
m.hello()
m.goodbye()
