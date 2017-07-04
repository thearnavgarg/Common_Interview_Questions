#include <bits/stdc++.h>
#include "LinkedList.h"

LinkedList* solution(LinkedList* list, int x) {
  if (list == NULL) {
    return NULL;
  }
  if (list->next == NULL) {
    return list;
  }
  LinkedList* current = list->next;
  LinkedList* prev = list;
  while(current != NULL) {
    if (current->value < x) {
      prev->next = current->next;
      current->next = list;
      list = current;
      current = prev->next;
    } else {
      prev = current;
      current = current->next;
    }
  }
  return list;
}

int main() {
  // 3->5->8->5->10->2->1
  LinkedList* head = new LinkedList(3);
  head->next = new LinkedList(5);
  head->next->next = new LinkedList(8);
  head->next->next->next = new LinkedList(5);
  head->next->next->next->next = new LinkedList(10);
  head->next->next->next->next->next = new LinkedList(2);
  head->next->next->next->next->next->next = new LinkedList(1);
  LinkedList::print_list(head);
  std::cout << std::endl;
  head = solution(head, 5);
  LinkedList::print_list(head);
  return 0;
}
