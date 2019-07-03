def Division():
    n1=int(input("Please enter a number: "))
    n2=int(input("Please enter another number: "))
    try:
        div=n1/n2
        return div
    except ZeroDivisionError:
        print("You can't divide by 0")
    except TypeError:
        print("You can't divide a letter or a number by the opposite one")



Division()