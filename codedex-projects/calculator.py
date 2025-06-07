print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = int(input('Which shape:'))
if shape == 1:
    base = int(input('base:'))
    height = int(input('height:'))
    area = (base * height)/2
    print("the area is", area)
elif shape == 2:
    length = int(input('length:'))
    width = int(input('width:'))
    area = (length * width)
    print("the area is", area)
elif shape == 3:
    side = int(input('side:'))
    area = side**2
    print("the area is", area)
elif shape == 4:
    radius = int(input('radius:'))
    area = 3.14 * radius**2
    print("the area is", area)
else:
    print("No shape selected.")
