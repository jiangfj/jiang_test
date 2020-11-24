data_result=[]
def perm(data,begin,end):
    global data_result
    if begin == end:
        # print(data)
        data_result.append(list(tuple(data)))
        # print(data_result)
    else:
        j=begin
        for i in range(begin,end):
            data[i],data[j] = data[j],data[i]
            perm(data,begin+1,end)
            data[i], data[j] = data[j], data[i]

arr=[1,2,3,4]
perm(arr,0,len(arr))

print(data_result)
