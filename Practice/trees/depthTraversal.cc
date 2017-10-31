#include <iostream>

#include "node.h"

void postorder_traversal(Node* head) {
  // Base condition
  if (head == nullptr) {
    return;
  }

  postorder_traversal(head->left);
  postorder_traversal(head->right);
  std::cout << head->data << " => ";
}

void preorder_traversal(Node* head) {
  // Base condition
  if (head == nullptr) {
    return;
  }

  std::cout << head->data << " => ";
  preorder_traversal(head->left);
  preorder_traversal(head->right);

}

void inorder_traversal(Node* head) {
  // Base condition
  if (head == nullptr) {
    return;
  }

  // recursive calls
  inorder_traversal(head->left);
  std::cout << head->data << " => ";
  inorder_traversal(head->right);
}

int main() {
  Node *head  = new Node(1);
  head->left = new Node(2);
  head->right = new Node(3);
  head->left->left = new Node(4);
  head->left->right = new Node(5);

  inorder_traversal(head);
  std::cout << "NULL" << std::endl;
  preorder_traversal(head);
  std::cout << "NULL" << std::endl;
  postorder_traversal(head);
  std::cout << "NULL" << std::endl;
  return 0;
}