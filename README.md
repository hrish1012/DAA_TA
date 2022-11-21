
# Programming Assignment-Data Analysis and Algorithms 

**PROBLEM STATEMENT :**

• Step 1: Let “n” be the size of an array.

• Step 2: Accept “n” input from keyboard.

• Step 3: Create a Dqueue with insertion of element alternately from front and rear end. 
          
  -For example: if elements in array are: [1, 5, 2, 9, 11] etc..
  -If element insertion start with F-R-F-R combination, then values stored will be [1] [1,5], [2,1,5], [2,1,5,9], [11,2,1,5,9]
          
        
• Step 4: The insertion on Dqueue is carried with certain condition.
                      
  - Condition 1 : If the element present at front is less than the new element, then new element will be inserted in front. [Otherwise]
  - Condition 2 : If element present at rear is less than the new element, then new element will be inserted at rear.
  - Condition 3 : If both condition 1 and condition 2 not satisfied, ignore the element and consider new element.


**CODE :**
```py
# taking input from the user and storing it in a list
n = int(input("Enter the size of an array :"))
array = []
for i in range(n):
    array.append(int(input()))
print("The list of input is : ", array)


dqueue = []                  # declaring an empty list for Dqueue


dqueue.insert(0, array[0])   # the first element is inserted by front in the dqueue
print("insert {} at front".format(array[0]))
print("-----------------------------", dqueue)

flag = 0
for i in range(1, len(array), 1):

    # CONDITION 1: insertion from front
    if (dqueue[0] < array[i] and flag == 1):
        dqueue.insert(0, array[i])
        print("insert {} at front".format(array[i]))
        flag = 0

    # CONDITION 2: insertion from rear
    elif (dqueue[-1] < array[i] and flag == 0):
        dqueue.append(array[i])
        print("insert {} at rear".format(array[i]))
        flag = 1

    # CONDITION 3: ignoring the element
    else:
        print("ignoring ", array[i])

    print("-----------------------------", dqueue)


# FINAL OUTPUT
print("\n\n*******final dqueue*******\n        ", dqueue)
```

**TEST CASES :**

• TEST CASE 1 : 
                     
    INPUT  : ASCENDING array
    OUTPUT : - The dqueue consists all the elements of the input array.
             - The dqueue is decreasing till the first inserted element and then it is increasing till the end.
             - The difference between size of array and size of dqueue => 5 - 5 = 0 
               (0 gives the count of ignored elements that are not inserted in the dqueue)

  ![a](https://user-images.githubusercontent.com/113937257/202613187-286ad68f-adc7-4e85-b833-1dea59a2e3b3.png)


• TEST CASE 2 : 

    INPUT  : DESCENDING array
    OUTPUT : - The dqueue only consists of the first inserted element
             - The difference between size of array and size of dqueue =>  6- 1 = 5 
               (5 gives the count of ignored elements that aren't inserted in the dqueue)

  ![b](https://user-images.githubusercontent.com/113937257/202613254-224f1354-98cf-4777-abdf-50ce685b31f8.png)


• TEST CASE 3 :

    INPUT  : RANDOM array
    OUTPUT : - The dqueue is decreasing till the first inserted element and then it is increasing till the end
             - The difference between size of array and size of dqueue =>  6- 4 = 2 
               (2 gives the count of ignored elements that aren't inserted in the dqueue)

  ![c](https://user-images.githubusercontent.com/113937257/202613273-4075a0ec-49a9-4d4f-824e-fdbe80061e4e.png)
  
  
  
• Find out difference between size of Dqueue and size of array. 
             
    -The difference between the size of dqueue and the size of input array is equal to the uninserted elements which are ignored due to the insertion conditions.

• Comment on shape of Dqueue : How the elements present in the Dqueue look like [Ascending/Descending/or …]
    
    -The elements present in the dqueue are decreasing till the first inserted element and then increasing till the end of the dqueue.

• Suggest a suitable mechanism, such that no element of array is ignored and it is inserted in the Dqueue.

    -The easiest way to insert all the elements is to use and if-else statement inside a for loop that ensures alternate front-rear-front-rear insertion of elements.
    
    IF STATEMENT : FOR even indices of input array--->for insertion from front end
    => using the function "insert(index,value)" of lists in python which inserts a particular value at the specified index of the list.
    => insert(0,new_element) =>will insert the element at front position
                
    ELSE STATEMENT : FOR odd indices of input array--->for insertion from rear end
    => using the function "append(value)" of lists in python that appends the specified value at the end of the list.
    => append(new_element) => will append the element at rear position.
       
       
     EXAMPLE:
     Input array : [23 45 34 99 10 39 89 52 4]
                    0  1  2  3  4  5  6  7  8 (indices)
                    
     -----index 0 --insertion from front [23]
     -----index 1 --insertion from rear  [23 45]
     -----index 2 --insertion from front [23 45 34]
     -----index 3 --insertion from rear [23 45 34 99]....and so on till the last element of the input array
     
                
