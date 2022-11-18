
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


• Find out difference between size of Dqueue and size of array. [The difference will be number of elements in array not inserted in the Dqueue]

• Comment on shape of Dqueue : How the elements present in the Dqueue look like [Ascending/Descending/or …]

• Suggest a suitable mechanism, such that no element of array is ignored and it is inserted in the Dqueue [modify condition 1 and 2]


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
TEST CASE 1 : The input array is in ASCENDING order

    ![a](https://user-images.githubusercontent.com/113937257/202613187-286ad68f-adc7-4e85-b833-1dea59a2e3b3.png)

TEST CASE 2 : The input array is in DESCENDING order

    ![b](https://user-images.githubusercontent.com/113937257/202613254-224f1354-98cf-4777-abdf-50ce685b31f8.png)

TEST CASE 3 : The input array is  in RANDOM order

    ![c](https://user-images.githubusercontent.com/113937257/202613273-4075a0ec-49a9-4d4f-824e-fdbe80061e4e.png)
