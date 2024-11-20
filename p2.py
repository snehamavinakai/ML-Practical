def dictonary_opeartions():
    d = {}
    while True:
        print("\nDictonary Operations Menu: ")
        print("1.Add key-value pair")
        print("2.remove key")
        print("3.Display dictonary")
        print("4.Search for key")
        print("5.Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the valuie: ")
            d[key] = value
            print(f"Added :{{'{key}':'{value}'}}")
            
        elif choice == '2':
            key = input("Enter the key to remove: ")
            if key in d:
                del d[key]
                print(f'Removed key: {key}')
            else:
                print("Key not found")
                
        elif choice == '3':
            print("Current dictionary contents: ")
            for k, v in d.items():
                print(f"{k}:{v}")
                
        elif choice == '4':
            key = input("Enter the key to search: ")
            if key in d:
                print(f"key '{key}' found with value: {d[key]}")
            else:
                print("Key not found")
                
        elif choice == '5':
            break
        
        else:
            print("Invalid choice: please try again: ")
            
def set_operations():
    s = set()
    while True:
        print("\nSet Operations menu:")
        print("1.Add element ")
        print("2.Remove Element ")
        print("3.Display set")
        print("4.Check if element exists")
        print("5.Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter the element to add: ")
            s.add(element)
            print(f"Added element: {element}")
            
        elif choice == '2':
            element = input("Enter the element to remove: ")
            
            if element in s:
                print(f"Element '{element}' exists in the set ")
                
            else:
                print("Element not found")
                
        elif choice == '3':
            print("Current set contents: ")
            print(s)
            
        elif choice == '4':
            element = input("Enter the key to search: ")
            
            if element in s:
                print(f"Element '{element}' exists in the set")
            else:
                print("Element not found")
        
        elif choice == '5':
          break
        
        else:
             print("Invalid choice : please try again ")
             
def main():
    while True:
        print("\n Main Menu: ")
        print("1.Dictonary operations ")
        print("2.Set operations")
        print("3.Exit")
        
        choice = input("Entre your choice: ")
        
        if choice == '1':
            dictonary_opeartions()
            
        elif choice == '2':
            set_operations()
        
        elif choice == '3':
            print("Exiting...")
        
        else:
            print("Invalid choice .Please try again")
            
if __name__ == "__main__":
    main()               