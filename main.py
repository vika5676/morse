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


def encode_to_morse(text):
    encoded_messange = []
    for i in text.upper():
        if i in morse:
            encoded_messange.append(morse[i])
        else:
            encoded_messange.append('?')


# Основная функция
def main():
    while True:
        choice = input("Хотите закодировать (1) или раскодировать (2) текст?")
        if choice == '1':
            text = input("Введите текст для кодирования: ")
            print("Закодированный текст:", encode_to_morse(text))
        elif choice == '2':
            code = input("Введите код Морзе для декодирования: ")
            print("Декодированный текст:", decode_from_morse(code))
        else:
            print("Неверный выбор, попробуйте снова.")
