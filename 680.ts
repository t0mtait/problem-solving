function validPalindrome(s:string): boolean {
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1);
        left++; right--;
    }
    return true;

    function isPalindrome(str: string, start: number, end: number): boolean {
        while (start < end) {
            if (str[start] !== str[end]) return false;
            start++; end--;
        }
        return true;
    }
}

let s = "abca"
console.log(validPalindrome(s))



// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

// Example 1:

// Input: s = "aba"
// Output: true

// Example 2:

// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.

// Example 3:

// Input: s = "abc"
// Output: false
