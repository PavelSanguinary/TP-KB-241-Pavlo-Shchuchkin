def discriminant(a, b, c):
    d = b*b-4*a*c
    if d < 0:
        print("Error: Diskriminant < 0")
        return d, None, None
    x1= (-b+ d**0.5)/(2*a)
    x2= (-b - d**0.5)/(2*a)
    return d,x1,x2

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

d, x1, x2 = discriminant(a, b, c)

print("Diskriminant: ", d)
print("x1 = ", x1)
print("x2 = ", x2)
