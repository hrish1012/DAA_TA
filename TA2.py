# taking input from the user and storing it in a list
n = int(input("Enter the size of an array :"))
array = []
for i in range(n):
    array.append(int(input()))
print("The list of input is : ", array)


dqueue = []                  # declaring an empty list for Dqueue

print("insert {} at front".format(array[0]))
dqueue.insert(0, array[0])   # the first element is inserted by front in the dqueue

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
