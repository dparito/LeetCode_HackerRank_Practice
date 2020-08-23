class Solution:
    def isValid(self, s: str) -> bool:
        para_dict = {'(':')', '{':'}', '[':']'}
        para_stack = []
        validity = True
        for para in s:
            if para in para_dict.keys():
                para_stack.append(para)
            elif para in para_dict.values():
                opening_para = None
                for key in para_dict:
                    if para_dict[key] == para:
                        opening_para = key
                        break
                if opening_para is None:
                    validity = False
                    break
                else:
                    if opening_para in para_stack:
                        para_stack.pop()
                    else:
                        validity = False
                        break
        if len(para_stack) > 0:
            validity = False
        return validity


if __name__ == "__main__":
    sol = Solution()
    para_validitiy = sol.isValid('[]')
    print(para_validitiy)