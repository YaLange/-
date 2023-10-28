from random import randrange
sourceConditions = ['0123456789','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz','!#$%&*+-=?@^_','il1Lo0O']
trueConditions = []
passValueipt = int(input("Введите количество паролей\n"))
lenPassipt = int(input("Введите длину одного пароля\n"))
digitipt = input("Включать ли цифры 0123456789?; да/нет\n")
if digitipt == 'да':
    trueConditions += sourceConditions[0]
xuppeript = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; да/нет\n")
if xuppeript == 'да':
    trueConditions += sourceConditions[1]
loweript = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; да/нет\n")
if loweript == 'да':
    trueConditions += sourceConditions[2]
symbolsipt = input("Включать ли символы !#$%&*+-=?@^_?; д/н\n")
if symbolsipt == 'да':
    trueConditions += sourceConditions[3]
simSimbolsipt = input("Исключать ли неоднозначные символы il1Lo0O?; да/нет\n")
if simSimbolsipt == 'да':
    trueConditions += sourceConditions[4]
trueConditions = ''.join(trueConditions)
passwords = []
chars = ''
for i in range(passValueipt):
    passwords.append(chars)
    chars = ''
    for j in range(lenPassipt):
        chars += trueConditions[randrange(len(trueConditions))]
print('Вот список сгенерированных паролей:', *passwords, sep='\n')