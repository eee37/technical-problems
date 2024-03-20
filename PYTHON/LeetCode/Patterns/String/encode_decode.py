'''
******************* PROBLEM STATEMENT
LC # 271

******************* NOTES
******** MY IMPLEMENTATION:

TIME COMPLEXITY:
SPACE COMPLEXITY:

******** SOLUTION

TIME COMPLEXITY:
SPACE COMPLEXITY:

******************* TAGS
'''


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
#         output = ''
        
#         for string in strs:
#             if len(string) > 0:
#                 output = f'{output} {string}'
        return "\s".join(strs)   # NOTE: Py Method str_delimeter.join(arr)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split("\s") # NOTE: Py Method str.split(str_delimeter)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))