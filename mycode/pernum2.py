"""
全排列
"""

def perm(array):
    list_temp=[]
    num=array.pop(0)
    list_temp.append(num)

    if len(array)==2:
        newlist=[[array[0],array[1]],
                 [array[1], array[0]]]
    else:
        newlist=perm(array)
    while list_temp:
        num = list_temp.pop()
        newlist1=[]
        for item in newlist:
            newlist1 +=subperm(item,num)
        newlist=list(tuple(newlist1))
    return newlist

def subperm(list1,num):
    list_result = []
    for i in range(len(list1)):
        tuple1 = tuple(list1)
        list12 = list(tuple1)
        list12.insert(i, num)
        list_result.append(list12)
    tuple1 = tuple(list1)
    list12 = list(tuple1)
    list12.append(num)
    list_result.append(list12)
    return list_result

array=[1,2,3,4]
print(perm(array))







