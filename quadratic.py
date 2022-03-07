def solve_quadratic(a,b,c):
    from math import sqrt
    disc = b*b-4*a*c
    if disc >=0:
        x1 = (-b+sqrt(disc))/(2*a)
        x2 = (-b-sqrt(disc))/(2*a)
        print(x1, x2)
    else:
        print("None")