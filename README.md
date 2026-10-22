# CipherSafe – Basic Encryption and Decryption

## Project Overview
CipherSafe is a beginner-friendly cybersecurity project that demonstrates basic encryption and decryption using the Caesar Cipher algorithm. It allows users to enter a text message, choose a shift key, encrypt the message, and decrypt ciphertext to recover the original message.

## Objectives
- Understand the basic concepts of encryption and decryption.
- Implement the Caesar Cipher algorithm using Python.
- Develop a simple web interface using HTML and CSS.
- Connect the frontend with Python using Flask.
- Demonstrate how a reversible cipher works.

## Technologies Used
- Python
- Flask
- HTML5
- CSS3
- Visual Studio Code

## Features
- Encrypt text using a user-selected shift key.
- Decrypt ciphertext using the same shift key.
- Display encrypted and decrypted results.
- Preserve letter case, spaces, numbers, and punctuation.
- Validate the shift key and empty input.
- Provide a simple, responsive user interface.

## Algorithm
1. Accept a message and a shift key from the user.
2. For encryption, shift each alphabetic character forward by the specified number of positions.
3. Wrap around to the beginning of the alphabet when necessary.
4. Preserve spaces, numbers, punctuation, and letter case.
5. For decryption, reverse the shift using the same key.
6. Display the results on the webpage.

## Project Structure
```text
CyberSecurity-Encryption-Project/
├── app.py
├── cipher.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation and Execution

### Prerequisites
Install Python and Visual Studio Code.

### Steps
1. Open the project folder in VS Code.
2. Open the terminal in the project directory.
3. Install the required dependency:

   `python -m pip install -r requirements.txt`

4. Start the application:

   `python app.py`

5. Open `http://127.0.0.1:5000` in a web browser.

## Sample Input and Output

**Input message:** `HELLO WORLD`

**Shift key:** `3`

**Encrypted message:** `KHOOR ZRUOG`

**Decrypted message:** `HELLO WORLD`

## Conclusion
The CipherSafe project demonstrates the basic working principle of encryption and decryption through the Caesar Cipher. It combines Python-based cryptographic logic with a Flask web application and a simple HTML/CSS interface. This project provides a foundation for learning about cryptography and data confidentiality.

## Security Note
The Caesar Cipher is intended for educational purposes only. It is not suitable for protecting real confidential information.
