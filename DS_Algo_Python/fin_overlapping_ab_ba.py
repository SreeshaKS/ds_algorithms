import re

class Solution:
    def solve(self, A):
        if re.search("(AB.*BA|BA.*AB)", A):
           return "YES"
        return "NO"