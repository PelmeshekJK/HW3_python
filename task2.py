def morse_tue_binary(n):
    binary_str = bin(n-1)[2:]
    morse_str = ''
    for b in binary_str:
        if b == '0':
            morse_str += '.'
        else:
            morse_str += '-'
    return morse_str

n = int(input("Введите число: "))
morse_str = morse_tue(len(morse_tue_binary(n)))
print(morse_str[:n])