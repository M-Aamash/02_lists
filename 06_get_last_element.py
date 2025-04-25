def main ():
    def last_element (lst):
        print (f"The last element is:{lst[-1]} ")
    
    num_element = int (input(f"how many element in the list? "))
    my_list = []
    for i in range (num_element):
        element = (input(f"Enter element # {i + 1}: "))
     
    my_list.append (element)
    last_element (my_list)

if __name__ == "__main__":
    main()