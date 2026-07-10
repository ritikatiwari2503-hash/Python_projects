#  Basics about Ceaser cypher:
#  Ceaser cypher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. 

# every character has its own order and character :
# e.g. "a" = 97, b = "98" , c = "99" and so on 
# then  ord("a") = 97, ord("b") = 98, ord("c") = 99 and so on
# whereas chr(97) = "a", chr(98) = "b", chr(99) = "c" and so on

# here is how we can create it :

# formula: (ord(char) - ord('a') + shift) % 26 + ord('a')

text = input("Enter message: ")
shift = int(input("Enter shift: "))
encrypted_text = ""

for ch in text:
    if ch.isalpha():  # (a-z or A-Z)
        if ch.islower():  # (a-z) only
            encrypted_text += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += chr((ord(ch) - ord('A') + shift) % 26 + ord('A')) 
    else:
        encrypted_text += ch


print("Encrypted_text:", encrypted_text)

# basically whatever shift we will enter for the e.g.(let's say shift is 2 then for text"abcd" it will skip first 2 alpha's and include next to alpha's in the text if if not in text as input() but in output we will get it )
# e.g. (abcde) with shift = 3 will be => (defgh) [first 3 removed and next 3 added]