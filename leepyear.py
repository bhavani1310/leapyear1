year=int(input())
if year%400==0:
    print("its a leap year")
elif year%100==0:
    print("its not a leap year")
elif year%4==0:
    print("its leap year")
else:
    print("its not a leap year")