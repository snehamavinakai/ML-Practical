def write_to_file(filename):
    with open(filename,'w')as file:
        print("Enter text to write to the file. type 'exit' on a new line to finish.")
        while True:
            line=input()
            if line.lower()=='exit':
                break
            file.write(line+'\n')
        print(f"data written to {filename}")
def read_from_file(filename):
    try:
        with open(filename,'r')as file:
            content=file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print(f"Error. the file '{filename}' doesn't exist")
def append_to_file(filename):
    with open(filename,'a')as file:
        print("Enter text to append to the file. Type 'exit' on a line to finish.")
        while True:
            line=input()
            if line.lower()=='exit':
                break
            file.write(line+'\n')
        print(f"data appended to '{filename}'")
def read_lines_from_file(filename):
    try:
        with open(filename,'r') as file:
            lines=file.readlines()
            print("\nLines in File:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error. The file'{filename}' doesn't exist")
def main():
    while True:
        print("\nFile operations menu:")
        print("1.Write to a file")
        print("2.read from a file")
        print("3.append to file")
        print("4.read lines from a file")
        print("5.Exit")
        choice=input("Enter your choice(1-5):")
        if choice=='1':
            filename=input("Enter filename to write to:")
            write_to_file(filename)
        elif choice=='2':
            filename=input("Enter filename to read from:")
            read_from_file(filename)
        elif choice=='3':
            filename=input("Enter filename to append to:")
            append_to_file(filename)
        elif choice=='4':
            filename=input("Enter filename to read lines from:")
            read_lines_from_file(filename)
        elif choice=='5':
            print("Exiing...")
            break
        else:
            print("invalid choice.please enter a number between 1 and 5.")
if __name__=="__main__":
    main()