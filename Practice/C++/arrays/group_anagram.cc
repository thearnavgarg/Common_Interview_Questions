/*
Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
*/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

void solution(std::string inputList[], int size) {
  std::map<std::string, std::vector<std::string>> anagram_group;

  for (int i = 0; i < size; i++) {
    std::string key = inputList[i];
    std::sort(key.begin(), key.end());
    if (anagram_group.find(key) != anagram_group.end()) {
      anagram_group[key].push_back(inputList[i]);
    } else {
      std::vector<std::string> temp;
      temp.push_back(inputList[i]);
      anagram_group.insert({key, temp});
    }
  }
  std::map<std::string, std::vector<std::string>>::const_iterator it;
  for (it = anagram_group.begin(); it != anagram_group.end(); it++) {
    std::vector<std::string> tempVec = it->second;
    for (std::string s : tempVec) {
      std::cout << s << " ";
    }
    std::cout << std::endl;
  }
}

int main() {
  std::string listAnagram[] = {"eat", "tea", "tan", "ate", "nat", "bat"};
  solution(listAnagram, 6);
  return 0;
}
