class Solution:
    def group_anagrams(self, strs: [str]) -> [[str]]:
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())
