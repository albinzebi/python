# a sentence given to a variable
sentence = "Right now I am writing a simple Python program"
print("Here is the original sentence:\n", sentence)


# a function that converts a sentence to a list of words
# and reverses this list
# i have used the split and reverse methods
def sentence_to_wordlist(s):
    wordlist = s.split()
    wordlist.reverse()
    print("Here is the reversed wordlist:\n", wordlist)


# calls function with the argument "sentence"
sentence_to_wordlist(sentence)
