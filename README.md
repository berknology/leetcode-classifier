# Leetcode problem classifier
This repository aims to categorize and label frequently asked leetcode coding questions into major categories such as 
linked list, binary search, two pointers, and backtracking, etc., and facilitate interviewees and developers to practice 
common programming interview questions. 

Two great online resources have been leveraged to compile the list: 
[Huahua](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) and 
[CyC2018](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E7%9B%AE%E5%BD%95.md).

## Table of Content :page_facing_up:
* Classification of Leetcode Problems

    | ID    | Topic                                                                         | Number of problems | 
    | ----- | ----------------------------------------------------------------------------- | ------------------ |
    | 01    | [Linked List](#linked-list)                                                   | 12                 |
    | 02    | [Two pointers](#two-pointers)                                                 | 18                 |
    | 03    | [Binary Search](#binary-search)                                               | 18                 |
    | 04    | [Binary Search Tree](#binary-search-tree)                                     | 15                 |
    | 05    | [Stack and Queue](#stack-and-queue)                                           | 14                 |
    | 06    | [Hash table and set](#hash-table-and-set)                                     | 6                  |
    | 07    | [Tree](#tree)                                                                 | 35                 |
    | 08    | [Divide and Conquer](#divide-and-conquer)                                     | 6                  |
    | 09    | [Graph](#graph)                                                               | 25                 |
    | 10    | [Greedy Algorithm](#greedy-algorithm)                                         | 10                 |
    | 11    | [Backtracking](#backtracking)                                                 | 22                 |
    | 12    | [Dynamic Programming](#dynamic-programming)                                   | 29                 |
    | 13    | [Miscellaneous (string, array, math, bit manipulation)](#miscellaneous)       | 35                 |
    | 14    | [Advanced Topics (Trie, Topological sorting, Union find)](#advanced-topics)   | 14                 |
    |       |                                                                               | 259 (total)        |

* [Time and Space Complexity of Algorithms](#complexity-of-an-algorithm-chart_with_upwards_trend)    
* [How to Approach a Coding Question](#how-to-approach-a-coding-question-heavy_check_mark)
* [Common Mistakes in a Coding Interview](#common-mistakes-in-a-coding-interview-x)
* [How to Practice and do Mock Interviews](#practice-practice-and-practice)


## Linked List

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


## Two Pointers

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Sum II - Input array is sorted | Easy | [15](https://leetcode.com/problems/3sum/), [16](https://leetcode.com/problems/3sum-closest/) | Head and tail pointers move toward the middle.
[633](https://leetcode.com/problems/sum-of-square-numbers/) | Sum of Square Numbers | Easy | | Head and tail (square root) pointers move toward the middle.
[345](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Reverse Vowels of a String | Easy | | Head and tail pointers move toward the middle.
[917](https://leetcode.com/problems/reverse-only-letters/) | Reverse Only Letters | Easy | | Head and tail pointers move toward the middle.
[125](https://leetcode.com/problems/valid-palindrome/) | Valid Palindrome | Easy | [680](https://leetcode.com/problems/valid-palindrome-ii/) | Head and tail pointers move toward the middle.
[88](https://leetcode.com/problems/merge-sorted-array/) | Merge Sorted Array | Easy | | Two pointers initialized at the ends.
[977](https://leetcode.com/problems/squares-of-a-sorted-array/) | Squares of a Sorted Array | Easy | | Head and tail pointer moves based on certain condition.
[925](https://leetcode.com/problems/long-pressed-name/) | Long Pressed Name | Easy | [56](https://leetcode.com/problems/merge-intervals/), [986](https://leetcode.com/problems/interval-list-intersections/) | Two pointers, one moves based on certain condition.
[141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle | Medium | [142](https://leetcode.com/problems/linked-list-cycle-ii/) | Slow and fast pointers
[524](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | Longest Word in Dictionary through Deleting | Medium | | Use two pointers to check if one string is a substring of another.
[11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water | Medium | [42](https://leetcode.com/problems/trapping-rain-water/) | Head and tail pointers move toward the middle.


## Binary Search
Please watch this [video](https://www.youtube.com/watch?v=P3YID7liBug) for an introductary tutorial and this video 
([part 1](https://www.youtube.com/watch?v=v57lNF2mb_s), [part 2](https://www.youtube.com/watch?v=J-IQxfYRTto)) for a 
great summary of binary search. It is extremely important to **implement your own versions** of binary search 
algorithms, and make correspondence between your versions and `bisect.bisect()/bisect.bisect_right()` and 
`bisect.bisect_left()`. 

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
[378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Kth Smallest Element in a Sorted Matrix | Medium | | Nested binary searches. Outer one search for the target, and inner one is used to calculate how many elements are less than or equal to the target candidate in each row. Another idea is to use min heap.
[719](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) | Find K-th Smallest Pair Distance | Hard | | Sort array first, and then search by checking validity. 
[4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Median of Two Sorted Arrays | Hard | | Binary search using the shorter list based on condition `nums_short[mid1] <? nums_long[mid2-1]`.


## Binary Search Tree

A special characteristic of BST is that its inorder traversal yields a sorted array. Note that the definitions of BST might 
be different for different problems. Moreover, you can recover a binary search tree from its preorder traversal.

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
[1008](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | Construct Binary Search Tree from Preorder Traversal | Medium |  | Use recursion and for each node, update the lower and upper values for its children.
[99](https://leetcode.com/problems/recover-binary-search-tree/) | Recover Binary Search Tree | Hard |  | Inorder traversal to find the two nodes and swap them


## Stack and Queue
The main characteristics of stack and queue are LIFO (Last In First Out) and FIFO (First In First Out) respectively. 
Stack and queue are frequently used in tree and graph traversal problems, leveraging stack for DFS and queue for BFS. We 
will not list such problems in this list.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[155](https://leetcode.com/problems/min-stack/) | Min Stack | Easy |  | Push a tuple (x, minimum) into stack. 
[232](https://leetcode.com/problems/implement-queue-using-stacks/) | Implement Queue using Stacks | Easy |  | Be careful about the amortized time complexity of each operation. Use two stacks. 
[1047](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | Remove All Adjacent Duplicates In String | Easy | [1209](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Use stack.
[20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses | Easy | [921](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/), [1249](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Be careful about the type of parentheses. Maybe use a dict to simplify code.
[739](https://leetcode.com/problems/daily-temperatures/) | Daily Temperatures | Medium | [402](https://leetcode.com/problems/remove-k-digits/) | Iterate through array, and pop util current temp smaller than or equal to temp at the top of the stack. Otherwise, push.
[503](https://leetcode.com/problems/next-greater-element-ii/) | Next Greater Element II | Medium | [496](https://leetcode.com/problems/next-greater-element-i/) | Iterate trough the concatenated array, e.g., given a list `nums`, iterate through `nums+nums`.
[581](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Shortest Unsorted Continuous Subarray | Medium |  | Use monotone stack.
[239](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window Maximum | Hard | [1438](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | Use monotone queue.


## Hash table and set
Hash table/set is one of the most frequently asked data structures in coding interviews. When stuck, try hash table. 
Hash table and hash set are also very useful to make time-space trade off. They enable `O(1)` time of searching. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[169](https://leetcode.com/problems/majority-element/) | Majority Element | Easy |  | Hash table
[1](https://leetcode.com/problems/two-sum/) | Two Sum | Easy |  | Iterate through the array and check if `target - nums[i]` is in the hash map.
[217](https://leetcode.com/problems/contains-duplicate/) | Contains Duplicate | Easy |  | Hash set
[594](https://leetcode.com/problems/longest-harmonious-subsequence/) | Longest Harmonious Subsequence | Easy |  | Iterate the array and do `max(ans, count[num] + count[num+1])`.
[128](https://leetcode.com/problems/longest-consecutive-sequence/)  | Longest Consecutive Sequence | Hard/Medium |  | Convert array to hash set. Iterate the array and check if the next element is in the set. 
[560](https://leetcode.com/problems/subarray-sum-equals-k/)  | Subarray Sum Equals K | Medium |  | Use cumulative sum and the two sum problem ([1](https://leetcode.com/problems/two-sum/)) idea.


## Tree
Most of tree problems are traversal problems. Traversal algorithms such as DFS including 'pre-order', 
'in-order', and 'post-order', and BFS or level order traversal are extremely important. Generally speaking, the time complexity of DFS algorithm 
is `O(n)` where `n` is the number of nodes and the space complexity is `O(h)` where `h` is the height of the tree due to 
implicit stack used in recursion. Additionally, BFS problems generally have complexity of `O(n)` in time and `O(w)` in
space, where `w` is the maximum width of a tree. Moreover, it is very important to know concepts such as 'depth', 
'height', 'level', 'complete tree', and 'perfect tree', etc. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Maximum Depth of Binary Tree  | Easy | [110](https://leetcode.com/problems/balanced-binary-tree/), [111](https://leetcode.com/problems/minimum-depth-of-binary-tree/), [112](https://leetcode.com/problems/path-sum/), [226](https://leetcode.com/problems/invert-binary-tree/), [617](https://leetcode.com/problems/merge-two-binary-trees/), [101](https://leetcode.com/problems/symmetric-tree/), [404](https://leetcode.com/problems/sum-of-left-leaves/), [814](https://leetcode.com/problems/binary-tree-pruning/), [1325](https://leetcode.com/problems/delete-leaves-with-a-given-value/) | Simple recursion.
[508](https://leetcode.com/problems/most-frequent-subtree-sum/) | Most Frequent Subtree Sum | Medium | | Use a hash table to find all path sums, and then find answer from the hash table.
[437](https://leetcode.com/problems/path-sum-iii/) | Path Sum III  | Easy/Medium | [113](https://leetcode.com/problems/path-sum-ii/), [129](https://leetcode.com/problems/sum-root-to-leaf-numbers/), [257](https://leetcode.com/problems/binary-tree-paths/) | For Problem 437, use hash_table + DFS to achieve linear time complexity, similar to two sum problem. Check out similar problem [560](https://leetcode.com/problems/subarray-sum-equals-k/).
[124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum | Hard/Medium | [543](https://leetcode.com/problems/diameter-of-binary-tree/) | Find left sum and right sum, and use both of them to calculate the sum with the current node as the root, and return only one of them.
[572](https://leetcode.com/problems/subtree-of-another-tree/) | Subtree of Another Tree | Easy/Medium | [687](https://leetcode.com/problems/longest-univalue-path/) | Recursively check if `t` is the same tree with a tree rooted at the current node, or if `t` is a subtree rooted at current node's left or right child. Problem 687 can have linear time complexity by calculating the longest path by using left and right paths and only returning the max of left and right paths. 
[102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Binary Tree Level Order Traversal | Medium | [637](https://leetcode.com/problems/average-of-levels-in-binary-tree/), [513](https://leetcode.com/problems/find-bottom-left-tree-value/), [429](https://leetcode.com/problems/n-ary-tree-level-order-traversal/), [1302](https://leetcode.com/problems/deepest-leaves-sum/) | Level-order traversal. Use BFS or `defaultdict[list]` to add node into corresponding level. 
[144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Binary Tree Preorder Traversal | Medium | [589](https://leetcode.com/problems/n-ary-tree-preorder-traversal/), [145](https://leetcode.com/problems/binary-tree-postorder-traversal/), [590](https://leetcode.com/problems/n-ary-tree-postorder-traversal/), [94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Recursively is trivial, but iteratively is very complicated. IMO, iteratively in-order traversal is the hardest.
[297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Serialize and Deserialize Binary Tree | Hard | [449](https://leetcode.com/problems/serialize-and-deserialize-bst/), [106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/), [105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | In the binary tree problem, we need to have "null" indicator to represent null node in the serialized string, while BST does not. BST problem uses pre-order traversal to serialize and deserialize by recursively building trees by checking lower and upper bounds for subtrees. 
[968](https://leetcode.com/problems/binary-tree-cameras/) | Binary Tree Cameras | Hard | [979](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | Bottom up. DFS + greedy. 


## Divide and Conquer

Divide and conquer approach refers to decomposing a big problem into smaller problems, then combine the results obtained 
from these smaller problems which are solved recursively. When stuck, think about the base case (the smallest problem), 
and see if we can build up a solution recursively from there. Merge sort and quick sort algorithms both leverage divide 
and conquer approach.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[912](https://leetcode.com/problems/sort-an-array/) | Sort an Array | Medium | [215](https://leetcode.com/problems/kth-largest-element-in-an-array/), [148](https://leetcode.com/problems/sort-list/) | Merge/quick sort, quick select
[241](https://leetcode.com/problems/different-ways-to-add-parentheses/) | Different Ways to Add Parentheses | Medium |  | Divide the string into two parts when encountering an operator, and recurse on each part and combine results.
[95](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Unique Binary Search Trees II | Medium |  | Iterate through the possible values ("array"), and use the current as root and pivot, and divide the "array" into two parts, and find all possible solutions using the recursion results obtained by using the aforementioned two parts.
[315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Count of Smaller Numbers After Self | Hard |  | Merge sort. The key is gradually updating the answer in the merge step.


## Graph

Graph problems are generalization of tree problems. DFS and BFS traversals are extremely important algorithms in graph 
problems. One key difference between graph and tree problems is that graph traversal requires a `visited` variable to 
memorize nodes that have been visited before. Moreover, use DFS to solve connected problems and BFS to solve shortest
path problems. The complexity of graph traversals is generally `O(V+E)` in time and `O(V)` in space, where `V` is the 
number of vertices/nodes and `E` is the number of edges. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[997](https://leetcode.com/problems/find-the-town-judge/) | Find the Town Judge | Easy |  | Use both in-degrees and out-degrees.
[133](https://leetcode.com/problems/clone-graph/) | Clone Graph | Medium | [138](https://leetcode.com/problems/copy-list-with-random-pointer/) | Use hash table and DFS. The hash table also serves as the `visited`.
[200](https://leetcode.com/problems/number-of-islands/) | Number of Islands | Medium | [547](https://leetcode.com/problems/friend-circles/), [695](https://leetcode.com/problems/max-area-of-island/), [733](https://leetcode.com/problems/flood-fill/), [841](https://leetcode.com/problems/keys-and-rooms/), [827](https://leetcode.com/problems/making-a-large-island/), [1202](https://leetcode.com/problems/smallest-string-with-swaps/), [130](https://leetcode.com/problems/surrounded-regions/), [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | It is a connected components problem, use DFS. Given grid might be able to be used as `visited`.
[1162](https://leetcode.com/problems/as-far-from-land-as-possible/) | As Far from Land as Possible | Medium | [433](https://leetcode.com/problems/minimum-genetic-mutation/), [863](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/), [1129](https://leetcode.com/problems/shortest-path-with-alternating-colors/), [1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/), [279](https://leetcode.com/problems/perfect-squares/), [127](https://leetcode.com/problems/word-ladder/), [399](https://leetcode.com/problems/evaluate-division/), [542](https://leetcode.com/problems/01-matrix/), [934](https://leetcode.com/problems/shortest-bridge/) | It is a shortest/longest path problem, use BFS. 
[785](https://leetcode.com/problems/is-graph-bipartite/) | Is Graph Bipartite? | Medium | [886](https://leetcode.com/problems/possible-bipartition/), [1042](https://leetcode.com/problems/flower-planting-with-no-adjacent/) | Graph coloring


## Greedy Algorithm

Greedy algorithm is a simple and heuristic algorithm that follows the problem-solving heuristic of making the locally 
optimal choice which **might but not necessarily** end up a global optimal solution. It builds up a solution piece by piece, always choosing the 
next piece that offers the most obvious and immediate benefit. Sometimes, we solved a problem using our instinct without 
even realizing it is a greedy algorithm problem.

The difference between greedy algorithm and dynamic programming (DP) is subtle. Detailed comparison is highlighted in 
this [article](https://www.geeksforgeeks.org/greedy-approach-vs-dynamic-programming/). In general, greedy algorithm is 
simpler and myopic, and make heuristic decision based on locally optimal choice. DP is generally harder, and makes 
decision at each step considering current problem and solution to previously solved sub-problems. 

In practice, a problem might be able to solved in both ways, as pointed out in
this [article](https://medium.com/algorithms-and-leetcode/greedy-algorithm-explained-using-leetcode-problems-80d6fee071c4) 
"beneath every greedy algorithm, there is almost always a more cumbersome dynamic programming solution".

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[455](https://leetcode.com/problems/assign-cookies/) | Assign Cookies | Easy |  | **Have kids and you will know** :joy:
[605](https://leetcode.com/problems/can-place-flowers/) | Can Place Flowers | Easy |  | Pad each side of `flowerbed` by `0`, and iteratively check if we can place flower by `flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0`.
[121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Best Time to Buy and Sell Stock | Easy | [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Keep track of the min price. You might have solved the problem without realizing it is a greedy algorithm problem. Greedy algorithm allows you to follow your instinct. 
[53](https://leetcode.com/problems/maximum-subarray/) | Maximum Subarray | Easy/Medium | [152](https://leetcode.com/problems/maximum-product-subarray/) | Repeatedly check current sum `cur_sum = max(cur_sum + num, num)`. There is a blur boundary between greedy algorithm and DP for this problem.
[435](https://leetcode.com/problems/non-overlapping-intervals/) | Non-overlapping Intervals | Medium | [452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Sort the intervals by the end point of each interval.
[763](https://leetcode.com/problems/partition-labels/) | Partition Labels | Medium |  | Use a hash table to keep track of the last time (largest index) a letter appeared.
[406](https://leetcode.com/problems/queue-reconstruction-by-height/) | Queue Reconstruction by Height | Medium |  | Sort the list by height `h` in descending order and number of people `k` in ascending order. Construct a queue `queue` by iteratively `queue.insert(k, h)` for each pair in the sorted list. 

## Backtracking

Backtracking is an exhaustive search algorithm for solving combination, permutation, subset, and constraint satisfaction 
problems. It solves a problem recursively by trying to build a solution incrementally while removing solutions that fail to satisfy the constraints of 
the problem. The time complexity of backtracking algorithm is generally large, e.g., at least `C(n, k)` for combination 
problem and at least `P(n, k)` for permutation problem 
[reference](https://betterexplained.com/articles/easy-permutations-and-combinations/). This 
[video](https://zxi.mytechroad.com/blog/searching/leetcode-78-subsets/) gives a great tutorial on how to implement 
backtracking algorithm for combination and permutation problems.

There are three key pillars in backtracking algorithms: (1) the base case, exit condition or the goal to achieve, (2) 
the choices to make to go to the next building step, and (3) pruning that discards solutions that fail to satisfy the
constraints of the problem. A great high-level introduction of backtracking algorithm can be found 
[here](https://www.youtube.com/watch?v=Zq4upTEaQyM).

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Letter Combinations of a Phone Number | Medium | [77](https://leetcode.com/problems/combinations/), [39](https://leetcode.com/problems/combination-sum/), [40](https://leetcode.com/problems/combination-sum-ii/), [216](https://leetcode.com/problems/combination-sum-iii/) | Combinations
[46](https://leetcode.com/problems/permutations/) | Permutations | Medium | [47](https://leetcode.com/problems/permutations-ii/), [784](https://leetcode.com/problems/letter-case-permutation/), [996](https://leetcode.com/problems/number-of-squareful-arrays/) | Permutations
[78](https://leetcode.com/problems/subsets/) | Subsets | Medium | [90](https://leetcode.com/problems/subsets-ii/) | Subsets
[79](https://leetcode.com/problems/word-search/) | Word Search | Medium | [212](https://leetcode.com/problems/word-search-ii/) | DFS for problem 79 and DFS + Trie for Problem 212.
[22](https://leetcode.com/problems/generate-parentheses/) | Generate Parentheses | Medium | [301](https://leetcode.com/problems/remove-invalid-parentheses/) | Add `(` whenever the number of `(` is smaller than `n`, and add `)` whenever the number of `)` is smaller than the number of open parentheses.  
[131](https://leetcode.com/problems/palindrome-partitioning/) | Palindrome Partitioning | Medium | [93](https://leetcode.com/problems/restore-ip-addresses/), [698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/), [842](https://leetcode.com/problems/split-array-into-fibonacci-sequence/), [282](https://leetcode.com/problems/expression-add-operators/) | Partition
[37](https://leetcode.com/problems/sudoku-solver/) | Sudoku Solver | Hard | [51](https://leetcode.com/problems/n-queens/) | 


## Dynamic Programming

Dynamic programming (DP) is an algorithm to solve problems by breaking it down into simpler and smaller subproblems 
and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solutions to these 
subproblems. DP algorithm is similar to Greedy and Divide & Conquer algorithms in breaking down the problem into smaller 
subproblems. However, these subproblems are not solved independently, and results of these smaller subproblems are 
remembered and used for similar and **overlapping** subproblems. 

Please watch this [video](https://www.youtube.com/watch?v=vYquumk4nWw&t=34s) for a brief introductory tutorial to DP, 
and this [video](https://www.youtube.com/watch?v=3mY5W0yojtA) for a great summary of DP algorithms. DP has two forms: 
top-down (recursion + memoization) and iterative bottom-up. The main goals of DP are reducing time complexity of a 
problem solved by using recursion from exponential to lower ones such as linear or finding counting and global optimal 
solution to a problem. The key to solve a DP problem is to find an iterative or recursive formula.  

Asking DP problems in coding interviews has been a little bit controversial. It is highly likely that an interviewee 
either solves the problem in several minutes or gets stuck for the whole coding session. Additionally, a lot of DP 
problems are really involved and complicated. However, DP is one of the most important algorithms in practice, and 
proven to be very useful to solve optimal control/decision problems.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[70](https://leetcode.com/problems/climbing-stairs/) | Climbing Stairs | Easy | [746](https://leetcode.com/problems/min-cost-climbing-stairs/), [1137](https://leetcode.com/problems/n-th-tribonacci-number/) | Simple DP
[198](https://leetcode.com/problems/house-robber/) | House Robber | Easy | [213](https://leetcode.com/problems/house-robber-ii/), [337](https://leetcode.com/problems/house-robber-iii/), [740](https://leetcode.com/problems/delete-and-earn/) | For Problem 213, try twice, one without the first house and one without the last house. Then find the maximum of them. One way to solve Problem 740 is to convert it into a house robber problem.
[1218](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) | Longest Arithmetic Subsequence of Given Difference | Medium | [413](https://leetcode.com/problems/arithmetic-slices/), [300](https://leetcode.com/problems/longest-increasing-subsequence/), [646](https://leetcode.com/problems/maximum-length-of-pair-chain/), [1143](https://leetcode.com/problems/longest-common-subsequence/) | For Problem 1218, use Hash table + DP
[416](https://leetcode.com/problems/partition-equal-subset-sum/) | Partition Equal Subset Sum | Medium | [494](https://leetcode.com/problems/target-sum/), [474](https://leetcode.com/problems/ones-and-zeroes/), [322](https://leetcode.com/problems/coin-change/), [518](https://leetcode.com/problems/coin-change-2/), [139](https://leetcode.com/problems/word-break/), [377](https://leetcode.com/problems/combination-sum-iv/) | Knapsack problem.
[62](https://leetcode.com/problems/unique-paths/) | Unique Paths | Medium | [63](https://leetcode.com/problems/unique-paths-ii/), [64](https://leetcode.com/problems/minimum-path-sum/), [120](https://leetcode.com/problems/triangle/), [931](https://leetcode.com/problems/minimum-falling-path-sum/) | DP in 2-dimensional space. Deal with the boundaries first for Problems 62-64. 
[85](https://leetcode.com/problems/maximal-rectangle/) | Maximal Rectangle | Hard/Medium | [221](https://leetcode.com/problems/maximal-square/), [1277](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Leverage the solution to Problem [84](https://leetcode.com/problems/largest-rectangle-in-histogram/) using stack for Problems 85 and 221.
[309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Best Time to Buy and Sell Stock with Cooldown | Medium/Hard | [801](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) | Multi-state (rest, sold, hold) DP


## Miscellaneous

#### String

Some of the most famous string problems include anagram, palindrome, substring, and rotation. If you are not familiar 
with the definition of anagram or palindrome, it might be a good idea to understand these concepts before the interview. 

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[242](https://leetcode.com/problems/valid-anagram/) | Valid Anagram | Easy | [438](https://leetcode.com/problems/find-all-anagrams-in-a-string/), [205](https://leetcode.com/problems/isomorphic-strings/) | Hash table
[409](https://leetcode.com/problems/longest-palindrome/) | Longest Palindrome | Easy |  | Hash table
[9](https://leetcode.com/problems/palindrome-number/) | Palindrome Number | Easy |  | Convert to string or reverse a number.
[3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | Medium |  | Hash set
[647](https://leetcode.com/problems/palindromic-substrings/) | Palindromic Substrings | Medium | [5](https://leetcode.com/problems/longest-palindromic-substring/) | Expand string centered at each letter
[796](https://leetcode.com/problems/rotate-string/) | Rotate String | Easy |  | A naive solution is check if `B in A+A`. 
[151](https://leetcode.com/problems/reverse-words-in-a-string/) | Reverse Words in a String | Medium |  | Reverse each word and reverse the string.

#### Array

Index plays an important role in array problems. In some problems, values in array are used as indices as well. 
Quick select is a great algorithm to find the k-th smallest element in an array in `O(n)` time, which outperforms 
heap/priority queue and sorting algorithms which have time complexities of `O(nlog(k))` and `O(nlog(n))` respectively.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[566](https://leetcode.com/problems/reshape-the-matrix/) | Reshape the Matrix | Easy |  | Have a counter `cnt`, and the row index will be `cnt//c` and the column index will be `cnt%c`.
[645](https://leetcode.com/problems/set-mismatch/) | Set Mismatch | Easy |  | Hash table
[697](https://leetcode.com/problems/degree-of-an-array/) | Degree of an Array | Easy/Medium |  | Hash table.
[422](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Find All Duplicates in an Array | Medium |  | Leverage the input list, and use negation.
[565](https://leetcode.com/problems/array-nesting/) | Array Nesting | Medium |  | Use input as visited array.
[769](https://leetcode.com/problems/max-chunks-to-make-sorted/) | Max Chunks To Make Sorted | Medium |  | Iterate through array. If current max is smaller than or equal to current index, the the number of chunks increases by 1.
[462](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) | Minimum Moves to Equal Array Elements II | Medium | [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Quick select algorithm.
[287](https://leetcode.com/problems/find-the-duplicate-number/) | Find the Duplicate Number | Medium |  | Slow and fast pointers + cycle detection.

#### Math

Typical math problems include finding prime numbers, gcd (greatest common divisor), lcm (least common multiple), 
converting base, and check if a number is a power of 2/3/4, etc.

There are a couple of tips related to gcd and lcm.
* find gcd, `def gcd(a, b): return a if b == 0 else gcd(b, a%b)`, time complexity `O(log(min(a, b)))`.
* find lcm, `def lcm(a, b): return a*b//gcd(a, b)`.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[204](https://leetcode.com/problems/count-primes/) | Count Primes | Easy |  | Sieve of Eratosthenes
[504](https://leetcode.com/problems/base-7/) | Base 7 | Easy | [405](https://leetcode.com/problems/convert-a-number-to-hexadecimal/), [168](https://leetcode.com/problems/excel-sheet-column-title/) | Repeatedly use `digit = n%base` and `n = n//base` where integer `base` is the target base.
[67](https://leetcode.com/problems/add-binary/) | Add Binary | Easy | [415](https://leetcode.com/problems/add-strings/) | 
[367](https://leetcode.com/problems/valid-perfect-square/) | Valid Perfect Square | Easy |  | Binary search with time complexity `O(log(n))` or `1+3+...+(2n-1) = n*n` with time complexity `O(sqrt(n))`.
[326](https://leetcode.com/problems/power-of-three/) | Power of Three | Easy | [342](https://leetcode.com/problems/power-of-four/) | 
[628](https://leetcode.com/problems/maximum-product-of-three-numbers/) | Maximum Product of Three Numbers | easy |  | The max product is `max(max1*max2*max3, max1*min1*min2))`.
[238](https://leetcode.com/problems/product-of-array-except-self/) | Product of Array Except Self | Medium |  | Leverage the output array to have `O(1)` space and do `cummulative product` from left to right and right to left. 

#### Bit manipulation

Bit manipulation problems can be very tricky. If you don't know the concept, it is highly likely you will not be able to 
solve the problem, and there is generally no workaround by using other algorithms. 

The fundamental operations of bit manipulation are:
```
x ^ 0s = x      x & 0s = 0      x | 0s = x
x ^ 1s = ~x     x & 1s = x      x | 1s = 1s
x ^ x = 0       x & x = x       x | x = x
```
where `0s` and `1s` represent a sequence of 0s and 1s respectively. 

There are a few tips that might help solve bit manipulation problems.
* Leverage `x ^ 0s = x` and `x ^ x = 0`, we can remove or find duplicate number, e.g., `1^1^2 = 2`.
* `x&(x-1)` will remove the last 1 in the binary representation of `x`, and `x&(-x)` will get the last 1 in the binary representation.
* The binary representation of `-k` as a n-bit number is `concat(1, bin(2^(n-1)-k))` where `bin` denotes binary representation.
* In Python converting an integer represented in any base to a binary number as a **string** can be done using `bin(num)`. Be careful when `num` is negative.
* `x << n` will multiply `x` by 2^n, and `x >> n` will divide `x` by 2^n.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[136](https://leetcode.com/problems/single-number/) | Single Number | Easy | [268](https://leetcode.com/problems/missing-number/), [260](https://leetcode.com/problems/single-number-iii/) | XOR
[318](https://leetcode.com/problems/maximum-product-of-word-lengths/) | Maximum Product of Word Lengths | Medium |  |  Use a mask/filter to indicate which letter has appeared for each word.
[338](https://leetcode.com/problems/counting-bits/) | Counting Bits | Medium |  | DP with `dp[i] = dp[i&(i-1)] + 1`.


## Advanced Topics

#### Trie

`Trie` is a special `tree` data structure that stores the letters of a string in an ordered manner. It enables fast 
search of a string by traversing down a branch path of the tree. It behaves as a dictionary, we can navigate to the next 
letter from the current letter. Each Trie node has a `children` variable and a `is_word` variable. The `children` 
variable is generally a hash table with letter as key and Trie node as the value, and the `is_word` variable is boolean.
There are three common methods for Trie data structure, `insert`, `search`, and `start_with`. The difference between the
`search` and `start_with` functions is the `is_word` flag is true or not after iterating through the searched string. 
When encountering key words such as `prefix`, `dictionary`, `search`, and `word`, etc. in a coding problem, think about 
the Trie data structure.

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[208](https://leetcode.com/problems/implement-trie-prefix-tree/) | Implement Trie (Prefix Tree) | Medium | [677](https://leetcode.com/problems/map-sum-pairs/), [648](https://leetcode.com/problems/replace-words/), [676](https://leetcode.com/problems/implement-magic-dictionary/), [720](https://leetcode.com/problems/longest-word-in-dictionary/), [211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Defining a `TrieNode` class whose children is a `defaultdict(TrieNode)` type variable will facilitate coding.

#### Topological Sorting

Topological sort is only feasible for DAG (directed acyclic graph). One way to implement topological sorting is use BFS.
First add nodes with in-degrees/out-degrees equal to 0 to queue. Then pop a node, traverse to its neighbors, and 
subtract 1 from the in-degrees/out-degrees of the neighbors. If the current in-degree/out-degree of a neighbor is equal 
to 0, add it to the queue.  

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[207](https://leetcode.com/problems/course-schedule/) | Course Schedule | Medium | [210](https://leetcode.com/problems/course-schedule-ii/), [802](https://leetcode.com/problems/find-eventual-safe-states/) | Build graph and in-degree/out-degree list, then do topological sort.

#### Union Find

Union Find algorithm or disjoint-set data structure aims to find if two nodes are in the same set in amortized `O(1)` 
time. There are two operations in the `UnionFind` class: `find` and `union`. To enable amortized `O(1)` time of `find`, 
two optimizations need to be done for the `UnionFind` class: path compression and union by rank.

A python implementation of the disjoint set data structure is given below.
```python
class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]
    
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        return True
```

**In a coding interview, if you are asked a Union Find problem and you are not familiar with this algorithm, try other 
algorithms such as DFS or BFS, and it is highly likely that you will be still able to solve the problem.**

 ID | Problem Name | Difficulty | Similar problems | Main Idea
--- | ------------ | ---------- | ---------------- | ----------------------------------------------------------
[684](https://leetcode.com/problems/redundant-connection/) | Redundant Connection | Medium | [1319](https://leetcode.com/problems/number-of-operations-to-make-network-connected/), [990](https://leetcode.com/problems/satisfiability-of-equality-equations/), [721](https://leetcode.com/problems/accounts-merge/), [685](https://leetcode.com/problems/redundant-connection-ii/) | 


## Complexity of an Algorithm :chart_with_upwards_trend:

Algorithm complexity is a measure of the amount of time and/or space required by an algorithm as a function of the input 
size. The time complexity is the computational complexity that describes the amount of time it takes to run an algorithm 
and the space complexity is amount of memory space required by the algorithm. 

The following picture depicts the Big O complexity of an algorithm as a function of input size `n`.

<div align="center">
    <img src="/images/big_o_complexity.jpg" alt="Big O Complexity"><br>
    <a href="https://www.bigocheatsheet.com/" target="_blank">
        Copyright of picture belongs to www.bigocheatsheet.com.
    </a>
</div>

We observe from the above picture that when `n` is large, 
```
O(n!) > O(2^n) > O(n^2) > O(nlog(n)) > O(n) > O(log(n)) > O(1)
``` 
which indicates the order of complexity in decreasing order as: 
factorial, exponential, polynomial, linearithmic, linear, logarithmic, and constant. 

The following table summarizes the complexity of common algorithms.

| Algorithm         | Best Time    | Average Time | Worst Time   | Worst Space | Comments                                  | 
| ----------------- | ------------ | ------------ | -----------  | ----------- | ----------------------------------------- |
| Quick sort        | `O(nlog(n))` | `O(nlog(n))` | `O(n^2)`     | `O(n)`      | [Unstable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)                                  |
| Merge sort        | `O(nlog(n))` | `O(nlog(n))` | `O(nlog(n))` | `O(n)`      | [Stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)                                    |
| Tim sort          | `O(n)`       | `O(nlog(n))` | `O(nlog(n))` | `O(n)`      | Stable. Python uses Tim sort.             |
| Heap sort         | `O(nlog(n))` | `O(nlog(n))` | `O(nlog(n))` | `O(1)`      | Unstable                                  |
| Binary search     |              |              | `O(log(n))`  | `O(1)`      |                                           |
| Tree DFS          |              |              | `O(n)`       | `O(h)`      | `h` is the height of the tree             |
| Tree BFS          |              |              | `O(n)`       | `O(w)`      | `w` is the maximum width of the tree      |
| Graph DFS         |              |              | `O(V+E)`     | `O(V)`      | `V` and `E` are numbers of vertices and edges respectively |
| Graph BFS         |              |              | `O(V+E)`     | `O(V)`      |                                           |
| Permutation       |              |              | `O(n!)`      | `O(n)`      | Permutation (backtracking)                |
| Combination       |              |              | `O(2^n)`     | `O(n)`      | Combination (backtracking)                |

Many leetcode questions not only present the problem description, but also give the constraint of input size. It is 
interesting to see that we can infer the time complexity of the algorithm we are supposed to develop based on the input 
size. The following picture shows the time complexity versus the input size. For example, if the input size is less than 
10, then this problem is probably a backtracking (permutation) problem. Please refer to this great 
[video](https://zxi.mytechroad.com/blog/sp/input-size-v-s-time-complexity/) for details. However, such information might 
not be available in a coding interview. But it doesn't hurt to ask.

<div align="center">
    <img src="/images/time_complexity_vs_input_size.jpg" alt="Time Complexity versus Input Size"><br>
    <a href="https://zxi.mytechroad.com/blog/sp/input-size-v-s-time-complexity/" target="_blank">
        Copyright of picture belongs to Huahua.
    </a>
</div>


## How to Approach a Coding Question :heavy_check_mark:

I recommend to get a copy of [Gayle McDowell's](http://www.gayle.com/) coding interview preparation book 
[Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850), 
and follow the recommend **seven steps** (illustrated below) to answer any coding questions.

1. **Listen carefully to the problem description and ask clarifying questions**

    Don't miss any important information/keyword which might help you find a(n) (optimal) solution. Most of the time, 
    the interviewer will type the problem description into the collaborative coding environment. Do ask questions to 
    clarify all your doubts such as input, output, edge cases, and constraints, etc. Even the problem description is 
    crystal clear to you or you have solved this problem before, it is still helpful to repeat the problem to the 
    interviewer in a different way to make sure you really understand it and engage the interviewer.

2. **Present a nontrivial example if it is not given in the problem description**

    Sometimes, the interviewer will give you an example input and an expected output. Be careful, the given example 
    might be too trivial or just an edge case or purposely misses some edge cases or information that might help you 
    develop a solution to the problem. In this case, you might want to clarify with your interviewer by presenting a 
    typical and non-trivial example, and explain the expected output. This step might be consolidated with the first 
    step depending on the situation.

3. **Describe a brute force solution ASAP**
    
    Do not dive into coding immediately. First give an intuitive and naive solution and explain 
    the time and space complexity, then engage/discuss with the interviewer to see if you can optimize it. Note that you 
    need to **lead** the conversation. The motivation for this step is that it is the natural way to solve a problem 
    that you have never seen before. The interviewer cares more about how you get to the optimal solution than the 
    solution itself. If you rush to present an optimal solution immediately without any explanation, it makes the 
    impression that you have solved this problem before, and you are copying what you have memorized. Note that 
    companies try to hire developers with great problem-solving skills instead of people with good memory.
    
4. **Optimize your solution to get an optimal one**
    
    This is the most important step. You need to lead the discussion to explain why you use certain data structure 
    and/or algorithm to optimize your brute force solution, and how you get there. Thinking out loud and explaining your 
    thought process is extremely important in the coding interview process. Leverage the BUD (bottleneck, unnecessary, 
    duplicated) framework and other tips in the 
    [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850)
    book. This is the part where all your practice and hard work pays off. Without sufficient practice and summarization 
    of different types and categories of coding questions, it will be challenging to come up an optimal solution to a 
    problem, especially to a problem you have never seen before.
    
5. **Walk through your optimal solution**

    Now you have an optimal solution and have explained how you get there, walk through the optimal solution with your 
    interviewer to make sure you and the interviewer understand everything. 
    
6. **Implement your algorithm and solution**

    Finally, we arrive the step of coding. **Imagine you dived into coding immediately after your interviewer gave you 
    the problem description, how many important steps you have missed!** Remember to write clean code and modularize 
    your code with standard variable and function names. [PEP 8](https://www.python.org/dev/peps/pep-0008/) and 
    [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) are great guidelines to write clean, 
    readable, and production-quality code for Python and C++ respectively. 
    
7. **Test your code**

    It is super important to initiate testing your code before your interviewer asks you to do so. First eye-balling 
    your code to see if there are any conceptual bugs such as keyword errors, incorrect indentations, inconsistent 
    variable or function names, missing colons, and indexing errors, etc. Then use small cases, special cases, and edge 
    cases to test your code. Do not panic if there are bugs. Everybody makes mistakes, and that is why we do the 
    testing. Fix the bugs carefully and gracefully.

**In a typical coding interview session, we generally need to solve one hard-level or two medium-level Leetcode 
questions in 45 minutes, including brief self-introductions and questions, etc. Therefore, use your time smartly and do 
not dogmatically follow the above 7 steps. Rather, be flexible and agile.**

<div align="center">
    <img src="/images/7steps.png" alt="Cracking the Coding Interview"><br>
    <a href="https://www.careerup.com/" target="_blank">
        Copyright of picture belongs to Gayle McDowell.
    </a>
</div>


## Common Mistakes in a Coding Interview :x:

* Did not ask clarifying questions or confirm/repeat the question
* Did not explain your idea clearly or walk through your solution
* Did not listen to or take interviewer's suggestions/hints
* Dived into coding immediately
* Did not actively engage or interact/discuss with the interviewer
* Communication was poor or defensive
* Did not test your algorithm
* Poor naming of variables or functions
* Code had bugs or missed edge cases
* Code was not clean or modularized
* Did not respect the interviewer or was too arrogant


## Practice, Practice, and Practice
Now you have mastered the skills and tips to crack the coding interviews, it is time to practice them in mock interviews 
before you take a real job interview. This step is extremely valuable since coding under pressure is very different and 
you need practice to be at your best. 

You can start by pairing a coding buddy and give each other a medium-level question to solve in 25 minutes, and give 
feedback at the end. [CoderPad](https://coderpad.io/) is a great online collaborative coding environment for mock 
interviews. After that, you might want to leverage [Pramp.com](https://www.pramp.com/invt/M6olAymmybCmyO9mZLLV) 
and [interviewing.io](https://interviewing.io/) to practice mock interviews with anonymous people, which will give you 
the "real" interview feeling. 
