* Given strings  J  representing the types of stones that are jewels, and  S  representing the stones you have. Each character in  S  is a type of stone you have. Determine how many of the stones you have are also jewels. Letters are case sensitive, so “a” is considered a different type of stone from “A”. Examples :
```
Input:  J = ‘aA’, S = ‘aAAbbbb’  Output:  3  
Input:  J = ‘z’, S = ‘ZZ’  Output:  0
```

* Write a function which takes two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. The characters in the first should appear without their order changing in the second string.
Examples :
```
Input:  ‘abc’, ‘abracadabra’  Output:  true  
Input:  ‘abc’, ‘acb’ Output:  false
```

* Write a function which accepts a string and returns the length of the longest substring with no
repeating characters. Examples:
```
Input:  ‘ ‘  Output:  0  
Input:  ‘thisisawesome’  Output:  6  
Input:  ‘bbbbbbb’  Output:  1
```

* Given a string containing just the characters ‘(‘, ‘)’, ‘{‘, ‘}’, ‘[‘, and ‘]’, determine if the input string is valid.
Examples:
```
Input:  ‘()[]{}’  Output:  true  
Input:  ‘{[]}’  Output:  true
Input:  ‘([)]’  Output:  false
```

* A string is said to be a special palindromic string if all of the characters are the same, e.g. ‘aaa’ and all characters except the middle one are the same, e.g. ‘aadaa’. Given a string, determine how many special palindromic substrings can be formed from it.
Examples:
```
Input: ‘asasd’  Output:  7  
Explanation:  [a, s, a, s, d, asa, sas]
Input: ‘ abcbaba’  Output:  10  
Explanation: [a, b, c, b, a, b, a, bcb, bab, aba]
```
