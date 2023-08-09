import math as M  
Radius = float (input ("Input the radius of the circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the circle with radius 1.1 is: ", area_of_the_circle)  


def main():
    filename = input("Enter a filename: ")
    
    name, extension = filename.split('.')
    print("The extension of the file is:", extension)

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

if '_name_' == "_main_":
    main()
