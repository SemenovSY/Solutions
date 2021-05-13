def addTwoNumbers(l1, l2):
    num_1 = ''
    num_2 = ''
    l3 = []
    for i in l1:
        num_1 += str(i)
    for i in l2:
        num_2 += str(i)
    num_3 = str(int(num_1[::-1]) + int(num_2[::-1]))
    for i in num_3:
        l3.append(int(i))
    return l3[::-1]

l1 = [1,2,3]
l2 = [1,9]
print(addTwoNumbers(l1, l2))
