def main():
    word = "Airplane"
    listOfVowels = occurringVowels(word)
    print("The following vowels occur in the word:, end=''")
    stringOfVowels = " ".join(listOfVowels)
    print(stringOfVowels)

def occurringVowels(word):
    word = word.upper()
    vowels = ('A','E','U','I','O') # tuple
    includedVowels = []
    for vowel in vowels:
        if (vowel in word) and (vowel not in includedVowels):
            includedVowels.append(vowel)
    return includedVowels

main()