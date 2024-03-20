'''
    LC #604
    NOTES:
        SOLUTION:
            APPROACH #1
                - Turns out this is not O(n) where n is compressed string its O(m) where
                m is length of uncompressed string. I suppose n is not proportional to m
                - A potential problem with this approach could arise if the length of the uncompressed string is very large. In such a case, the size of the complete uncompressed string could become so large that it can't fit in the memory limits, leading to memory overflow
                -However, if hasNext() is performed most of the times, this approach isn't much advantageous since precomputation needs to be done anyhow.
                So any pre-computation is bad for hasnext operation. Is this bc has next can be done without any precomputation. This seems to be the reason
            APPROACH #2
                - Uses RegEx func in java to split by regex match
                - The precomputation step requires O(n)O(n) time. Thus, if hasNext() operation is performed most of the times, this precomputation turns out to be non-advantageous.
            APPROACH #3
                - Not how nums is created using power of 10s
                - I guess on average next could be O(1) but we need to create
                num on some cases which to me is O(n) where n is compressed string
                since that is an upperbound on num length
            Clean python solution that follows approach 2
            https://leetcode.com/problems/design-compressed-string-iterator/discuss/103866/Python-Straightforward-with-Explanation
'''
class StringIterator:

    def __init__(self, compressedString: str): # NOTE: Only need two pointers
        start = 0
        compressedArr = []
        for index, char in enumerate(compressedString):
            if index == 0:
                continue
            if char.isalpha():
                compressedArr = compressedArr + [compressedString[start]] * int(compressedString[start + 1: index])
                start = index
        # add last unprocessed chunk
        if compressedString:
            compressedArr = compressedArr + [compressedString[start]] * int(compressedString[start + 1: len(compressedString)])
        
        self.uncompressedString = ''.join(compressedArr)
        self.pos = 0
        print(self.uncompressedString)
                
        

    def next(self) -> str:
        if self.hasNext():
            self.pos += 1
            return self.uncompressedString[self.pos - 1]
        return ' '
        

    def hasNext(self) -> bool:
        return self.pos < len(self.uncompressedString)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()