try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
