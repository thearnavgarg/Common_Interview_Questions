#include <iostream>
#include <string>

/*
 * Return a binary string representation of a given integer.  
 */

/*
 * Time Complexity: O(log(N))
 * Space Complexity: O(1)
 */

std::string binaryStringofInt(int input) {
  /*
   * 3 = 0011
   * 4 = 0100
   */
  if (input == 0) {
    return "00000000";
  }

  std::string answer("");
  while (input != 0) {
    int bit = input % 2;
    answer = std::to_string(bit) + answer;
    input = input/2;
  }

  if (answer.size() < 8) {
    int padding = 8 - answer.size();
    for (int i = 0; i < padding; i++) {
      answer = "0" + answer;
    }
  }

  return answer;
}

int main() {

  int input = 0;
  std::cout << "Enter an int: ";
  std::cin >> input;

  std::cout << binaryStringofInt(input) << std::endl;
  return 0;
}
