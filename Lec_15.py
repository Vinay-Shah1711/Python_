import time
timeStamp=time.strftime('%H %M %S')

hour=int(time.strftime('%H'))
minutes=time.strftime('%M')
second=time.strftime('%S')

print("Current time")
print("Hour",hour)
print("Minutes",minutes)
print("Second",second)

if(0<=hour<=12):
    print("GOOD MORNING")
elif(12<=hour<=16):
    print("GOOD AFTERNOON")
elif(16<=hour<=19):
    print("GOOD EVENING")
elif(19<=hour<=24):
    print("GOOD NIGHT")
else:
    print("Valid Input give")