# import travel.thailand
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()


# import 공개 범위 설정해야함 => __init__
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
