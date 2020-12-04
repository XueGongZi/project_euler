class Solution:
    def collatz_sequence_length(self, num):
        length = 1
        while num != 1:
            length += 1
            if num % 2 == 1:
                num = 3 * num + 1
            else:
                num = num // 2
        return length
 
    def longest_collatz_sequence(self, limit):
        length = 10
        for i in range(14, limit + 1):
            new_length = self.collatz_sequence_length(i)
            if length < new_length:
                length = new_length
                result = { 'length': new_length, 'number': i }
        return result['number']
