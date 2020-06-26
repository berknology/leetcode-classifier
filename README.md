# Leetcode problem classifier
This repository aims to categorize and label frequently asked leetcode coding questions into major categories such as 
linked list, binary search, two pointers, and backtracking, etc., and facilitate interviewees and developers to practice 
common programming interview questions.

Two great online resources have been leveraged to compile the list: 
[Huahua](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) and 
[CyC2018](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E7%9B%AE%E5%BD%95.md).


## Linked list

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[206](https://leetcode.com/problems/reverse-linked-list/) | Reverse Linked List | Easy | | Iteratively is straightforward but recursively is a little bit tricky.
[21](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge Two Sorted Lists | Easy | [23](https://leetcode.com/problems/merge-k-sorted-lists/) | Recursion make solution much cleaner for Problem 21. Use heap for Problem 23.
[160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Intersection of Two Linked Lists | Easy | | Connect the end of a list to the head of the other list.
[19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Remove Nth Node From End of List | Medium | | Use two pointers and let one move N times first.
[24](https://leetcode.com/problems/swap-nodes-in-pairs/) | Swap Nodes in Pairs | Medium | | Use recursion and divide & conquer.
[2](https://leetcode.com/problems/add-two-numbers/) | Add Two Numbers | Medium | [445](https://leetcode.com/problems/add-two-numbers-ii/)| Iterate, add number and make new linked list.
[725](https://leetcode.com/problems/split-linked-list-in-parts/) | Split Linked List in Parts | Medium | | Find length n, and use n//k and n%k to determine the size for each part. 
[328](https://leetcode.com/problems/odd-even-linked-list/) | Odd Even Linked List | Medium | | Use odd and even pointers, and a node to save the head of the even list.
[141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle | Medium | [142](https://leetcode.com/problems/linked-list-cycle-ii/) | Slow and fast pointers
[148](https://leetcode.com/problems/sort-list/) | Sort List | Medium |  | Slow and fast pointers + merge sort
[234](https://leetcode.com/problems/palindrome-linked-list/) | Palindrome Linked List | Medium | | Use slow and fast pointers to cut it into halves. Reverse the second half and compare with the first half.