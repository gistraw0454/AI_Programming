def main():
    listOfWords = formListOfWords("./file/Gettysburg.txt")
    freq = createFreqDictionary(listOfWords)
    disaplayWordCount(listOfWords,freq)
    displayMostCommonWords(freq)

def formListOfWords(fileName):
    infile = open(fileName)
    originalLine = infile.readline().lower()    # 한줄읽고 소문자로 바꿔서 저장
    line = ""

    for ch in originalLine:
        if ('a'<=ch<='z') or (ch == " "):   # 문자로만된 문장인지 확인
            line += ch

    listOfWords = line.split()  # 띄어쓰기 기준으로 나눠 list만들기
    return listOfWords

def createFreqDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] =0   # 전부 0으로 만들어줌
    for word in listOfWords:    # 개수 세기
        freq[word] = freq[word] +1
    return freq

def disaplayWordCount(listOfWords,freq):
    print(len(listOfWords),len(freq))

def displayMostCommonWords(freq):
    # 6번 이상 나온 word 출력
    listOfMostCommonWords = []  # 6번 넘게나온거 list에 넣고 출력
    for word in freq.keys():
        if freq[word] >= 6:
            listOfMostCommonWords.append((word,freq[word]))
    
    listOfMostCommonWords.sort(key=lambda x:x[1], reverse=True)

    for item in listOfMostCommonWords:
        print(item[0],item[1])

main()
