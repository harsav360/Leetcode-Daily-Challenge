In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

   def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def check(first,second):
            i,j = 0,0
            while i < len(first) and j < len(second):
                if mp[first[i]] == mp[second[j]]:
                    i += 1
                    j += 1
                elif mp[first[i]] > mp[second[j]]:
                    return True
                else:
                    return False
            if i != len(first) and j == len(second):
                return False
            return True

        
        mp = {}
        i = len(order)
        for c in order:
            mp[c] = i
            i -= 1
        for i in range(len(words)-1):
            if not check(words[i],words[i+1]):
                return False
        return True
