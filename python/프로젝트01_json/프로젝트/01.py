
with open ('data/fruits.txt', 'r', encoding='utf=8') as f:
    text = f.read()
    names = text.split('\n')
print(len(names))
with open('01.txt', 'w', encoding='utf=8') as f:
    f.write(str((len(names))))