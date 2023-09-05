import math

list = []
'''z = [(lambda x: math.sin(x))(i) for i in range(91)]
k = math.degrees(z)
print(k)'''

z = [(math.degrees(i)) for i in range(30)]
deg = [(math.sin(i)) for i in z]
print(deg)
