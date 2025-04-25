def main():
    def first_element (lst):
        print (f"The first element is: {lst[0]}")

    num_element =int (input("How many element in the list? "))
    my_list = []

    for i in range(num_element):
        element =input (f"Enter element # {i + 1}: ")  
        my_list.append(element)

    first_element(my_list)

if __name__ == "__main__":
    main()