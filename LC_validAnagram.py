import challenge_header as CH
from collections import defaultdict 


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_char_count_dict = {char:s.count(char) for char in s}
    t_char_count_dict = {char:t.count(char) for char in t}

    return s_char_count_dict == t_char_count_dict


def main():
    CH.printHeader("Valid Anagram")
    
    print ("s = ", end="")
    s = input()
    print ("t = ", end="")
    t = input()
    print (isAnagram(s, t))


if __name__ == "__main__":
    main()
