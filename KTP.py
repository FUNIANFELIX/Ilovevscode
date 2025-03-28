
print("Welcome KTP (Key Typer Program)")
print("Would you like to use the program? Type 'yes' or 'no':")

input_yesorno = input()  

if input_yesorno.lower() == "yes":
    files = input("Enter the name of the file (with extension, e.g., 'example.txt'): ")

    try:
        with open(files, 'w') as file:  
            print("File opened successfully. Start writing content. Type 'finish' to save and exit.")

            while True:
                line = input("Enter a line of text (or 'finish' to end): ")

                if line == "finish":
                    print(f"Content saved to {files}. Exiting program.")
                    break

                file.write(line + "\n")

            print("I saved the file dw")
            print("If you think im lying check the content")

    except Exception as e:
        print(f"An error occurred: {e}")
else:
   if input_yesorno : ("no")
print("Alright, bye! Stay safe :)")
