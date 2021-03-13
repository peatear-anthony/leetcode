# 1309. Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        string_map = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10': 'j',
            '11': 'k',
            '12': 'l',
            '13': 'm',
            '14': 'n',
            '15': 'o',
            '16': 'p',
            '17': 'q',
            '18': 'r',
            '19': 's',
            '20': 't',
            '21': 'u',
            '22': 'v',
            '23': 'w',
            '24': 'x',
            '25': 'y',
            '26': 'z'
        }

        if '#' not in s:
            return "".join(string_map[x] for x in s)
        index = len(s) - 1
        result = []
        
        while index >= 0:
            if s[index] == "#":
                double_digit = s[index-2] +s [index-1]
                result.append(string_map[double_digit])
                index -= 3
            else:
                result.append(string_map[s[index]])
                index -= 1
                
        return "".join(x for x in result)[::-1]
            
            