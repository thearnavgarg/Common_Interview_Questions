#include <bits/stdc++.h>
#include "LinkedList.h"
#include <stack>

bool solution(LinkedList* head) {
  LinkedList* rhead = head;
  std::stack<int> s;
  while(rhead != NULL) {
    s.push(rhead->value);
    rhead = rhead->next;
  }
  bool is_pal = true;
  while(!s.empty()) {
    if (s.top() != head->value) {
      is_pal = false;
      break;
    }
    head = head->next;
    s.pop();
  }
  return is_pal;
}  

int main() {
  LinkedList* head = new LinkedList(1);
  head->next = new LinkedList(2);
  head->next->next = new LinkedList(4);
  head->next->next->next = new LinkedList(1);
  bool is_pal = solution(head);
  std::cout << is_pal << std::endl;
  return 0;
}
