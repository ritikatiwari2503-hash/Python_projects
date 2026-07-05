word1 = input("enter first word:")
word2 = input("enter second word:")

# check if the words are anagrams
if sorted(word1) == sorted(word2): # means they do have same length and also same characters
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")
