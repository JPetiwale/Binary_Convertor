import endecrypt

def start():
    print("What do you want to do ?")
    print("1. Convert Binary to Character")
    print("2. Convert Character to Binary")
    option=input("Please select your option: ")

    if option not in ("1","2","back"):
        print("Invalid Option")
        start()
    else:
        if option=="1":
            x=input("Enter binary you want to convert: ")
            print("character conversion is :")
            endecrypt.decode(x,'binary')

        elif option=="2":
            x=input("Enter character you want to convert: ")
            print("Binary conversion is :")
            endecrypt.encode(x,'binary')

        elif option=="back":
            start()

start()
#end