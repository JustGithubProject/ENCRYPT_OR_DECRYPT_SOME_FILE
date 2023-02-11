import os

import pyAesCrypt

FILE_FOR_ENCRYPT = "password.txt"  # Here must be your file
FILE_FOR_DECRYPT = "password.aes"  # Here must be your file


def encrypt():
    password = input("Enter password for encryption: ")
    pyAesCrypt.encryptFile(FILE_FOR_ENCRYPT, FILE_FOR_DECRYPT, password)


def decrypt():
    password = input("Enter a password for the file: ")
    pyAesCrypt.decryptFile(FILE_FOR_DECRYPT, FILE_FOR_ENCRYPT, password)


def main():
    command = input("Enter - 1 to encrypt the file; Enter - 2 to decrypt the file: ")
    if command == "1":
        encrypt()
        os.remove(
            r"D:\Users\Kropi\PycharmProjects\encryptDecrypt\{0}".format(FILE_FOR_ENCRYPT))  # Here must be your path
    elif command == "2":
        decrypt()
        os.remove(
            r"D:\Users\Kropi\PycharmProjects\encryptDecrypt\{0}".format(FILE_FOR_DECRYPT))  # Here must be your path
    else:
        raise ValueError("You need to select 1 or 2")


if __name__ == "__main__":
    main()
