#include <iostream>
#include <string>
#include <vector>
#include <map>

// Using a datastructure.
bool solution1(std::string input) {
  bool charMap[256];
  for (auto& ch : input) {
    if (charMap[int(ch)]) {
      return false;
    } else {
      charMap[int(ch)] = true;
    }
  }
  return true;
}

// No additional datastructure. 
bool solution2(std::string input) {
  int checker = 0;
  for(auto& ch : input) {
    int bit_shift = (int)ch - 'a';
    if ((checker & 1<<bit_shift) > 0) {
      return false;
    }
    checker = checker | 1<<bit_shift;
  }
  return true;
}

int main() {
  std::string input("");
  std::cout << "Enter a string: " << std::endl;
  std::cin >> input;
  std::cout << solution1(input);
  std::cout << solution2(input);
  return 0; 
}
