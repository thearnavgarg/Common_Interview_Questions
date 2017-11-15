/*
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
   */
#include <iostream>
#include <string>

bool solution(std::string& input) {
  if (input.empty()) {
    return false;
  }
  if (input.size() == 1) {
    return true;
  }
  std::string cleanString("");
  for (int i = 0; i < input.size(); i++) {
    if (std::isalnum(input[i])) {
      cleanString += std::tolower(input[i]);
    }
  }

  int start = 0, end = cleanString.size()-1;
  while(end >= start) {
    if (cleanString[start] != cleanString[end]) {
      return false;
    }
    start++; end--;
  }
  return true;
}

int main() {
  std::string testcase1 = "A man, a plan, a canal: Panama";
  std::string testcase2 = "race a car";

  std::cout << solution(testcase1) << std::endl;
  std::cout << solution(testcase2) << std::endl;

  return 0;
}
