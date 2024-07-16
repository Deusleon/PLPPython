def create_file():
    file = None
    try:
        file = open('my_file.txt', 'w')
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: This is PLP Python.\n")
        file.write("Line 3: 1234567890\n")
        print("File created and initial content written.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
    finally:
        if file:
            file.close()

def read_file():
    file = None
    try:
        file = open('my_file.txt', 'r')
        content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        if file:
            file.close()

def append_to_file():
    file = None
    try:
        file = open('my_file.txt', 'a')
        file.write("Line 4: Appending new content.\n")
        file.write("Line 5: This line was added.\n")
        file.write("Line 6: This is line 2 appending.\n")
        print("New content appended to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        if file:
            file.close()

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
