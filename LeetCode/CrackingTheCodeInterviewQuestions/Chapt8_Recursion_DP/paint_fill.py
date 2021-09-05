from typing import List

'''
    Time Complexity: sr + sc
    Space Complexity: sr + sc. To reduce make iteritevely
    Variable Names Note:
    If you used the variable names x and y to implement this, be careful about the ordering of the variables in
    screen [y] [x]. Because x represents the horizontal axis (that is, it's left to right), it actually corresponds
    to the column number, not the row number. The value of y equals the number of rows. This is a very easy
    place to make a mistake in an interview, as well as in your daily coding. It's typically clearer to use row and
    column instead, 
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        sr_len = len(image)
        sc_len = len(image[0])
        # out bounds
        if sr < 0 or sc < 0 or sr >= sr_len or sc >= sc_len: # This check could have been moved over to helper fxn and then checks could have been removed
            return image
        # complete
        if image[sr][sc] == newColor:
            return image

        return Solution.floodFillHelper(image, sr, sc, newColor, image[sr][sc], sr_len, sc_len)

    @staticmethod
    def floodFillHelper(image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int, sr_len, sc_len):
        image[sr][sc] = newColor
        # top
        if sr - 1 >= 0:
            if image[sr - 1][sc] != newColor and image[sr - 1][sc] == oldColor:
                Solution.floodFillHelper(image, sr - 1, sc, newColor, oldColor, sr_len, sc_len)

        # left
        if sc - 1 >= 0:
            if image[sr][sc - 1] != newColor and image[sr][sc - 1] == oldColor:
                Solution.floodFillHelper(image, sr, sc - 1, newColor, oldColor, sr_len, sc_len)

        # right
        if sc + 1 < sc_len:
            if image[sr][sc + 1] != newColor and image[sr][sc + 1] == oldColor:
                Solution.floodFillHelper(image, sr, sc + 1, newColor, oldColor, sr_len, sc_len)

        # bottom
        if sr + 1 < sr_len:
            if image[sr + 1][sc] != newColor and image[sr + 1][sc] == oldColor:
                Solution.floodFillHelper(image, sr + 1, sc, newColor, oldColor, sr_len, sc_len)
        return image


if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill([[0,0,0],[0,0,0]], 0,  0, 2))
    print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))