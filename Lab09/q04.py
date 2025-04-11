def UserInput():
    ww = float(input("Input your weight (kilogram): "))
    hh = float(input("Input your height (meter): "))
    return hh, ww

def FindBMI(hh, ww):
    UserBMI = ww / (hh * hh)
    return UserBMI

def ShowBMI(MyBMI):
    print(f"The user BMI is {MyBMI:.2f}")


hh, ww = UserInput()
UserBMI = FindBMI(hh, ww)
ShowBMI(UserBMI)