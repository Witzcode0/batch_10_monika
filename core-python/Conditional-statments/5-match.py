# [mon - 0 tue - 1,....sun - 6 ]
# day = 5
import datetime

day = datetime.datetime.now().weekday()

match (day):
    case 0:
        print("Today is Mon")
    case 1:
        print("Today is The")
    case 2:
        print("Today is Wed")
    case 3:
        print("Today is Thu")
    case 4:
        print("Today is Fri")
    case 5:
        print("Today is Sat")
    case 6:
        print("Today is Sun")
    case _:
        print("Invalid day")