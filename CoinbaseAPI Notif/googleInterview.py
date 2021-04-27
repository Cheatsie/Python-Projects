import math
intlist = []
x = "True"

def nextsquare(material):
    tempmaterial = float(material)
    panelsize = int(math.sqrt(tempmaterial))
    return panelsize

material = input("Enter value:")

while x == "True":
    panelsize = nextsquare(material)
    intlist.append(int(panelsize * panelsize))
    material = int(material) - int(panelsize * panelsize)
    if material < 1:
        x = "False"
        break

print(intlist)