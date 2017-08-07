// return the kth to the last element
#include <bits/stdc++.h>
#include "LinkedList.h"

int solution(LinkedList* list, int k) {
  if (list == NULL) {
    return INT_MIN;
  }
  int list_size = 0;
  LinkedList* head = list;
  while(head != NULL) {
    head = head->next;
    list_size++;
  }
  int element_pos = list_size - k;
  if (element_pos < 0) {
    return INT_MIN;
  }
  head = list;
  while(element_pos > 0) {
    head = head->next;
    element_pos--;
  }
  return head->value;
}

int main() {
  LinkedList* head = new LinkedList(1);
  head->next = new LinkedList(2);
  head->next->next = new LinkedList(3);
  head->next->next->next = new LinkedList(4);
  int value= solution(head, 2);
  std::cout << "The list is : " << std::endl;
  LinkedList::print_list(head);
  std::cout << std::endl;
  std::cout << value << std::endl;
  return 0;
}
