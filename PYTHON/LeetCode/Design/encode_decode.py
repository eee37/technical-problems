class Codec:

    def encode(self, strs):
                # Initialize an empty string to hold the encoded string.
        encoded_string = ''
        for s in strs:
            # Append the length, the delimiter, and the string itself.
            encoded_string += str(len(s)) +  "?" + s
        return encoded_string


        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        index = 0
        start = 0
        ans = []
        while index < len(s):
            char = s[index]
            if char == '?':
                str_len = int(s[start:index])
                ans.append(s[index+1: index+1+str_len])
                index =index + 1 +str_len
                start = index
            else:
                index += 1
        return ans
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))