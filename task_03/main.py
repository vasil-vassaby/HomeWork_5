# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

import view as vw


def main():
    encrypted_data = vw.encrypter(input('Введи строку, которую надо сжать >: '))
    print('Строка после сжатия:', encrypted_data)
    decrypted_data = vw.decrypter(encrypted_data)
    print('Строка после разжатия:', decrypted_data)


if __name__ == '__main__':
    main()
