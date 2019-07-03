def Udc():
    colores = {"rojo": "red", "verde":"green", "negro":"black"}
    try:
        print(colores["blanco"])
    except KeyError:
        print("The color 'white' doesn't exist in this list")



Udc()