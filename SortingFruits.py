def sortingFruits(array):
    dct = {}

    for fruit in array:
        if fruit not in dct.keys():
            dct[fruit] = 0
        dct[fruit] += 1
    #dct = {'banana' : 3, 'grapefruit' : 2, 'orange'  :1}
    list_fruits = list(dct.items())
    list_fruits.sort(key = lambda i: -i[1])

    return list(i[0] for i in list_fruits)
    
fruits = ['banana', 'grapefruit', 'orange', 'banana', 'banana', 'grapefruit', 'orange', 'orange', 'orange']

print(sortingFruits(fruits))
