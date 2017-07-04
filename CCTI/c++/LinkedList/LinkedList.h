#include <bits/stdc++.h>

class LinkedList {
public:
  int value;
  LinkedList* next;
  LinkedList(int value){
    this->value = value;
  }
  static void print_list(LinkedList* head) {
    while(head != NULL) {
      std::cout << head->value << " ";
      head = head->next;
    }
  }
};
