from challenge_header import printHeader


class Solution:
    def smallestWord(self, strs) -> str:
        word = strs[0]
        min_len = len(word)
        for i in strs:
            if len(i) < min_len:
                word = i
                min_len = len(i)
        return word
    
    
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = self.smallestWord(strs)
        match = True
        while len(prefix) > 0:
            for i in strs:
                if prefix == i[:len(prefix)]:
                    match = True
                    continue
                else:
                    match = False
                    break
            if not match:
                prefix = prefix[:len(prefix)-1]
            else:
                break
            
        return prefix if match else ""


if __name__ == "__main__":
    printHeader("Longest Common Prefix")

    my_solution = Solution()

    s = ["flower","flow","flight"]
    # s = ["dog","racecar","car"]

    print(my_solution.longestCommonPrefix(s))
