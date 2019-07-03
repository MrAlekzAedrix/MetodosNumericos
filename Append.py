def AppendValue(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
            return lista
    except ValueError:
        print("You can't have duplicated values")
        return lista

list = [1, 2, 3, 4, 5, 6]
print("The full list is: ",AppendValue(list, 7))