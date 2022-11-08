def minMax(arr1):
    min = max = arr1[0]
    max_count = min_count = 0
    for num in arr1:
        if min < num:
            min = num
            min_count += 1
        elif max > num:
            max = num
            max_count += 1

    return min_count, max_count

print(minMax([10,5,20,20,4,5,2,25,1]))
