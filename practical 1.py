def trafficLight():
    msg = {0: "STOP, your life is precious",
           1: "Please WAIT, till the light turns Green",
           2:"GO! Thank you for being patient",
           -1:"Please enter a correct colour"}
    code = light(input(f"Enter a colour {colors}: ").upper())
    print(msg[code])
    print("SPEED THRILLS BUT KILLS!!")

def light(color):
    code = colors.index(color) if (color in colors) else -1
    return code
colors = ['RED',"YELLOW","GREEN"]
trafficLight()
