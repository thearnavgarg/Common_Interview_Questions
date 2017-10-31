class Node {
  
public:
  int data;
  Node* left;
  Node* right;

  Node() {
    this->data = 0;
    this->left = nullptr;
    this->right = nullptr;
  }

  Node(int data) {
    Node();
    this->data = data;
  }
};