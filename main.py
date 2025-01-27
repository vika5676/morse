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

