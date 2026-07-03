import time                           #import time

text = "The quick brown fox jumps over the lazy dog."

print("Type the following text as fast as you can:")

print(text)

start_time = time.time()              #timer start
user_input = input()                  #input the text from user
end_time = time.time()                #timer end

time_taken = end_time - start_time    #calculate time taken

words = len(user_input.split())       #counts the number of words in the user input
wpm = words / (time_taken / 60)       #calculates words per minute


print("time taken: {:.2f} seconds".format(time_taken)) #time taken in seconds
print("words per minute: {:.2f}".format(wpm))          #words per minute
