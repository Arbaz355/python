# Program for quadric equation
import cmath;
a = 1;
b= 2; 
c= 1;
d= 4*a*c;
sol1 = ((-b+cmath.sqrt(d))/(2*a));
sol2 = (((-b-cmath.sqrt(d))/(2*a)));
print("Solution are {0} and {1}".format(sol1,sol2));