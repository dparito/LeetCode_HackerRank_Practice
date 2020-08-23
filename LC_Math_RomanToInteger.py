if __name__ == "__main__":
    s = 'LVIII'     # Failing test case
    t = 'XIV'
    u = 'MCMXCIV'
    symbol_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_number = list(ss for ss in s)
    number_list = [symbol_map[i] for i in roman_number if i in symbol_map.keys()]
    
    i = 0
    new_list = []
    while i < len(number_list):
        if i < len(number_list)-1 and number_list[i] < number_list[i+1]:
            new_list.append(number_list[i+1] - number_list[i])
            i += 2
        else:
            new_list.append(number_list[i])
            i += 1
    
    total = 0
    for n in new_list:
        total += n
    print(total)
    