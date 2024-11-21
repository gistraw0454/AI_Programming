def main():
    fullName = input("enter a person's full name")
    print("first name:", firstName(fullName))


def firstName(fullName):
    firstSpace = fullName.index(' ')    # 공백 처음으로나온 index
    givenName = fullName[:firstSpace]   # 공백전까지 출력
    return givenName 
main()