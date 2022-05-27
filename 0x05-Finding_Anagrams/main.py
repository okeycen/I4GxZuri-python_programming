# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    new_word= word.strip().lower()
    new_anagram= anagram.strip().lower()

    if len(new_word)==len(new_anagram):
        
        sorted_word = sorted(new_word)
        sorted_anagram = sorted(new_anagram)

        if  sorted_word== sorted_anagram:
            return True
        else:
            return False

    else:
        return False

print(find_anagrams("below", "elbow"))
print(find_anagrams("hello", "check"))