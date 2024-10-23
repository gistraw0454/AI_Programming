#�� �߿��ҵ�
def main():
    listOfWords = formListOfWords("Gettysburg.txt")
    freq = createFrequencyDictionary(listOfWords)
    displayWordCount(listOfWords,freq)
    displayMostCommonWords(freq)

def formListOfWords(filename):
    infile = open(filename)
    originalLine = infile.readline().lower()
    line = ""
    for ch in originalLine: # ������ �� ���鼭 Ư������ �����ϸ� ���ڿ������
        if ('a'<=ch <='z') or (ch == " "):
            line += ch
    listOfWords = line.split()  # ���⸦ �������� list�����
    return listOfWords

def createFrequencyDictionary(listOfWords):
    freq = {}
    for word in listOfWords:
        freq[word] = 0  # �ش�ܾ key, value�� 0���� ����
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
            listOfMostCommonWords.append((word,freq[word])) # 6�� �̻� ���� word�� Ʃ�÷� ����
    listOfMostCommonWords.sort(key = lambda x: x[1],reverse=True)
    for item in listOfMostCommonWords:
        print(item[0],item[1])
    

main()