def set_operations():
    print("\nSet Operations:")
    
    # Input sets
    set_a = set(map(int, input("Enter elements of Set A (space-separated): ").split()))
    set_b = set(map(int, input("Enter elements of Set B (space-separated): ").split()))
    
    # Display sets
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Perform all operations
    union = set_a | set_b
    intersection = set_a & set_b
    difference = set_a - set_b
    symmetric_difference = set_a ^ set_b
    
    # Display results
    print(f"\nResults of Set Operations:")
    print(f"Union (A ∪ B): {union}")
    print(f"Intersection (A ∩ B): {intersection}")
    print(f"Difference (A - B): {difference}")
    print(f"Symmetric Difference (A Δ B): {symmetric_difference}")

def dictionary_operations():
    print("\nDictionary Operations:")
    
    # Input dictionary
    n = int(input("Enter the number of key-value pairs: "))
    dictionary = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value
    
    while True:
        # Display menu
        print("\nSelect an operation:")
        print("1. Search for a key")
        print("2. Remove a key")
        print("3. Add a new key-value pair")
        print("4. Display the dictionary")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            # Search for a key
            key_to_search = input("Enter a key to search: ")
            if key_to_search in dictionary:
                print(f"Value for '{key_to_search}': {dictionary[key_to_search]}")
            else:
                print(f"'{key_to_search}' not found in dictionary.")
        elif choice == 2:
            # Remove a key
            key_to_remove = input("Enter a key to remove: ")
            if key_to_remove in dictionary:
                removed_value = dictionary.pop(key_to_remove)
                print(f"Removed key '{key_to_remove}' with value '{removed_value}'.")
            else:
                print(f"'{key_to_remove}' not found in dictionary.")
        elif choice == 3:
            # Add a new key-value pair
            new_key = input("Enter a new key to add: ")
            new_value = input("Enter its value: ")
            dictionary[new_key] = new_value
            print(f"Key '{new_key}' added with value '{new_value}'.")
        elif choice == 4:
            # Display the dictionary
            print(f"Current Dictionary: {dictionary}")
        elif choice == 5:
            # Exit the dictionary operations
            print("Exiting Dictionary Operations.")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Basic Operations on Set and Dictionary")
    
    while True:
        print("\nSelect an option:")
        print("1. Perform Set Operations")
        print("2. Perform Dictionary Operations")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            set_operations()
        elif choice == 2:
            dictionary_operations()
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
