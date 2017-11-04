#include <iostream>
#include <string>

bool solution(std::string input) {
  // Assuming that an empty string will return true.
  if (input.size() < 2) {
    return true;
  }
  char* charMap = new char[256];
  int countOdd = 0;
  for (auto& ch : input) {
    if (ch == ' ') {
      continue;
    }
    ch = std::tolower(ch, std::locale());
    charMap[ch] += 1;
    if (charMap[ch] % 2 == 0) {
      countOdd -= 1;
    } else {
      countOdd += 1;
    }
  }
  if (countOdd > 1) {
    return false;
  }
  return true;
}

int main() {
  std::string input("Tac Coa");
  std::cout << solution(input) << std::endl;
  return 0;
}
