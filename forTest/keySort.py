def main():
    list1 = ["demoada","ghaskd",'asnklgnasklfg',"asoopwe"]
    list1.sort(key=len, reverse=True)
    print(list1)
    list1.sort(key = numberOfVowels,reverse=True)


def numberOfVowels(word):
    vowels = ('a','e','u','i','o')
    total =0
    for vowel in vowels:
        total += word.count(vowel)
    return total


main()