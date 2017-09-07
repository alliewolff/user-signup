from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_text = []    
    start = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in text:
        key_rotate = alphabet_position(key[start])
        if not char in alphabet:            
            new_text.append(char)
            continue
        elif char.isalpha():
            new_text.append(rotate_character(char, key_rotate)) 
        if start == (len(key) - 1): 
            start = 0
        else: 
            start += 1

    return ''.join(new_text)    

def main():   
    text = input("What is your phrase?")
    key = input("What is your key?")
    print(encrypt(text, key))

if __name__ == "__main__":
    main()
      