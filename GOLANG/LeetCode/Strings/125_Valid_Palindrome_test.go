package main

import (
    "testing"
)

func TestIsPalindrome(t *testing.T) {
    var tests = []struct {
        name string
        input string
        expected bool
    }{
        {"TRUE: ODD CASE", "A B A", true},
        {"TRUE: EVEN CASE", "1221", true},
        {"FALSE", "palindrome", false},
    }

    for _, test := range tests {
        t.Run(test.name, func(t *testing.T) {
            ans := isPalindrome(test.input)
            if ans != test.expected {
                t.Errorf("Expected > %t < but got > %t <", test.expected, ans)
            }
        })
    }
    
}