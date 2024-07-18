from collections import Counter

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        letterCount = Counter(letters)

        def can_form_word(w, letterCount):
            word_cnt = Counter(w)
            for c in word_cnt:
               if word_cnt[c] > letterCount[c]:
                   return False
            return True
        
        def get_score(word):
            res = 0 
            for c in word:
                res += score[ord(c) - ord('a')]
            return res
            
        def backtracking(index):
            if index == len(words):
                return 0
            # skip case
            res = backtracking(index+1)
            # use case
            if can_form_word(words[index], letterCount):
                for c in words[index]:
                    letterCount[c] -= 1
                res = max(res,backtracking(index+1) + get_score(words[index]))
                backtracking(index+1)
                for c in words[index]:
                    letterCount[c] += 1
            return res
        return backtracking(0)
    



sol = Solution()
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print(sol.maxScoreWords(words, letters, score))
        