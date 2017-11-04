#include <iostream>
#include <cmath>

bool findReplace(std::string str1, std::string str2) {
  bool foundDiff = false;
  for (int i = 0; i < str1.size(); i++) {
    if (str1[i] != str2[i]) {
      if (foundDiff) {
        return false;
      } else {
        foundDiff = true;
      }
    }
  }
  return true;
}

bool findEdit(std::string str1, std::string str2) {
  char* charMap = new char[128];
  for (auto& ch : str1) {
    int index = int(ch) - int('a');
    charMap[index]++;
  }
  for (auto& ch : str2) {
    int index = int(ch) - int('a');
    charMap[index]--;
    if (charMap[index] < 0) {
      return false;
    }
  }
  return true;
}

bool solution(std::string input1, std::string input2) {
  if (std::abs(input1.size() - input2.size()) > 1) {
    return false;
  }
  if (input1.size() == input2.size()) {
    return findReplace(input1, input2);
  } else if (input1.size() > input2.size()) {
    return findEdit(input1, input2);
  }
  return findEdit(input2, input1);
}

int main() {
  std::string input1("");
  std::string input2("");
  std::cin >> input1 >> input2;
  std::cout << solution(input1, input2) << std::endl;
  return 0;
}
