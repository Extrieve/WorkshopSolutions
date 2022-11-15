class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for x in operations:
            if x.isdigit() or  x.startswith('-'):
                st.append(int(x))
            elif x == '+':
                st.append(st[-1] + st[-2])
            elif x == 'D':
                st.append(2 * st[-1])
            elif x == 'C':
                st.pop()

        # sum = 0
        # for i in st:
        #     sum += i

        return sum(st)