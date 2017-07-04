
// ANSWER IS NOT COMPLETE. NEED TO FIGURE OUT THE 
// POINT OF INTERSECTION.

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
  while(fast_head->next->next != NULL && slow_head->next != NULL) {
    fast_head = fast_head->next->next;
    slow_head = slow_head->next;
    if (fast_head == slow_head) {
      return slow_head->value;
    }
  }
  return INT_MIN;
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

