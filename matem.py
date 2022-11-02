b = [1,2,3,4,6,1,2,10,4,5,6]
a = (1,2,3,4,5,6,1,2,3,4,5,6)
b.reverse()
b.sort()
b.remove(10)
b.append(300)
b.insert(2,500)
# print(b)

# print(list.index(4))
# print(a)
# print(a[1])
# list[0] = 100
# a[0] = 100
# print(list)
# print(a)

# a = [1, 2, 3] 
# b = a*4

# c = a + b
# print(len(c))
# for x in c : print (x,end = ' ')




dict = {
    'yil': [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
    ], 
    'Age': 7, 
    'Class': "First"
}

# print(dict['Age'] , dict['Class'] )
# dict.clear()
# if  dict:
#     print(dict)




def Karra(list, karra = 3,qush = 10):
    a = []
    for i in list:
        a.append(i*karra + qush)
    return a

a = [1,2,3,4,5,6,7,8,9]
result = Karra(a,3,5)
print(a[666])
print(result)








