def permutation():

    s1 = "The cows are jumping over the moon"
    s2 = "The moon are jumping          over the cows"

    lower_s1 = s1.lower().replace(" ","")
    lower_s2 = s2.lower().replace(" ","")
    return sorted(lower_s1) == sorted(lower_s2)


print(permutation())

