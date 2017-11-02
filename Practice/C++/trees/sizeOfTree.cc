/* Returns the number of nodes in the tree */

#include <iostream>

#include "node.h"

int size_of_tree(Node* head) {
  if (head == nullptr) {
    return 0;
  }
  return ( 1+ size_of_tree(head->left) + size_of_tree(head->right) );
}

int main() {
  Node* head = new Node(1);
  head->left = new Node(2);
  head->right = new Node(3);
  head->left->left = new Node(4); 

  std::cout << "Size of the tree: " << size_of_tree(head);
  std::cout << "\n";
  return 0;
}