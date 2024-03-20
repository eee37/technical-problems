console.log('begin');
function isPalindrome(s) {
    var cleanString = s.replace(/[^a-z0-9]/, '');
    var startPointer = 0;
    var endPointer = cleanString.length;
    while (startPointer !== endPointer) {
        if (cleanString[startPointer] === cleanString[endPointer]) {
            continue;
        }
        else {
            return false;
        }
        startPointer--;
        endPointer--;
    }
    return true;
}
;
console.log(isPalindrome('A man, a plan, a canal: Panama'));
