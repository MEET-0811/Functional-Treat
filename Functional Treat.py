data = []      # will store 1D list only (simple version)

# 1. Built-in Functions
def show_summary():
    print("\n--- Data Summary ---")
    print("Total elements:", len(data))
    print("Minimum:", min(data))
    print("Maximum:", max(data))
    print("Sum:", sum(data))
    print("Average:", sum(data) / len(data))


# 2. User-defined Function
def get_avg(lst):
    return sum(lst) / len(lst)


# 3. *args, **kwargs, __doc__
def show_info(*args, **kwargs):
    """This function prints args & kwargs data"""
    print("\nArgs:", args)
    print("Kwargs:", kwargs)


# 4. Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 5. Lambda (filter)
def filter_data(threshold):
    return list(filter(lambda x: x >= threshold, data))


# 6. Return multiple values
def stats():
    return min(data), max(data), sum(data), get_avg(data)


# 7. Sorting
def sort_data(order):
    return sorted(data, reverse=(order == "desc"))


# -------------------------
# MAIN MENU
# -------------------------
while True:
    print("\n----- SIMPLE DATA ANALYZER -----")
    print("1. Input Data")
    print("2. Show Summary")
    print("3. Factorial (Recursion)")
    print("4. Filter Data (Lambda)")
    print("5. Sort Data")
    print("6. Show Stats (Return Multiple Values)")
    print("7. Show *args, **kwargs, __doc__")
    print("8. Exit")

    ch = int(input("Enter choice: "))

    # 1
    if ch == 1:
        arr = input("Enter numbers (space separated): ").split()
        data = list(map(int, arr))
        print("Data saved!")

    # 2
    elif ch == 2:
        show_summary()

    # 3
    elif ch == 3:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))

    # 4
    elif ch == 4:
        t = int(input("Enter threshold value: "))
        print("Filtered:", filter_data(t))

    # 5
    elif ch == 5:
        print("asc / desc?")
        o = input("Enter order: ")
        print("Sorted:", sort_data(o))

    # 6
    elif ch == 6:
        mn, mx, sm, av = stats()
        print("\n--- Stats ---")
        print("Min:", mn)
        print("Max:", mx)
        print("Sum:", sm)
        print("Avg:", av)

    # 7
    elif ch == 7:
        show_info(10, 20, 30, name="Test", size=len(data))
        print("\nDoc:", show_info.__doc__)

    # 8
    elif ch == 8:
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
