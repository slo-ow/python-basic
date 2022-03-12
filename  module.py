# from module import theater_module
# theater_module.price(3)  # 3명이서 영화 보러 갔을때 가격
# theater_module.price_morinig(4)  # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5)  # 5명의 군인이 영화 보러 갔을 때

# from module import theater_module as mv
# mv.price(3)
# mv.price_morinig(4)
# mv.price_soldier(5)


# 별도의 변수명 없이 전체 함수를 전부다 가져다 씀
# from module.theater_module import *
# price(5)
# price_morinig(2)
# price_soldier(3)


# # 필요한 함수만 정의해서 가져다가 사용할 수 있음.
# from module.theater_module import price,price_morinig


# 함수명을 재정의 하여 사용할 수 있음.
from module.theater_module import price_soldier as prise
prise(5)