def main():
    filename = input("Enter a filename: ")
   
    name, extension = filename.split('.')
    extension = extension.lower()  
    
    extension_to_language = {
        "py": "Python",
        "java": "Java",
        "cpp": "C++",
        "c": "C",
    }
    
    if extension in extension_to_language:
        language = extension_to_language[extension]
        print(f"The extension of the file is: {language}")
    else:
        print("Unknown extension")

if __name__ == "__main__":
    main()
