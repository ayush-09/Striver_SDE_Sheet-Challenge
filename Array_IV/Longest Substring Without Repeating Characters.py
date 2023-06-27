def lengthOfLongestSubstring(s):
    ma=0
    st=0
    se={}
    for i in range(len(s)):
        ch=s[i]
        if ch in se:
            st=max(st,se[ch]+1)
        ma=max(ma,i-st+1)
        se[ch]=i
    return ma

if __name__=="__main__":
    print(lengthOfLongestSubstring("abcabcbb"))