# Cryptography-and-Network-Security
This repository contains Cryptography programs in the Python programming language.

## Cryptography:

- **Definition:**
  - Cryptography is the practice and study of techniques for securing communication and information from adversaries.

- **Objectives:**
  - Ensure confidentiality, integrity, and authenticity of information.
  - Provide secure communication in the presence of malicious third parties.

- **Types of Cryptography:**
  - Symmetric Key Cryptography (uses a single key for both encryption and decryption).
  - Asymmetric Key Cryptography (uses a pair of public and private keys).

- **Applications:**
  - Used in securing online transactions (e.g., HTTPS).
  - Protects sensitive data in storage and transmission.

- **Challenges:**
  - Continuous need for stronger algorithms due to advancements in computing power.
  - Balancing security and usability in real-world applications.

### Caesar Cipher:

- **Algorithm:**
  - Substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

- **Key Concept:**
  - Key represents the number of positions each letter of the alphabet is shifted.

- **Weakness:**
  - Vulnerable to brute-force attacks due to a limited number of possible keys (26 in the case of the English alphabet).

- **Encryption Example:**
  - Plain text: "HELLO"
  - Key: 3
  - Cipher text: "KHOOR"

- **History:**
  - Named after Julius Caesar, who is believed to have used it for military communication.

### Rail Fence Cipher:

- **Algorithm:**
  - Transposition cipher where the plaintext is written in a zigzag pattern on a set of rails.

- **Key Concept:**
  - Key represents the number of rails (rows) used in the encryption process.

- **Encryption Example:**
  - Plain text: "HELLO"
  - Key: 3
  - Cipher text: "HOLELW"

- **Decryption:**
  - Reconstruct the zigzag pattern and read off the message.

- **Usage:**
  - Historical use in non-secure communication due to its simplicity.
  - Rarely used for serious encryption today, more of a puzzle or educational tool.
