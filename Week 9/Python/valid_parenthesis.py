class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        st = []
        for p in s:
            if p in pairs.keys():
                st.append(p)
            elif len(st) > 0 and pairs[st[-1]] == p:
                st.pop()
            else:
                return False
        return len(st) == 0