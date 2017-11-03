#include <iostream>

bool check_permutation(std::string input1, std::string input2) {
  if (input1.size() != input2.size()) {
    return false;
  }

  int* charMap = new int[256];
  for (auto& ch : input1) {
    charMap[int(ch)] += 1;
  }
  for (auto& ch : input2) {
    charMap[int(ch)] -= 1;
    if (charMap[int(ch)] < 0) {
      return false;
    }
  }

  return true;
}

int main() {
  std::string input1("");
  std::string input2("");
  std::cin >> input1 >> input2;
  std::cout << check_permutation(input1, input2) << std::endl;
  return 0;
}
