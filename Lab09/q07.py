def TriArea(h, b):
    area = 0.5 * h * b
    return area

h = int(input("Enter the height (h): "))
b = int(input("Enter the base (b): "))
area = TriArea(h, b)
print(f"The area of the triangle is {area:.1f}")