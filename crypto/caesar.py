from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    some_text = list(text)
    new_text = []
    if some_text is new_text:
        return new_text
    else: #i in some_text:
        x = [rotate_character(i, rot) for i in some_text]
        x = ''.join(x)
        return x

def main():   
    text = input("What is your phrase?")
    rot = int(input("How many rotations?"))
    result = encrypt(text, rot)
    print(result)

if __name__ == "__main__":
    main()
