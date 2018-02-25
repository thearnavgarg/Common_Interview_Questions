#include <iostream>
#include <vector>
#include <string>
#include <cmath>

/*
 * You are given two integers, p and q. Complete the function  calculatePower which takes two integers
 * as arguments and returns p to the power of q,  without using the built-in power function.
 * We expect you to do better than O(q). A same input is p = 2 and q = 3, and the corresponding output is 8.
 * Constraints: 0 <= p^q <= ((2^63) - 1)
 */

/*
 * Time Complexity: O(log(q))
 * Space Complexity: O(1) (without function stack)
 * Space Complexity: O(log(q)) (With function stack)
 */

int computePower(int p, int q) {
  const static bool odd = (q%2 == 0) ? false : true;
  const static int original_p = p;

  if (q == 1) {
    if (odd) {
      return p * original_p;
    }
    return p;
  }
  if (p == 1) {
    return p;
  }

  p = p*p;
  q = q/2;
  return computePower(p, q); 
}

int main() {
  /*
   * example: 2^5 = 4^2 * 2 = 8^1 * 2
   */
  int p, q;
  std::cout << "Enter the values of p and q: ";
  std::cin >> p >> q;
  std::cout << computePower(p, q) << std::endl;
  return 0;
}

















































