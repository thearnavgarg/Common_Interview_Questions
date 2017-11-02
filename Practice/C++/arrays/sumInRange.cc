#include <iostream>
#include <vector>
#include <cmath>

int sumInRange(std::vector<int> nums, std::vector<std::vector<int>> queries) {
  long long int sum = 0;
  std::vector<int> subsetSum;
  // Going through the nums vector and adding all the elements till that index
  // and storing it in the subsetSum vector..
  // For example
  // nums = {1, 2, 3, 4, 5}
  // then subsetSum = {1, 3, 6, 10, 15}
  for (std::vector<int>::iterator it = nums.begin(); it != nums.end(); it++) {
      sum = sum + *it;
      subsetSum.push_back(sum);
  }
  sum = 0; // Resetting the sum value.
  // Here I am iterating over each set of element in the queries vector.
  for (auto& row : queries) {
      // row = [init_index, final_index]
      int first_index = row[0];
      int second_index = row[1];
      // sum(a, b) is sum of elements from index a to b
      // sum(a, b) = sum(0, b) - sum(0, a) + element.at(a);
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

