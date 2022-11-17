
# Programming Assignment-Data Analysis and Algorithms 

**PROBLEM STATEMENT :**

• Step 1: Let “n” be the size of an array.

• Step 2: Accept “n” input from keyboard.

• Step 3: Create a Dqueue with insertion of element alternately from front and rear end. 
          For example: if elements in array are: [1, 5, 2, 9, 11] etc..
          If element insertion start with F-R-F-R combination, then values stored will be [1] [1,5], [2,1,5], [2,1,5,9], [11,2,1,5,9]
          Create the code and demonstrate execution with 03 test cases
        
• Step 4: The insertion on Dqueue is carried with certain condition.
                      
         - Condition 1 : If the element present at front is less than the new element, then new element will be inserted in front. [Otherwise]
         - Condition 2 : If element present at rear is less than the new element, then new element will be inserted at rear.
         - Condition 3 : If both condition 1 and condition 2 not satisfied, ignore the element and consider new element.


Find out difference between size of Dqueue and size of array. [The difference will be number of elements in array not inserted in the Dqueue].
Comment on shape of Dqueue : How the elements present in the Dqueue look like [Ascending/Descending/or …].
Suggest a suitable mechanism, such that no element of array is ignored and it is inserted in the Dqueue [modify condition 1 and 2]
