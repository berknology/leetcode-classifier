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


## Stack and Queue
The main characteristics of stack and queue are LIFO (Last In First Out) and FIFO (First In First Out) respectively. 
Stack and queue are frequently used in tree and graph traversal problems, leveraging stack for DFS and queue for BFS. We 
will not list such problems in this list.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[155](https://leetcode.com/problems/min-stack/) | Min Stack | Easy |  | Push a tuple (x, minimum) into stack. 
[232](https://leetcode.com/problems/implement-queue-using-stacks/) | Implement Queue using Stacks | Easy |  | Be careful about the amortized time complexity of each operation. Use two stacks. 
[20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | Easy |  | Be careful about the type of parentheses. Maybe use a dict to simplify code.
[739](https://leetcode.com/problems/daily-temperatures/) | Daily Temperatures | Medium |  | Iterate through array, and pop only when current temp greater than that at the top of the stack. Otherwise, push.
[503](https://leetcode.com/problems/next-greater-element-ii/) | Next Greater Element II | Medium | [496](https://leetcode.com/problems/next-greater-element-i/) | Iterate trough the concatenated array, e.g., given a list `nums`, iterate through `nums+nums`.


## Hash table & set
Hash table/set is one of the most frequently asked data structures in coding interviews. When stuck, try hash table. 
Hash table is also very useful to make time-space trade off. They enable `O(1)` time of searching. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[169](https://leetcode.com/problems/majority-element/) | Majority Element | Easy |  | Hash table
[1](https://leetcode.com/problems/two-sum/) | Two Sum | Easy |  | Iterate through the array and check if `target - nums[i]` is in the hash map.
[217](https://leetcode.com/problems/contains-duplicate/) | Contains Duplicate | Easy |  | Hash set
[594](https://leetcode.com/problems/longest-harmonious-subsequence/) | Longest Harmonious Subsequence | Easy |  | Iterate the array and do `max(ans, count[num] + count[num+1])`.
[128](https://leetcode.com/problems/longest-consecutive-sequence/)  | Longest Consecutive Sequence | Hard/Medium |  | Convert array to hash set. Iterate the array and check if the next element is in the set. 
[560](https://leetcode.com/problems/subarray-sum-equals-k/)  | Subarray Sum Equals K | Medium |  | Use cumulative sum and the two sum problem ([1](https://leetcode.com/problems/two-sum/)) idea.


## Tree
Tree problems are generally traversal problems using recursion. In most of tree traversal problems, the time complexity 
is `O(n)` where `n` is the number of nodes and the space complexity is `O(h)` where `h` is the height of the tree due to 
implicit stack used in recursion. 

It is very important to know concepts such as 'depth', 'height', 'level', 'complete', and 'perfect', 
etc. Moreover, DFS traversal methods such as 'pre-order', 'in-order', and 'post-order', and BFS traversal methods should
be known.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Maximum Depth of Binary Tree  | Easy | [110](https://leetcode.com/problems/balanced-binary-tree/), [111](https://leetcode.com/problems/minimum-depth-of-binary-tree/), [112](https://leetcode.com/problems/path-sum/), [226](https://leetcode.com/problems/invert-binary-tree/), [617](https://leetcode.com/problems/merge-two-binary-trees/), [101](https://leetcode.com/problems/symmetric-tree/), [404](https://leetcode.com/problems/sum-of-left-leaves/), [814](https://leetcode.com/problems/binary-tree-pruning/), [1325](https://leetcode.com/problems/delete-leaves-with-a-given-value/) | Simple recursion.
[508](https://leetcode.com/problems/most-frequent-subtree-sum/) | Most Frequent Subtree Sum | Medium | | Use a hash table to find all path sums, and then find answer from the hash table.
[437](https://leetcode.com/problems/path-sum-iii/) | Path Sum III  | Easy/Medium | [113](https://leetcode.com/problems/path-sum-ii/), [129](https://leetcode.com/problems/sum-root-to-leaf-numbers/), [257](https://leetcode.com/problems/binary-tree-paths/) | Recurse with left and right subtrees respectively. Each recursion return a list of possible path sum values starting with that node. The current node then check with the path sums rooted at the left and right child respectively.
[124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum | Hard | [543](https://leetcode.com/problems/diameter-of-binary-tree/) | Find left sum and right sum, and use both of them to calculate the sum with the current node as the root, and return only one of them.
[572](https://leetcode.com/problems/subtree-of-another-tree/) | Subtree of Another Tree | Easy/Medium | [687](https://leetcode.com/problems/longest-univalue-path/) | Recursively check if `t` is the same tree with a tree rooted at the current node, or if `t` is a subtree rooted at current node's left or right child. 
[102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Binary Tree Level Order Traversal | Medium | [637](https://leetcode.com/problems/average-of-levels-in-binary-tree/), [513](https://leetcode.com/problems/find-bottom-left-tree-value/), [429](https://leetcode.com/problems/n-ary-tree-level-order-traversal/), [1302](https://leetcode.com/problems/deepest-leaves-sum/), [872](https://leetcode.com/problems/leaf-similar-trees/) | Level-order traversal. Use BFS or `defaultdict[list]` to add node into corresponding level. 
[144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Binary Tree Preorder Traversal | Medium | [589](https://leetcode.com/problems/n-ary-tree-preorder-traversal/), [145](https://leetcode.com/problems/binary-tree-postorder-traversal/), [590](https://leetcode.com/problems/n-ary-tree-postorder-traversal/), [94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Recursively is trivial, but iteratively is very complicated. IMO, iteratively in-order traversal is the hardest.
[297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Serialize and Deserialize Binary Tree | Hard | [449](https://leetcode.com/problems/serialize-and-deserialize-bst/) | In the binary tree problem, we need to have "null" indicator to represent null node in the serialized string, while BST does not. BST problem uses pre-order traversal to serialize and deserialize by recursively building trees by checking lower and upper bounds for subtrees. 
[968](https://leetcode.com/problems/binary-tree-cameras/) | Binary Tree Cameras | Hard | [979](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | Bottom up. DFS + greedy. 
