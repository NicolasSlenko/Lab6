def encode(password):
    result = ""
    for i in password:
        i = int(i)
        if i <= 6:
            i += 3
            result += str(i)
        else:
            if i == 7:
                result += '0'
            elif i == 8:
                result += '1'
            elif i == 9:
                result += '2'
    return result

def decode(password):
    result = ""
    for i in password:
        i = int(i)
        if i <= 3:
            print("we tried")
    return result


def main():
    encoded = None
    while True:
        userInput = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ")
        if userInput == '1':
            userpassword = input("Please enter your password to encode: ")
            encoded = encode(userpassword)
            print("Your output has been encoded and stored!")
            print(encoded)
        elif userInput == '2':
            decoded = decode(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")
        elif userInput == '3':
            break


while __name__ == "__main__":
    main()


