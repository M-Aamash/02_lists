
def main():
    def add_three_copies(my_list,data):
        my_list.append(data)
        my_list.append(data)
        my_list.append(data)
    
    
    message = input("Enter a message to copy: ")
    my_messages=[]

    print(f"List before:{my_messages}")

    add_three_copies (my_messages,message)

    print(f"List after: {my_messages}")
if __name__ == "__main__":
    main()
