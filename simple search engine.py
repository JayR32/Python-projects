text = input()
word = input()
def search(text, word):
    if word in text:
        print("word found")
    else:
        print("word not found")
search(text, word)