class Solution:
    '''
        Learnings: 
            1. Misinterpreted problem. Permutation chars must be adjacent
            2. Leetcode problem different from textbook. Leetcode cares about order, textbook doest not

            Lessons:
                1. Go through examples!!!
                2. Re-read problem statement at least twice
                3. CtCI and LeetCode problems are not identical!
    '''
    @staticmethod
    def checkInclusion( s1: str, s2: str) -> bool:
        # assing shortest
        shortest: str 
        longest: str


        if len(s1) < len(s2):
            shortest = s1
            longest = s2
        else:
            shortest = s2
            longest = s1

        # sort shortest
        shortest = sorted(shortest)

        # return
        for index in range(len(longest) - len(shortest) + 1): # need to add a + 1 here. Because range is [)
            if longest[index] in shortest:
                if shortest == sorted(longest[index: index + len(shortest)]): # dont need + 1 bc len is not 0 index based
                    return True
        
        return False


    @staticmethod
    def checkInclusionv1( s1: str, s2: str) -> bool:
        # sort
        x1 = sorted(s1)
        x2 = sorted(s2)

        # assing shortest
        shortest: str 
        longest: str 

        if len(x1) < len(x2):
            shortest = x1
            longest = x2
        else:
            shortest = x2
            longest = x1

        # return
        for char in shortest:
            if char not in longest:
                return False
            else:
                longest = longest[longest.index(char):]
        
        return True


if __name__ == '__main__':
    #print(Solution.checkInclusion('ab', 'cbac'))
    #print(Solution.checkInclusion('ab', 'eidboaoo'))
    print(Solution.checkInclusion('ab', 'ba'))
    #print(Solution.checkInclusion('', 'ba'))