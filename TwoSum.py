def twoSum(arr,k):

    prevNum = {}

    for idx,num in enumerate(arr):
        diff = k - num
        if diff in prevNum:
            return [prevNum[diff],idx]
        else:
            prevNum[num] = idx


print(twoSum([1,2,3,4],7))