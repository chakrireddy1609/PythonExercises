def candles(arr):
    max_height = max(arr)
    count = 0
    for i in arr:
        if i == max_height:
            count+=1
    return count

print(candles([4,5,6,7,7,7]))