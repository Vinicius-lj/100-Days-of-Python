alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
  if (shift/len(alphabet)) > 1:
    shift -= len(alphabet) * (shift//len(alphabet))
  encrypt_text = ""
  for letter in text:
    index = alphabet.index(letter)
    if direction == "encode":
      index += shift
      if index > (len(alphabet) - 1):
        index -= len(alphabet)
    else:
      index -= shift
      if index < 0:
        index += len(alphabet)
    encrypt_text += alphabet[index]
  print(encrypt_text)

ceaser(text, shift, direction)