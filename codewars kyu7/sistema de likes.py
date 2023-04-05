'''
Você provavelmente conhece o sistema de "curtir" do Facebook e outras páginas. As pessoas podem "curtir" postagens de blog, fotos ou outros itens. Queremos criar o texto que deve ser exibido ao lado de tal item.

Implemente a função que recebe um array contendo os nomes das pessoas que gostam de um item. Ele deve retornar o texto de exibição conforme os exemplos:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Nota: Para 4 ou mais nomes, o número "and 2 others"simplesmente aumenta.
'''

names = []

def likes(names):
    # your code here
    initial = 0
    quantity = int(input('Digite a quantidade de nomes que deseja cadastrar: '))
    
    while initial < quantity:
        name = str(input('Digite um nome: '))
        names.append(name)
        initial +=1
    return names

print(likes(names))
    
if len(names) == 0: 
    print('no one likes this')
elif len(names) == 1:
    print(f'{names[0]} like this')
elif len(names) == 2:
    print(f'{names[0]} and {names[1]} like this')
elif len(names) == 3:
    print(f'{names[0]}, {names[1]} and {names[2]} like this')
elif len(names) >= 4:
    others = len(names) - 2
    print(f'{names[0]}, {names[1]} and {others} others like this')


