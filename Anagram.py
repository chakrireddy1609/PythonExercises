def Anagram(s1,s2):

    countS1 = {}
    countS2 = {}

    for i in range(len(s1)):
        countS1[s1[i]] = 1+countS1.get(s1[i],0)
        countS2[s2[i]] = 1+countS2.get(s2[i],0)

    for c in s1:
        if countS1[c] != countS2.get(c,0):
            return False

    return True

Anagram("aadriti","Anushaa")
