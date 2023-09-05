import math

list = []
z = [(lambda x: math.sin(x))(i) for i in range(91)]
k = math.degrees(z)
print(k)

k=10
#конвертация с радиана в градусыпуе
z = [(math.degrees(i)) for i in range(30)]
deg = [(math.sin(i)) for i in z]
print(deg)
