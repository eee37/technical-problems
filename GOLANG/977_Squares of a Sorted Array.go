package main


func reverseArray(nums []int) []int {
	result := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		result[i] = nums[len(nums) - i - 1]
	}

	return result

}

func sortedSquares(nums []int) []int {
	start := 0
	end := len(nums) - 1

	var result []int; // NOTE: Previosly had result := make([]int, len(nums) but then append will add at the end of the array. For that to have worked I would have had to use indexes

	
	for start <= end {
		if nums[start] * nums[start] > nums[end] * nums[end] {
			result = append(result, nums[start] * nums[start])
			start = start + 1
		} else {
			result = append(result, nums[end] * nums[end])
			end = end - 1
		}
	}

	return reverseArray(result)
}