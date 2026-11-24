class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2 ) : return False
        elif len(s1) == 0: return True

        char_cnt = [0 for i in range (0, 26)]
        char_cnt2 = [0 for i in range (0, 26)]
        for r in range(0, len(s1)):
            char_cnt[ord(s1[r])  - ord('a')] += 1
        l = 0
        letter_cnt = 0
        
        for r in range(0, len(s2)):
            char_cnt2[ord(s2[r]) - ord('a')] += 1 
          #  if char_cnt2[ord(s2[r]) - ord('a')] > char_cnt[ord(s2[r]) - ord('a')]:
               # print(s2[0:r])
            while char_cnt2[ord(s2[r]) - ord('a')] > char_cnt[ord(s2[r]) - ord('a')]: 
                #print("removing %s because count of %c doesn't match, word: %s " % (s2[0: l + 1], s2[r] , s2[l:r]))
                char_cnt2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                letter_cnt -= 1
                
            letter_cnt+= 1
            if letter_cnt == len(s1): return True
        print(char_cnt)
        print(char_cnt2)
        print(letter_cnt)
        return letter_cnt == len(s1)

        
