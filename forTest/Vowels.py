def main():
    word = input("word: ")
    listOfVowels = occurringVowels(word)
    print(" ".join(listOfVowels))

def occurringVowels(word):
    word = word.upper()
    vowels = ('A','E','I','O','U')
    included = []
    for vowel in vowels:
        if (vowel in word) and (vowel not in included):
            included.append(vowel)
    return included


main()