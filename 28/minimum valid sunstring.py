s = "ADOBEC"
t = "ABC"
left=0
need={}
for ch in t:
    need[ch]=need.get(ch,0)+1
window={}
for right in range(len(s)):
    window[s[right]]=window.get(s[right],0)+1
    for ch in need:
        window[ch]>=need[ch]
        left+=1

    

        
    

        
 
        