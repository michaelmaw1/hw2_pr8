class S:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxL = 0
        charSet = set()
        l = 0

        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                maxL = max(maxL, r - l +1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
        
        return maxL

s1 = "abcabcbb"
s2 = "xxxxxxxx"
s3 = "pubwwkewsin"
test = S()
print(test.lengthOfLongestSubstring(s1))
print(test.lengthOfLongestSubstring(s2))
print(test.lengthOfLongestSubstring(s3))

