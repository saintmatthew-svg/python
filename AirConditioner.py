def TurnOn():
    return True

def TurnOff():
    return False

def Increase(Temperature):
    if(TurnOn() and Temperature < 30):
        Temperature = Temperature + 1
    return Temperature

def Decrease(Temperature):
    if (TurnOn() and Temperature > 16) :
        Temperature = Temperature - 1
    return Temperature