# Simple Password Manager

This is a simple password manager that allows you to store and view encrypted passwords.

## Features

- **Encryption**: Passwords are encrypted using the Fernet symmetric encryption algorithm.
- **Adding Passwords**: You can add new account passwords.
- **Viewing Passwords**: You can view existing passwords.

## How to Use

1. **Generate Key**:
   - Before using the password manager, you need to generate a key. This key is used for encryption and decryption of passwords.
   - Run the `generate_key()` function to generate a key.

2. **Write Key to File**:
   - The generated key should be written to a file for later use.
   - Run the `write_key(key)` function to write the key to a file named `key.key`.

3. **Load Key**:
   - When using the password manager, the key needs to be loaded from the file.
   - Run the `load_key()` function to load the key from the file.

4. **Main Menu**:
   - Run the `main()` function to start the password manager.
   - You'll be prompted to choose between viewing existing passwords or adding new ones.
   - Enter `view` to view passwords or `add` to add a new password.

## Requirements

- Python 3.x
- `cryptography` library (`pip install cryptography`)

## How to Run

1. Clone this repository or download the `password_manager.py` file.
2. Install the `cryptography` library if you haven't already:
   ```
   pip install cryptography
   ```
3. Run the Python script:
   ```
   python password_manager.py
   ```

## Sample Usage

```
Would you like to add a new password or view existing ones (view, add), press q to quit? add
Account Name: example@gmail.com
Password: mypassword
Would you like to add a new password or view existing ones (view, add), press q to quit? view
User: example@gmail.com | Password: mypassword
Would you like to add a new password or view existing ones (view, add), press q to quit? q
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).