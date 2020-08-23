from challenge_header import printHeader


class Solution:
    def __init__(self):
        pass

    
    def isValidPalindrome(self, s: str) -> bool:
        s_alpha_only = [i.lower() for i in s if i.isalnum()]
        salpha_len = len(s_alpha_only)
        for i in range(salpha_len):
            if s_alpha_only[i] != s_alpha_only[salpha_len -1 - i]:
                return False
        return True


if __name__ == "__main__":
    printHeader("Valid Palindrome")

    my_solution = Solution()

    # s = "A man, a plan, a canal: Panama"
    s = "0P"

    print(my_solution.isValidPalindrome(s))
