#include <iostream>
#include <string>

std::string solution(std::string s) {
  if (s.empty()){
    return s;
  }
  std::string answer("");
  int i = 0, j = 0;
  while (j < s.size()) {
    if (s[i] == s[j]) {
      j++;
    } else {
      answer += s[i] + std::to_string(j-i);
      i = j;
      j++;
    }
  }
  answer += s[i] + std::to_string(j-i);
  if (answer.size() >=s.size()) {
    return s;
  }
  return answer;
}

int main() {
  std::string input("");
  std::cin >> input;
  std::cout << solution(input) << std::endl;
  return 0;
}
