def btwnsets(arr1, arr2):
    num = 0
    while arr1[-1] <= num < arr2[0]:
        for i in arr1:
            for j in arr2:
                if num%i==0 and j%num ==0:
                    break
                    return num
                else:
                    continue
                num += 1





print(btwnsets([2,6],[24,36]))
