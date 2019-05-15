import random


d1 = 4
d2 = 12
d3 = 20
d4 = 28

cp1 = +3
cn1 = -3
cp2 = +9
cn2 = -9
cp3 = +13
cn3 = -13

pairings = [(d1, cp1), (d1, cn1), (d1, cp2), (d1, cn2), (d1, cp3), (d1, cn3), (d2, cp1), (d2, cn1),
          (d2, cp2), (d2, cn2), (d2, cp3), (d2, cn3), (d3, cp1), (d3, cn1), (d3, cp2), (d3, cn2),
          (d3, cp3), (d3, cn3), (d4, cp1), (d4, cn1), (d4, cp2), (d4, cn2), (d4, cp3), (d4, cn3)]


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']

choice = random.sample(list, 1)
print(choice)

if choice == a:
    d == d1
    c == cp1
    print('optionA')
if choice == b:
    d == d2
    c == cp1
    print('optionB')
if choice == c:
    d == d3
    c == cp1
    print('optionC')
if choice == d:
    d == d4
    c == cp1
    print('optionD')
if choice == e:
    d == d1
    c == cn1
    print('optionE')
if choice == f:
    d == d2
    c == cn1
    print('optionF')
if choice == g:
    d == d3
    c == cn1
    print('optionG')
if choice == h:
    d == d4
    c == cn1
    print('optionH')