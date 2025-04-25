MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove the last element
        print(removed)       # Print the removed element

# Example main() function for testing
def main():
    # Example list, you can change this for testing
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    shorten(items)
    print("Final list:", items)

# Run the program
if __name__ == "__main__":
    main()
