You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

def longestStrChain(self, words: List[str]) -> int:
        def compare(str1,str2):
            if len(str1) != len(str2) + 1:
                return False
            first = 0
            second = 0

            while first < len(str1):
                if second < len(str2) and str1[first] == str2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1
            if first == len(str1) and second == len(str2):
                return True
            return False


        words.sort(key = len)
        n = len(words)
        dp = [1 for _ in range(n)]
        ans = 1
        for i in range(n):
            for prev in range(i):
                if compare(words[i],words[prev]) and dp[i] < dp[prev] + 1:
                    dp[i] = 1+dp[prev]
            if dp[i] > ans:
                ans = dp[i]

        return ans
