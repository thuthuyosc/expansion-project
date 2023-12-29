import qrcode
import os

def to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', 
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--', 
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', 
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', 
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    return ' '.join(morse_code[i.upper()] for i in text)

def to_qr(text):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr_code.png')

def main():
    while True:
        try:
            with open('input.txt', 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print("File 'input.txt' does not exist. Please check again.")
            return
        try:
            text.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            print("The text in the file 'input.txt' is not a Unicode string. Please check again.")
            return
        else:
            while True:
                print("0: Exit")
                print("1: Convert file to QR")
                print("2: Convert file to Morse")
                choice = input("Enter your choice (0, 1, 2): ")
                if choice == '0':
                    return
                elif choice == '1':
                    to_qr(text)
                    print("The file has been converted to a QR code and saved as 'qr_code.png'.")
                elif choice == '2':
                    with open('output_morse.txt', 'w') as file:
                        file.write(to_morse(text))
                    print("The Morse code has been saved to the file 'output_morse.txt'.")
                else:
                    print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()
