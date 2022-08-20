# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
length_AB = int(input())
length_BC = int(input())
print(round(math.degrees(math.atan(length_AB/length_BC))),chr(176),sep='')
