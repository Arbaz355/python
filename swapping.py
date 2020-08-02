# Swapping two number taking console(user) input
a = input ("Enter the frist number:");
b = input ("Enter the second number:");
temp = a;
a=b;
b=temp;
print("After swapping the number are",a,b );
# swapping number without third variable
x=10;
y=20;
x,y=y,x;
print("Number after swapping are", x,y);