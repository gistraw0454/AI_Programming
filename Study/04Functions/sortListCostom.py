def main():
    list1 = ["demo","segu","equal","brrr","break","two"]
    list1.sort(key=len) # 길이순으로 ascending sort
    print(list1)

    list1.sort(key = numberOfVowels,reverse = True) # 모음 개수순으로 descending
    print(list1)

def numberOfVowels(word):
    vowels = ['a','e','u','i','o']
    total =0
    for vowel in vowels:
        total += word.count(vowel)
    
    return total

main()