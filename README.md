# ProtectPRF

ProtectPRF is a simple command-line tool that enables users to encrypt PDF files with a specified password. It leverages the `PyPDF2` library to perform the encryption, providing an additional layer of security for your PDF documents.

## Features

- **Encrypt PDF Files**: Protect your PDF files by encrypting them with a secure password.
- **User-Friendly Interface**: The tool prompts you to enter the file path and the password, guiding you through the process.
- **File Existence Check**: Ensures that the file path provided by the user is valid before proceeding with encryption.

## Installation

1. Clone the repository `git clone https://github.com/Ceasari/ProtectPRF.git`
2. Install dependencies `pip install -r requirements.txt`.
3. Run the app `main.py`.
4. Follow the prompt to enter the path to your pdf file, and the script will extract the file and save it in the same directory as the original file with prefix 'protected'.

## Security Note

Please remember to keep your password secure and do not use this tool for any illegal activities.

## Contributing:

If you have any suggestions, bug reports, or just want to contribute to the project, feel free to file an issue or send a pull request!
 
## Author

[Ceasari](https://github.com/Ceasari)

## License

This project is licensed under the [MIT](LICENSE)
