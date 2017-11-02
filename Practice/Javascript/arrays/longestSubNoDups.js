/*
Given a string, find the length of the longest substring without repeating characters. 

Examples:
'abcabcbb' => 3 (abc).
'bbbbb' => 1 (b). 
'pwwkew' => 3 (wke).

Time Complexity: O(n).
Space Complexity: O(1).
*/

function longestSubNoDups(s, n) {
	if (n === 0) return 0;
	const sNoDups = [... new Set(s)];
	const m = sNoDups.length;
	let current = 1;
	let max = 1;
	for (let i = 0; i < n; i++) {
		if ((s[i] === sNoDups[i % m]) && (current < m)) {
			current++;
		} else {
			if (current > max) {
				max = current;
				current = 1;
			}
		}
	}
	return max;
}