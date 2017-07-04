#include <bits/stdc++.h>
#include "LinkedList.h"

int solution(LinkedList* list) {
  if (list == NULL) {
    return INT_MIN;
  }
  if (list->next == NULL) {
    return INT_MIN;
  }
  LinkedList* slow_head = list;
  LinkedList* fast_head = list;
  while(fast_head && fast_head->next)  {
    fast_head = fast_head->next->next;
    slow_head = slow_head->next;
    if (fast_head == slow_head) {
      break;
    }
  }
  if (!fast_head || !slow_head) {
    return INT_MIN;
  }
  slow_head = list;
  while(slow_head != fast_head) {
    slow_head = slow_head->next;
    fast_head = fast_head->next;
  }
  return fast_head->value;
}

int main() {
  LinkedList* head = new LinkedList(1);
  head->next = new LinkedList(2);
  head->next->next = new LinkedList(3);
  head->next->next->next = new LinkedList(4);
  head->next->next->next->next = new LinkedList(5);
  head->next->next->next->next->next = head->next;
  int value = solution(head);
  std::cout <<"The connection is at: " << value << std::endl;
  return 0;
}

