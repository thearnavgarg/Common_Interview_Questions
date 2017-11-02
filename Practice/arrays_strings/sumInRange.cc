#include <iostream>
#include <vector>
#include <cmath>

int sumInRange(std::vector<int> nums, std::vector<std::vector<int>> queries) {
  long long int sum = 0;
  std::vector<int> subsetSum;
  for (std::vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
      sum = sum + *it;
      subsetSum.push_back(sum);
  }
  sum = 0; // Resetting the sum value.
  for (auto& row : queries) {
      int first_index = row[0];
      int second_index = row[1];
      sum = sum + (subsetSum.at(second_index) - subsetSum.at(first_index) + nums.at(first_index));
  }
  unsigned long int num_mod = (int)(std::pow(10, 9) + 7);
  if (sum < 0) {
      return num_mod - ((-1*sum)%num_mod);
  }
  return (sum % num_mod);
}

int main() {
  std::vector<int> nums = {3, 0, -2, 6, -3, 2};
  std::vector<std::vector<int>> queries = {{0, 2}, {2, 5}, {0, 5}};

  std::cout << sumInRange(nums, queries) << std::endl;
  return 0;
}

