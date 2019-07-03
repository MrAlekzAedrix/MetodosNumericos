def ListError():

    list = [1, 2, 3, 4, 5]

    try:
        list[10]
    except IndexError:
        print("There's no ninth position")


ListError()