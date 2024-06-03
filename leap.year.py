year=int(input("Enter an Year"))
if year%400==0:
    print("%d is Leap year and Century year"%year)
elif year%100==0:
    print("%d is not Leap year but Century year"%year)
elif year%4==0:
    print("%d is Leap year but not Century year"%year)
else :
    print("%d is not Leap year nor Century year"%year)