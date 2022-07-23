cnt = 0
berry = []

with open('data/fruits.txt', 'r', encoding='utf=8') as f:
    text =f.read()
    fruitlist = text.split('\n')
    # print(fruitlist)해보면 각자 리스트 안에 담김
    for i in fruitlist:
        if i.endswith('berry'):
            # fruitlist에서 뒤에 베리만 남김
            berry.append(i)
            # []안에 fruitlist를 추가함.
            
            
berry = list(set(berry))
cnt = len(berry)


with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{cnt}\n')
    for i in berry:
        f.write(f'{i}\n')