#4] program to perform file handling operations
def main():
 while True:
     print("\nFile Handling Menu:")
     print("1. Write to a file")
     print("2. Read from a file")
     print("3. Append to a file")
     print("4. Exit")
     choice = int(input("Enter your choice: "))
     if choice == 1:
        file_name = input("Enter the file name: ")
        content = input("Enter the content to write: ")
        with open(file_name, 'w') as file:
           file.write(content)
        print(f"Content written to '{file_name}'.")

     elif choice == 2:
        file_name = input("Enter the file name: ")
        try:
           with open(file_name, 'r') as file:
            print(f"Content of '{file_name}':")
            print(file.read())
        except FileNotFoundError:
           print(f"File '{file_name}' does not exist.")
     elif choice == 3:
        file_name = input("Enter the file name: ")
        content = input("Enter the content to append: ")
        with open(file_name, 'a') as file:
          file.write(content)
        print(f"Content appended to '{file_name}'.")
     elif choice == 4:
         print("Exiting program.")
         break
     else:
       print("Invalid choice. Please try again.")

if __name__ == "__main__":
 main()