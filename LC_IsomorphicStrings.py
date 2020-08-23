import challenge_header as CH


def isIsomorphic(s:str, t:str) -> bool:
    return False


if __name__ == "__main__":
    CH.printHeader("Isomorphic Strings")
    s = 'paper'
    t = 'title'
    result = isIsomorphic(s, t)
    print(f"\n{s} <--> {t}\nIsomorphic? {result}\n")
