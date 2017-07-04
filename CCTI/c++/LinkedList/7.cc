#include <bits/stdc++.h>
#include "LinkedList.h"

int list_size(LinkedList* head) {
  int size = 0;
  while(head != NULL) {
    size++;
    head = head->next;
  }
  return size;
}

// 1->2->3->4->5
//    1->2 ^
int solution(LinkedList* l1, LinkedList* l2) {
  if (l1 == NULL || l2 == NULL) {
    std::cout << "ERROR IN PASSING THE LIST" << std::endl;
    return INT_MIN;
  }
  int size1 = list_size(l1);
  int size2 = list_size(l2);
  int size = 0;
  if (size1 > size2) {
    size = size1 - size2;
    while(size--) {
      l1 = l1->next;
    }
  } else if (size2 > size1) {
    size = size2 - size1;
    while(size--) {
      l2 = l2->next;
    }
  } 
  bool found = false;
  while(l1 != NULL && l2 != NULL) {
    if (l1 == l2) {
      found = true;
      break;
    } 
    l1 = l1->next;
    l2 = l2->next;
  }
  if (found) return l1->value;
  return INT_MIN;
}

int main() {
  LinkedList node(5);
  LinkedList* head = new LinkedList(1);
  head->next = new LinkedList(2);
  head->next->next = new LinkedList(3);
  head->next->next->next = &node;
  head->next->next->next->next = new LinkedList(4);
  LinkedList* head1 = new LinkedList(1);
  head1->next = &node;
  int value = solution(head, head1);
  std::cout << value << std::endl;
  return 0;
}
