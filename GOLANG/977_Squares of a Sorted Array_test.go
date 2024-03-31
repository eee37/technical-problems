package main

import (
	"reflect"
	"testing"
)

func TestSortedSquares(t *testing.T) {
	var tests = []struct {
		name     string
		input    []int
		expected []int
	}{
		{"With Negative and Postive Numbers and 0", []int{-4, -1, 0, 3, 10}, []int{0, 1, 9, 16, 100}},
		{"All Negative", []int{-7, -3, -2, -1}, []int{1, 4, 9, 49}},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			ans := sortedSquares(test.input)
			if !reflect.DeepEqual(ans, test.expected) {
				t.Errorf("Expected > %v < but got > %v <", test.expected, ans)
			}
		})
	}

}
