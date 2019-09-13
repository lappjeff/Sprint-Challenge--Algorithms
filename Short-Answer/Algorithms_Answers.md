#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n): The algorithm loops over n and increments a based on n. This is a linear process based on n

b)
O(n squared) - O of n squared - for each element n, we will need repeat the while loop until j is equal to n. This require n to essentially be repeated for every n, leading to big O of n squared

c)
O(n): Once again, the recursion depends on n counts of bunnies, so will be a linear process, so big O of n

## Exercise II

#Example for 8 stories

| - 8
| - 7
| - 6
| - 5
| - 4 - Step 1. start at half point - if egg breaks, go to lower half point - else go to upper half point
| - 3
| - 2 - Step 2. start at half point - if egg breaks, breaking_floor is 3 - else breaking floor is current floor, 2
| - 1

#14 floors

| - 14
| - 13
| - 12
| - 11
| - 10 - Step 2. start at half point - if egg breaks, go to lower half point - else go to upper half point
| - 9 -
| - 8 - Step 3. start at half point - if egg breaks, go to lower half-point - else go to upper half point - RESULT FOUND - EGG BROKE HERE - BREAKING_FLOOR IS 8
| - 7 - Step 1. start at half point - if egg breaks, go to lower half point - else go to upper half point
| - 6
| - 5
| - 4
| - 3
| - 2
| - 1

This is essentially binary search - big O is O(n log n) due to results being halved on each iteration
