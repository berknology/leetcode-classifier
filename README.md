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
[148](https://leetcode.com/problems/sort-list/) | Sort List | Medium |  | Slow and fast pointers + merge sort
[234](https://leetcode.com/problems/palindrome-linked-list/) | Palindrome Linked List | Medium | | Use slow and fast pointers to cut it into halves. Reverse the second half and compare with the first half.

## Two pointers

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Sum II - Input array is sorted | Easy | [15](https://leetcode.com/problems/3sum/), [16](https://leetcode.com/problems/3sum-closest/) | Head and tail pointers move toward the middle.
[633](https://leetcode.com/problems/sum-of-square-numbers/) | Sum of Square Numbers | Easy | | Head and tail (square root) pointers move toward the middle.
[345](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Reverse Vowels of a String | Easy | | Head and tail pointers move toward the middle.
[917](https://leetcode.com/problems/reverse-only-letters/) | Reverse Only Letters | Easy | | Head and tail pointers move toward the middle.
[125](https://leetcode.com/problems/valid-palindrome/) | Valid Palindrome | Easy | [680](https://leetcode.com/problems/valid-palindrome-ii/) | Head and tail pointers move toward the middle.
[88](https://leetcode.com/problems/merge-sorted-array/) | Merge Sorted Array | Easy | | Two pointers initialized at the ends.
[977](https://leetcode.com/problems/squares-of-a-sorted-array/) | Squares of a Sorted Array | Easy | | Head and tail pointer moves based on certain condition.
[925](https://leetcode.com/problems/long-pressed-name/) | Long Pressed Name | Easy | [986](https://leetcode.com/problems/interval-list-intersections/) | Two pointers, one moves based on certain condition.
[141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle | Medium | [142](https://leetcode.com/problems/linked-list-cycle-ii/) | Slow and fast pointers
[524](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | Longest Word in Dictionary through Deleting | Medium | | Use two pointers to check if one string is a substring of another.
[11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water | Medium | [42](https://leetcode.com/problems/trapping-rain-water/) | Head and tail pointers move toward the middle.


## Binary Search
Please watch this great video tutorial ([part 1](https://www.youtube.com/watch?v=v57lNF2mb_s), 
[part 2](https://www.youtube.com/watch?v=J-IQxfYRTto)) on binary search. It is extremely important to **implement your own 
versions** of binary search algorithms, and make correspondence between your versions and `bisect.bisect()/bisect.bisect_right()` and `bisect.bisect_left()`. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[69](https://leetcode.com/problems/sqrtx/) | Sqrt(x)   | Easy | | 
[35](https://leetcode.com/problems/search-insert-position/) | Search Insert Position | Easy | [704](https://leetcode.com/problems/binary-search/) | `bisect.bisect_left()`
[278](https://leetcode.com/problems/first-bad-version/) | First Bad Version | Easy | [981](https://leetcode.com/problems/time-based-key-value-store/) |
[744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) | Find Smallest Letter Greater Than Target | Easy | | Be careful about the 'wrap around' constraint and duplicates. Use `bisect.bisect()` function.
[875](https://leetcode.com/problems/koko-eating-bananas/) | Koko Eating Bananas | Medium | [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Search by checking validity.
[74](https://leetcode.com/problems/search-a-2d-matrix/) | Search a 2D Matrix | Medium | | Search row and then search column or treat 2D as 1D array.
[34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Find First and Last Position of Element in Sorted Array | Medium | | Use both `bisect.bisect_left()` and `bisect.bisect()`.
[33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Search in Rotated Sorted Array | Medium | [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/), [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), [154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | `left +=1` and `right -= 1` if `nums[left]==nums[mid]==nums[right]`.
[540](https://leetcode.com/problems/single-element-in-a-sorted-array/) | Single Element in a Sorted Array | Medium | | This problem is tricky. If `mid` is even and `nums[mid] == nums[mid+1]`, then `left = mid+2`. If `mid` is odd, then `mid -= 1` and check condition.
[378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Kth Smallest Element in a Sorted Matrix | Medium | | Nested binary searches. Outer one search for the target, and inner one is used to calculate how many elements are less than or equal to the target candidate in each row.
[719](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | Find K-th Smallest Pair Distance | Hard | | Sort array first, and then search by checking validity. 
[4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Median of Two Sorted Arrays | Hard | | Binary search using the shorter list based on condition `nums_short[mid1] <? nums_long[mid2-1]`.


## Binary Search Tree

A special characteristic of BST is that its inorder traversal yields a sorted array. Note that the definitions of BST might 
be different for different problems.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[700](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Search in a Binary Search Tree | Easy | [701](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Recursion and search in half of the subtree each time.
[669](https://leetcode.com/problems/trim-a-binary-search-tree/) | Trim a Binary Search Tree | Easy | | Recursion, and check current node value with lower and upper bounds
[653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Two Sum IV - Input is a BST | Easy | | Use inorder to get a sorted array, and use two pointers. 
[235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Lowest Common Ancestor of a Binary Search Tree | Easy | [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Recursion, and check current node value with the values of the two given nodes
[98](https://leetcode.com/problems/validate-binary-search-tree/) | Validate Binary Search Tree | Medium | [530](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) | Check value with lower and upper bounds for each node. Another way is to leverage inorder traversal.
[230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Kth Smallest Element in a BST | Medium |  | Inorder traversal
[108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Convert Sorted Array to Binary Search Tree | Easy | [109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | Divide array by half and use recursion.
[501](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | Find Mode in Binary Search Tree | Easy |  | Be careful to the BST definition, and use inorder traversal
[450](https://leetcode.com/problems/delete-node-in-a-bst/) | Delete Node in a BST | Medium |  | The deleted node could have no child, 1 child, and 2 children (which is the most tricky part)
[99](https://leetcode.com/problems/recover-binary-search-tree/) | Recover Binary Search Tree | Hard |  | Inorder traversal to find the two nodes and swap them
