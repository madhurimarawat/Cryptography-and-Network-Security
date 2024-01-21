# Rail Fence Cipher

# This approach is a simple and straight forward approach for Rail Fence Cipher and it can also handle Whitespaces.

# Function for Rail Fence Cipher Encryption
def rail_Fence_Encrypt(input):

  c1,c2 = "", ""

  for i in range(len(input)):

    if i % 2 == 0:
      c1 += input[i]
    else:
      c2 += input[i]

  result = c1 + c2

  return result

# For Decrypting
def rail_Fence_Decrypt(ciphertext):

  result = ""

  # For Mid Point
  mid = len(ciphertext) // 2

  if len(ciphertext) % 2 == 0:

    for i in range(mid):

      # For Last Character
      if i == mid:
        result = result + ciphertext[i]

      else:
        result = result + ciphertext[i] + ciphertext[i + mid]

  else:

    for i in range(mid + 1):

      # For Last Character
      if i == mid:
        result = result + ciphertext[i]

      else:
        result = result + ciphertext[i] + ciphertext[i + mid + 1]

  return result

text = input("Enter Message: ")

# Printing Message
print("\nMessage is:", text)

# Giving Input text function will generate cipher text
cipher = rail_Fence_Encrypt(text)
print("\nCipher Text is:", cipher)

# Giving Cipher Text the Function wll generate the plaintext/decrypted Output
print("\nPlain Text is:", rail_Fence_Decrypt(cipher))