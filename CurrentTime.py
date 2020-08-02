# Program to show current time
import time
currentTime=time.time();
TotalSecond= int(currentTime);
currentSecond= int((TotalSecond%60));
TotalMinute= TotalSecond//60;
currentMinute= TotalMinute%60;
Totalhour= TotalMinute//60;
Currenthour=Totalhour%60;
print("Time",Currenthour,":",currentMinute,":",currentSecond);