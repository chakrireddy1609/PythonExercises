def divi(arr1):

    lst = [0] * 6
    for i in range(len(arr1)):

        lst[arr1[i]] += 1

    return lst.index(max(lst))


print(divi([1,4,4,5,2,2,2,2,2,2,2,3,3,3,3,3,3]))







