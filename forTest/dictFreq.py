#좀 중요할듯
def main():
    listOfWords = formListOfWords("Gettysburg.txt")
    freq = createFrequencyDictionary(listOfWords)
    displayWordCount(listOfWords,freq)
    displayMostCommonWords(freq)

def formListOfWords(filename):
    infile = open(filename)
    originalLine = infile.readline().lower()
    line = ""
    for ch in originalLine: # 라인을 쭉 돌면서 특수문자 제거하며 문자열만들기
        if ('a'<=ch <='z') or (ch == " "):
            line += ch
    listOfWords = line.split()  # 띄어쓰기를 기준으로 list만들기
    return listOfWords

def createFrequencyDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] = 0  # 해당단어를 key, value를 0으로 설정
    for word in listOfWords:
        freq[word] += 1
    return freq

def displayWordCount(listOfWords, freq):
    print("word count: ",len(listOfWords))
    print("different word count : ",len(freq))
    print()

def displayMostCommonWords(freq):
    listOfMostCommonWords = []
    for word in freq.keys():
        if (freq[word]>=6):
            listOfMostCommonWords.append((word,freq[word])) # 6번 이상 나온 word만 튜플로 저장
    listOfMostCommonWords.sort(key = lambda x: x[1],reverse=True)
    for item in listOfMostCommonWords:
        print(item[0],item[1])
    

main()