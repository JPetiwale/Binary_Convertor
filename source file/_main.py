print("What do you want to do ?")
print("1. Convert Binary to Character")
print("2. Convert Character to Binary")
option=input("Please select your option: ")

if option not in ("1","2"):
    print("Invalid Option")
else:
    if option=="1":
        import binary_to_character
    elif option=="2":
        import character_to_binary