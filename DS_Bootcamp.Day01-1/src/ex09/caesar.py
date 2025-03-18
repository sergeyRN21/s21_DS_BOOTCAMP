import sys

def caesar_cipher(text, shift, mode='encode'):
    if not all(ord(c) < 128 for c in text):
        raise Exception("Скрипт пока не поддерживает ваш язык")
    
    result = []
    for char in text:
        ascii_code = ord(char)
        if 65 <= ascii_code <= 90 or 97 <= ascii_code <= 122:
            new_ascii_code = ascii_code + (-shift if mode == 'decode' else shift)
            if new_ascii_code > 90 and ascii_code <= 90:
                new_ascii_code -= 26
            elif new_ascii_code < 65 and ascii_code <= 90:
                new_ascii_code += 26
            elif new_ascii_code > 122 and ascii_code >= 97:
                new_ascii_code -= 26
            elif new_ascii_code < 97 and ascii_code >= 97:
                new_ascii_code += 26
            result.append(chr(new_ascii_code))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("Неверное количество аргументов")
        
        mode = sys.argv[1].strip().lower()
        text = sys.argv[2].strip()
        shift = int(sys.argv[3])
        
        if mode not in ['encode', 'decode']:
            raise ValueError("Неизвестный режим работы")
        
        print(caesar_cipher(text, shift, mode))
    except ValueError as e:
        print(e)