# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if [sorted(i) for i in word.split()] == [sorted(h) for h in anagram.split()]:
        anagram_ = True
    else:
        anagram_ = False
    #anagram_ = word * anagram   
    return anagram_
    
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
