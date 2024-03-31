/*
This is a simple program that generates a template for Leetcode questions. It takes the leetcode id and the question name as input and generates a markdown file with the template for the question and a go file with the same name as the question.

Enhancements:
- Add a flag to specify the directory where the files should be generated
- Fill out markdown file details with the leetcode id and question name
- Create test file automatically
- Consider replacing spaces with _ in the file names
- Modularize the code
*/
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Generating Leetcode template ...")
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter the leetcode id \n")
	leetcodeId, _ := reader.ReadString('\n')
	leetcodeId = leetcodeId[:len(leetcodeId)-1] // Remove the newline character

	fmt.Print("Enter the leetcode question name \n")
	questionName, _ := reader.ReadString('\n')
	questionName = questionName[:len(questionName)-1] // Remove the newline character

	documentationFileName := fmt.Sprintf("%s_%s.md", leetcodeId, questionName)
	documentationFile, err := os.Create(documentationFileName) // Create a new file

	if err != nil {
		fmt.Println(err)
		return
	}
	defer documentationFile.Close()

	inputData, err := os.ReadFile("./LeetCode/Template.md")
	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	// Write the contents to the output file
	err = os.WriteFile(documentationFileName, inputData, 0644)
	if err != nil {
		fmt.Println("Error writing to output file:", err)
		return
	}

	fmt.Println("Documentation file successfully written")

	_ , err = os.Create(fmt.Sprintf("%s_%s.go", leetcodeId, questionName)) // Create a new file
	if err != nil {
		fmt.Println("Error writting file:", err)
		return
	}
}
