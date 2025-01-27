morse = {"a": ".-",
         "b": "-...",
         "c": "-.-.",
         "d": "-..",
         "e": ".",
         "f": "..-.",
         "g": "--.",
         "h": "....",
         "i": "..",
         "j": ".---",
         "k": "-.-",
         "l": ".-..",
         "m": "--",
         "n": "-.",
         "o": "---",
         "p": ".--.",
         "q": "--.-",
         "r": ".-.",
         "s": "...",
         "t": "-",
         "u": "..-",
         "v": "...-",
         "w": ".--",
         "x": "-..-",
         "y": "-.--",
         "z": "--.."}


def encode_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MorseCode:
            morse_code.append(MorseCode[char])
        elif char == ' ':
            morse_code.append(' ')
    return ' '.join(morse_code)


# Функция декодирования
def decode_from_morse(code):
    code = code.split(' ')  # Разделяем код по пробелам
    decoded_text = []
    for morse_char in code:
        for letter, morse in MorseCode.items():
            if morse_char == morse:
                decoded_text.append(letter)
                break
        else:
            decoded_text.append(' ')  # Добавляем пробел для разделения слов
    return ''.join(decoded_text)


# Основная функция
def main():
    while True:
        choice = input("Хотите закодировать (1) или раскодировать (2) текст? (введите 0 для выхода): ")
        if choice == '1':
            text = input("Введите текст для кодирования: ")
            print("Закодированный текст:", encode_to_morse(text))
        elif choice == '2':
            code = input("Введите код Морзе для декодирования: ")
            print("Декодированный текст:", decode_from_morse(code))
        elif choice == '0':
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
