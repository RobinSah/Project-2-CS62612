import matplotlib.pyplot as plt
import math

a = [100,200,300,400,500,600,700,800,900,1000,1100] #values of n from 100 to 1000

y = [0.0002790999995643506, 0.00029970000004017493, 0.0003290000053780386,
0.00033999999991978984, 0.0003435000004785252, 0.0003599000003028894,
0.00036566999993289937, 0.000385099999627273, 0.000387699999465549,
0.0003999455999901047, 0.000409999999914624]
"""y represents the total elapsed time of the program when n 
was substituted from 100 to 1000."""

x = [(math.log2(x)) for x in a]          #Theoretical values by putting n in log2(n)
n = [j/(24*(10**3)) for j in x]          #Adjusted theoretial values

plt.plot(a,y)
plt.plot(a,n)