time=float(input("input time in minutes:"))
day=time//(24*3600)
time=time(24*3600)
hour=time//3600
minutes=time//60
time%=3600
minutes=time//60
time%=60
second=time
print("d:h:m:s:",%d%d%d%d(day,hours,minutes,seconds))
