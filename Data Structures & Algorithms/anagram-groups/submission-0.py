class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        a = {}

        for i in strs:
            sort = ''.join(sorted(i))

            if sort not in a:
                a[sort] = []
            a[sort].append(i)

        return list(a.values())
