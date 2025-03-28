import os
# FHS
file_path = "diary.txt"
print("Loading file systems and other stuff....")
print("Welcome to fhs! (file handeling system), The option  of the system are listed below")
if not os.path.exists(file_path):
    open(file_path, "w").close()

while True:
    option = input("You can: 1 write a entry, 2 you can view pass entries (if you have any) 3. leave ")

    if option == "1":
        password = input("also for extra security make a password, diarys are meant to be kept secert: ")
        if password == "mypassword":
            date = input("Whats the date as if in right now? ")
            entry = input("feel free to write a entry: ").replace("\n", " ")
            with open(file_path, "a") as file:
                file.write(f"Date: {date} | Entry: {entry}\n")
            print("Gimme a moment... and there entry saved.")
        else:
            print("entre a passwrod")

    elif option == "2":
        password = input("Enter password: ")
        if password == "passwords":
            with open(file_path, "r") as file:
                entries = file.read()
                if entries.strip():
                    print(entries)
                else:
                    print("I didnt find any entries")
        else:
            print("Wrong password, please dont break into  someones diary or im gonna call 911 >:(")

    elif option == "3":
        print("Alright bud bye")
        break

    else:
        print("That Aint Valid please choose one of 1, 2, or 3.")

#i used the website you sent in the code examples (if your reading this) instead  of  f i use file
#Also i have a question will we be using this code to open a sepreate window just like you showed in the presentation?
# also im not sure if this counts as a cite but in the only time.sleep thing over there i used the final text adventure code to make it looks like if it was loading, not sure if it is that important   