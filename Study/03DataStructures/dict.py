addr = {
    'a':'aaaa',
    'b':'bbbb',
    'c':'cccc'
}

print(addr['a'])

# key-value pair 삭제
del addr['a']
print(len(addr))

for name,address in list(addr.items()): # 튜플을 리턴하고 그걸 list화 시킨다.
    print(name,address)

# key-value 추가
addr['b'] = 'cdcddc'
if 'b' in addr:
    print(addr['b'])