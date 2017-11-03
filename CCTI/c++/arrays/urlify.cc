#include <iostream>

void urlify(std::string& input, int true_len){
  /*
   * 01234567890123456
   * Mr John Smith    |
   * Mr%20John%20Smith
   */
  if (input.size() < true_len) {
    return;
  }
  int i = true_len-1, j = input.size()-1;
  while (i > 0 && j > 0) {
    if (input[i] != ' ') {
      input[j] = input[i];
      j--; i--;
    } else {
      input[j] = '0';
      input[j-1] = '2';
      input[j-2] = '%';
      j = j-3;
      i = i-1;
    }
  }
}

int main() {
  std::string input("Mr John Smith    ");
  int true_len = 13;
  urlify(input, true_len);
  std::cout << input << std::endl;
  return 0;
}
