#include <bits/stdc++.h>
#include "LinkedList.h"

LinkedList* solution(LinkedList* list) {
  if (list == NULL) {
    return NULL;
  }
  int lsize = 0;
  LinkedList* head = list;
  while(head != NULL) {
    lsize++;
    head = head->next;
  }
  if (lsize < 3) {
    return list;
  }
  int mid = lsize/2;
  head = list;
  while(mid != 1) {
    head = head->next;
    mid--;
  }
  head->next = head->next->next;
  return list;
}

int main() {
  LinkedList* head = new LinkedList(1);
  head->next = new LinkedList(2);
  head->next->next = new LinkedList(3);
  head->next->next->next = new LinkedList(4);
  head->next->next->next->next = new LinkedList(5); 
  head = solution(head);
  LinkedList::print_list(head);
  return 0;
}
