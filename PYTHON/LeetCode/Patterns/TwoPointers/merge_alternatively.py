# https://leetcode.com/problems/merge-strings-alternately/submissions/993882504/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    @staticmethod
    def mergeAlternately(word1: str, word2: str) -> str:
        output = [""] * (len(word1) + len(word2))

        short_len, long_word = (len(word2), word1) if len(word1) > len(word2) else (len(word1), word2)

        # fill in even
        for iter_1 in range(short_len):
            output[iter_1 * 2] = word1[iter_1]

        # fill in odd
        for iter_2 in range(short_len):
            output[iter_2 * 2 + 1] = word2[iter_2]

        # fill in overfill
        overfill_pos = short_len
        for iter_overfill in range(short_len * 2, (len(word1) + len(word2))): # BUG: On both ranges. Don't need to subtract 1
            output[iter_overfill] = long_word[overfill_pos]
            overfill_pos = overfill_pos + 1

        return "".join(output)


print(Solution.mergeAlternately("abc", "pqr"))
print(Solution.mergeAlternately("ab", "pqrs"))
print(Solution.mergeAlternately("abcd", "pq"))



