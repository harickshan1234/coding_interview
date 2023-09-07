# two string check is the anagram if the same characters
from collections import Counter
def are_angrams(s1,s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
    freq1 = {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1 +=1
        else:
            freq1 = 1
    for ch in s2:
        if ch in freq2:
            freq2 += 1
        else:
            freq2 = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


