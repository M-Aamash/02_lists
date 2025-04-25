def main ():
    numbers = [1, 2, 3, 4, 5]

    double_list =  [num*3 for num in numbers]
    print(f"Original list {numbers}")
    print(f'Double list {double_list}')


if __name__  == "__main__":
    main()