
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        chars = list(counter.keys())
        chars.sort(key=counter.get, reverse=True)

        result = ''
        for char in chars:
            result = result + char * counter.get(char) # NOTE: Python supports string interpolation f'{var}chars' or can use join function
        return result

if __name__ == '__main__':
    sol = Solution()
    assert sol.frequencySort('tree') == 'eetr'
    assert sol.frequencySort('cccaaa') == 'cccaaa'
    assert sol.frequencySort('Aabb') == 'bbAa'