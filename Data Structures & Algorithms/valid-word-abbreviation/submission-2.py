class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        while i < len(word) and j < len(abbr):
            if abbr[j] in numbers:
                if abbr[j] == '0':
                    return False

                offset = "" 
                while j < len(abbr) and abbr[j] in numbers:
                    offset += abbr[j]
                    j += 1

                i += int(offset)
            
            elif word[i] != abbr[j]:
                return False
            else:
                i += 1
                j += 1

        if i != len(word) or j != len(abbr):
            return False

        return True
