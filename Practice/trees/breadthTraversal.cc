#include <iostream>
#include <queue>

#include "node.h"

void traversal(Node* head) {
  if (head == nullptr) {
    return;
  }
  std::queue<Node*> q;
  q.push(head);
  while (!q.empty()) {
    Node* current = q.front();
    q.pop();
    if (current->left != nullptr) {
      q.push(current->left);
    }
    if (current->right != nullptr) {
      q.push(current->right);
    }
    std::cout << current->data << " ";
  }
}

int main() {
  Node* head = new Node(1);
  head->left = new Node(2);
  head->left->left = new Node(3);
  head->left->left->left = new Node(4);
  head->left->left->right = new Node(5);
  head->left->right = new Node(6);
  head->right = new Node(7);

  traversal(head);
  return 0;
}