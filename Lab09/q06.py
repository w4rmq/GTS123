def CelciusToFahrenheit(c):
    f = c * 9 / 5 + 32
    return f

c = float(input("Input temperature in degree Celcius: "))
f = CelciusToFahrenheit(c)
print(f"The degree in Farenheit is {f:.2f}")