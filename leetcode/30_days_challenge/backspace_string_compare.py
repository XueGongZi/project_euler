class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ha = "#"
        def start_from_correct_index(s: str):
            n = len(s)
            for i in range(n):
                if s[i] != ha:
                    result = s[i:]
                    break
            return result
        def segment(s: str):
            result = []
            n = len(s)
            j = 0
            for k in range(n):
                new_str = s[j:(k + 1)]
                if k == n - 1:
                    result += [new_str]
                    break
                condition = (s[k] == ha) and (s[k + 1] != ha)
                without_hash = list(filter(lambda x: x != ha, list(new_str)))
                count_hash = len(new_str) - len(without_hash)
                if condition and (ha not in s[(k + 1):]):
                    new_s = s[j:(k + 1)]
                    last_s = s[(k + 1):]
                    result += [new_s, last_s]
                    break
                elif condition and (len(without_hash) <= count_hash): 
                    new_s = s[j:(k+1)]
                    result += [new_s]
                    j = k + 1
            return result
        def join_back(arr):
            result = ""
            for i in arr:
                result += i
            return result
        def remove_hash(s: str):
            arr = list(s)
            after_count = list(filter(lambda x: x != ha, arr))
            new_s = join_back(after_count)
            count = len(after_count)
            number_of_hash = len(arr) - count
            if count <= number_of_hash:
                return ""
            else:
                while ha in s:
                    ind = s.index(ha)
                    s = s[:(ind - 1)] + s[(ind + 1):]
                return s
        s = segment(start_from_correct_index(S))
        t = segment(start_from_correct_index(T))
        join_s = join_back(list(map(lambda x: remove_hash(x), s)))
        join_t = join_back(list(map(lambda x: remove_hash(x), t)))
        return join_s == join_t

s = "ab#c###d"
t = "abaerjl###dare#"
s1 = "ab#c"
t1 = "ad#c"
s2 = "ab##"
t2 = "c#d#"
s3 = "a##c"
t3 = "#a#c"
s4 = "a#c"
t4 = "b"
s5 = "bxj##tw"
t5 = "bxo#j##tw"
s6 = "nzp#o#g"
t6 = "b#nzp#o#g"
s7 = "y#ujr#y##csb#txvhjs"
t7 = "ujy##csb#txvhjs"
# print(Solution().backspaceCompare(s7, t7))
# print(Solution().backspaceCompare(s6, t6))
# print(Solution().backspaceCompare(s5, t5))
# print(Solution().backspaceCompare(s4, t4))
# print(Solution().backspaceCompare(s3, t3))
# print(Solution().backspaceCompare(s2, t2))
# print(Solution().backspaceCompare(s1, t1))
# print(Solution().backspaceCompare(s, t))
