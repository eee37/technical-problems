function isPalindrome(s: string): boolean {
    let cleanString = s.toLocaleLowerCase().replace(/[^a-z0-9]/g, ''); // Without the g flag, it'll do the first occurance of a match
    let startPointer = 0;
    let endPointer = cleanString.length - 1;

    while(startPointer < endPointer) { // cant use equal bc it will fail in the case that s is of length of one as endpointer will start before startpointer
        if (cleanString[startPointer] === cleanString[endPointer]) {
            startPointer++
            endPointer--
        }
        else {
            return false
        }
    }
    return true;
};

console.log(isPalindrome(' '))