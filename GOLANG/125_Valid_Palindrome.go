package main

import (
	"unicode"
)
/*
TODO:
	Restructure program to allow for easy testing/execution of programs
	Keep automation
*/


func isAlphaNumeric(char rune) bool {
	return unicode.IsLetter(char) || unicode.IsNumber(char)
}

func isPalindrome(s string) bool {
    left := 0
    right := len(s) -  1 // REMEMBER: len(s) is 1-based index

    for {
        if left >= right {
            return true
		}
		if !isAlphaNumeric(rune(s[left])){
			left = left + 1
			continue
		}

		if !isAlphaNumeric(rune(s[right])) {
			right = right - 1
			continue
		}
		
		leftChar := unicode.ToLower(rune(s[left]))
		rightChar := unicode.ToLower(rune(s[right]))

		if leftChar == rightChar {
			left = left + 1
			right = right - 1
		} else {
			return false
		}
	}
}

