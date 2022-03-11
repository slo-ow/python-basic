class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # 맨 처음 상속 받은 class의 생성자를 호출함.
        Unit.__init__(self)
        Flyable.__init__(self)


dropship = FlyableUnit()


class Empty:
    pass  # 아무 기능이 없는 제어문, 주로 미구현 블럭에서 들여쓰기 문제를 해결하기 위하여 사용한다.
