#include <bits/stdc++.h>
#include "LinkedList.h"

LinkedList* with_temp_buffer(LinkedList* list) {
  if (list == NULL) {
    return NULL;
  }
  if (list->next == NULL) {
    return list;
  }
  std::map<int, int> list_map;
  LinkedList* current = list;
  LinkedList* prev = NULL;
  while(current != NULL) {
    if (list_map.find(current->value) == list_map.end()) {
      list_map.insert({current->value, 1});
    } else {
      prev->next = current->next;
    }
    prev = current;
    current = current->next;
  }
  return list;
}

LinkedList* without_temp_buffer(LinkedList* list) {
  if(list == NULL) {
    return NULL;
  }
  if(list->next == NULL) {
    return list;
  }
  LinkedList* head = list;
  LinkedList* current = NULL;
  LinkedList* prev = NULL;
  while(head != NULL) {
    prev = head;
    current = head->next;
    int val = head->value;
    while(current != NULL) {
      if(current->value == val) {
        prev->next = current->next;
        current = current->next;
      } else {
        prev = prev->next;
        current = current->next;
      }
    }
    head = head->next;
  }
  return list;
}

int main() {
  LinkedList* head;
  head = new LinkedList(1);
  head->next = new LinkedList(1); 
  head = without_temp_buffer(head);
  LinkedList::print_list(head);
  return 0;
}
