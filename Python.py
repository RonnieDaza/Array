list1 = [1, 2, 5, 7, 13, 19, 50, 300, 200, 100]
print("Array: ", list1)

print("Menu: ")
print("1 -> Add an element")
print("2 -> Insert an element")
print("3 -> Modify an element")
print("4 -> Delete an element")
print("5 -> Arrange in ascending order")
print("6 -> Arrange in descending order")

choice = int(input("What do you want to do? "))

if choice == 1:
    list1.append(int(input("Enter the element you want to add: ")))
    print("The element has been added.")
    print("This is the new array: ", list1)
elif choice == 2:
    list1.insert(int(input("Enter the element you want to insert: ")))
    print(list1)


