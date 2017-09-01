/*
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
#include <iostream>
#include <map>

int solution(std::string s) {
  if (s.empty()) {
    return 0;
  }
  std::map<char, int> charPosition;
  unsigned int i, j, max;
  j = 0;
  i = 0;
  max = 0;
  while (j < s.size()) {
    char ch = s[j];
    if ( (charPosition.find(ch) != charPosition.end()) &&
         (charPosition.at(ch) >= i) ) {
      std::string substring(s.begin() + i, s.begin() + j - 1);
      int stringLen = j-i;
      if (max < stringLen) {
        max = stringLen;
      }
      i = charPosition.at(ch) + 1;
      charPosition.at(ch) = j;
    } else if (charPosition.find(ch) != charPosition.end() ) {
      charPosition.at(ch) = j;
    } else {
      charPosition.insert(std::pair<char, int> (ch, j));
    }
    j++;
  }
  // final check
  if (max < (j-i)) {
    return (j-i);
  }
  return max;
}
int main() {
  std::string s = "qwnfenpglqdq";
  int answer = solution(s);
  std::cout << answer << std::endl;
  return 0;
}
