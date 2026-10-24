def word_break(s, wordDict):
    dp=[False]*(len(s)+1)
    dp[0]=True
    for i in range(len(s)):
        if dp[i]:
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    dp[i+len(word)]=True
    return dp[len(s)]
print(word_break("leetcode", ["leet", "code"]))