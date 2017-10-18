#include <iostream>
#include <vector>

int firstDuplicate(std::vector<int> a) {
  int index = 0;
  for (size_t i = 0; i < a.size(); i++) {
    index = abs(a[i]) - 1;
    if (a[index] < 0) {
      return abs(a[i]);
    } else {
      a[index] = -a[index];
    }
  }
  return -1;
}

int main() {
  std::vector<int> a = {2, 3, 3, 1, 5, 2};
  std::cout << "Solution: " << firstDuplicate(a);
  std::cout << "\n";
  return 0;
}