"""Colors"""
color1 = input()
color2 = input()

momc=["Yellow","Red","Blue"]

if color1 in momc and color2 in momc:
    if color1 == color2:
        print(color1)
    elif color1 == "Red" and color2 == "Yellow" or color1 == "Yellow" and color2 == "Red":
        print("Orange")
    elif color1 == "Red" and color2 == "Blue" or color1 == "Blue" and color2 == "Red":
        print("Violet")
    elif color1 == "Yellow" and color2 == "Blue" or color1 == "Blue" and color2 == "Yellow":
        print("Green")
else:
    print("Error")
