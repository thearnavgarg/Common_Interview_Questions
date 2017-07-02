#include <bits/stdc++.h>
#include "LinkedList.h"

int solution(LinkedList* head1, LinkedList* head2) {
  if (head1 == NULL && head2 == NULL) {
    return INT_MAX;
  }
  int c_over = 0;
  LinkedList* head = NULL;
  LinkedList* current = NULL;
  while(head1 != NULL || head2 != NULL) {
    int sum = head1->value + head2->value + c_over;
    int u_digit = sum%10;
    if (head == NULL) {
      head = new LinkedList(u_digit);
      current = head;
    } else {
      current->next = new LinkedList(u_digit);
      current = current->next;
    }
    c_over = sum/10;
    head1 = head1->next;
    head2 = head2->next;
  }
  LinkedList* rHead = (head1 == NULL) ? head2 : head1;
  while(rHead != NULL) {
    int sum = rHead->value + c_over;
    int u_digit = sum%10;
    if (head == NULL) {
      head = new LinkedList(u_digit);
      current = head;
    } else {
      current->next = new LinkedList(u_digit);
      current = current->next;
    }
    c_over = sum/10;
    rHead = rHead->next;
  }
  if (c_over != 0) {
    current->next = new LinkedList(c_over);
  }
  // convert LinkedList to a number
  int num = 0;
  int counter = 0;
  while(head != NULL) {
    num += head->value*pow(10, counter);
    counter++;
    head = head->next;
  }
  return num;
}

LinkedList* reverse_list(LinkedList* head) {
  LinkedList* current = head;
  LinkedList* prev = NULL;
  while(current->next != NULL) {
    LinkedList* next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }
  current->next = prev;
  head = current;
  return head;
}

int solution1(LinkedList* head1, LinkedList* head2) {
  if (head1 == NULL && head2 == NULL) {
    return INT_MIN;
   }
  head1 = reverse_list(head1);
  head2 = reverse_list(head2);
  return solution(head1, head2);
}

int main() {
  LinkedList* head1 = new LinkedList(7);
  head1->next = new LinkedList(1);
  head1->next->next = new LinkedList(6);
  LinkedList* head2 = new LinkedList(5);
  head2->next = new LinkedList(9);
  head2->next->next = new LinkedList(2);
  int value = solution(head1, head2);
  head1 = new LinkedList(6);
  head1->next = new LinkedList(1);
  head1->next->next = new LinkedList(7);
  head2 = new LinkedList(2);
  head2->next = new LinkedList(9);
  head2->next->next = new LinkedList(5);
  int value1 = solution1(head1, head2); 
  std::cout << value << std::endl;
  std::cout << value1 << std::endl;
  return 0;
}
