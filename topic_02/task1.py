def discriminant(a, b, c):
    d = b*b-4*a*c
    return d

def koreni(a,b,c):
    if a == 0:
        print("Error, a = 0")
        return None, None, None
    d = discriminant(a, b, c)
    if d < 0:
        print("Error: Diskriminant < 0")
        return d, None, None
    elif d == 0:
        x= -b/(2*a)
        return d,x,x
    else:
        x1= (-b + d**0.5)/(2*a)
        x2= (-b - d**0.5)/(2*a)
        return d,x1,x2


a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

d, x1, x2 = koreni(a, b, c)
if d is not None:
    print("Diskriminant: ", d)
if x1 is None:
    print("Nema koreniv")
elif x1 == x2:
    print("x = ", x1)
else:
    print("x1 = ", x1)
    print("x2 = ", x2)
