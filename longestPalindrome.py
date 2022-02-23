def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        string = []
        length = []
        for i in range(len(s)): 
            for j in range(i + 1, len(s) + 1): 
                if s[i:j] == s[i:j][::-1]: 
                    string.append(s[i:j])
                    length.append(len(s[i:j]))
        
        max_index = length.index(max(length))
        return string[max_index]
        
s = "aabcdee"
print(longestPalindrome(s))