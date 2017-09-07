def alphabet_position(letter):
    """Find the position of a letter in the alphabet"""
    letter = (str(letter))
    letter = letter.lower()
    return ord(letter) - 97

def rotate_character(char, rot):
    if char.isupper():
        char = ord(char)
        new_pos = char + rot
        if new_pos <= 90:
            return chr(new_pos)
        if new_pos > 90:
            new_num = (new_pos - 65) % 26 + 65
        return chr(new_num)

    elif char.islower():
        char = ord(char)
        new_pos = char + rot
        if new_pos <= 122:
            return chr(new_pos)
        if new_pos > 122: 
            new_num = (new_pos - 97) % 26 + 97
            return chr(new_num)
    else:
        return char

def main():   
    char = input("What is your phrase?")
    rot = int(input("How many rotations?"))
    result = rotate_character(char, rot)
    print(result)

if __name__ == "__main__":
    main()