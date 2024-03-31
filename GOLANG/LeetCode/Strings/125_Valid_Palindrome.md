Name the file [leetcode problem id]_[Name of Problem]

# #125 Valid Palindrome
```
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

### Tags
```
#easy, #string
```

### Notes and Takeaways
```
1. Using the string[index] syntax we work with bytes
Using the for index, value := range string syntax we work with runes
Because bytes are limited to ASII characters it is best to work with runes
2. unicode library is handy when it comes to working with runes
3. Negate operator is !
```

### My Solution
```
Time Complexity: n where n is the length of the string
Space Complexity: 0
``` 