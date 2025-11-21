# print("welcome to Day 8")
#
# def calculate_love_score(name1, name2):
#     # reset counters locally
#     _true = 0
#     _love = 0
#
#     merge_name = (name1 + name2).lower()
#
#     for char in merge_name:
#         if char in "true":
#             _true += 1
#         if char in "love":
#             _love += 1
#
#     return f"{_true}{_love}"
#
#
# print(calculate_love_score("Kanye West", "Kim Kardashian"))

letters = [chr(i) for i in range(97, 123)]
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift  = int(input("Type the shift number:\n"))

def caesar(message,shift_number,encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for alphabet in message:
        if alphabet not in letters:
            cipher_text += alphabet
        else:
            shifted_index = (letters.index(alphabet) + shift_number) % len(letters)
            shifted_text = letters[shifted_index]
            cipher_text += shifted_text


    print(f"Here is the {encode_or_decode} message:\n{cipher_text}")

caesar(message=text, shift_number=shift,encode_or_decode=direction)
