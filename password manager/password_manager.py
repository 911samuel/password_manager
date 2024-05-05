from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()


def write_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found.")
        print("Generating new key...")
        key = generate_key()
        write_key(key)
        return key


def view_passwords(fernet):
    try:
        with open('passwords.txt', 'r') as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 2:
                    user, passw = data
                    print("User:", user, "| Password:", fernet.decrypt(passw.encode()).decode())
                else:
                    print("Malformed entry:", line.strip())
    except FileNotFoundError:
        print("Password file not found.")


def add_password(fernet):
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fernet.encrypt(pwd.encode()).decode() + "\n")


def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break

        if mode == "view":
            view_passwords(fernet)
        elif mode == "add":
            add_password(fernet)
        else:
            print("Invalid mode.")
            continue


if __name__ == "__main__":
    main()
