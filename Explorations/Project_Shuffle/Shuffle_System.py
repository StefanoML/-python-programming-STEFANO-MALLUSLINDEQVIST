import math
import random as rnd
import os


file_dirin = os.path.join(os.path.dirname(__file__), "input")
file_dirout = os.path.join(os.path.dirname(__file__), "output")

filein = input("Please Enter the name of the file you want to shuffle:")
if not filein.endswith(".txt"):
    filein += ".txt"

fileout = input("Please Enter the name of the output file you would like to generate:")
if not fileout.endswith(".txt"):
    fileout += ".txt"

filepath_in = os.path.join(file_dirin,filein)
filepath_out = os.path.join(file_dirout,fileout)

def read_file(file):
    try:
        with open (file, "r", encoding="utf-8")as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Specified file not found, please check that the file is in the 'input' directory")
        return
    
def main():
    print("Would you like to:")
    print("1: Decide the number of groups to create;")
    print("2: Decide the amount of elements in each group.")
    print("3: Just shuffle the elements in the list")
    try:
        choice = int(input("Please enter your choice..."))
    except ValueError:
        print("Please enter a number between 1 and 3.")
        return
    
    items = read_file(filepath_in)

    #We check whether the file doesn't exist, or does not contain any data
    if items is None: 
        return
    if not items:
        print(f"The file {filein} does not contain any data")
        return

#Now we can finally go on with the script's functionalities
    if choice == 1:
        try:
            groups = int(input("How many groups would you like to create?"))

        except ValueError:
            print("Please enter a number.")
            return
        
        rnd.shuffle(items)
        groups_list = []
        group_size = math.ceil(len(items)/groups) #Calculates the size of groups

        for i in range(0,len(items), group_size):
            groups_list.append(items[i:i + group_size])

        os.makedirs(file_dirout, exist_ok=True) #Checks that the directory exists

        with open(filepath_out, "w", encoding="utf-8") as f:
            for idx, group in enumerate(groups_list, start=1):
                f.write(f"Group {idx}:\n")
                for item in group:
                    f.write(f"- {item}\n")
                f.write("\n")

        print(f"{len(groups_list)} groups have been created and saved to {filepath_out}!")



    elif choice == 2:
        try:
            elements = int(input("How many elements would you like each group to include?"))
        except ValueError:
            print("Please enter a number.")
            return
        
        rnd.shuffle(items)
        groups_list = []

        for i in range(0,len(items), elements):
            groups_list.append(items[i:i + elements])

        os.makedirs(file_dirout, exist_ok=True) #Checks that the directory exists

        with open(filepath_out, "w", encoding="utf-8" )as f:
            for idx, group in enumerate(groups_list, start=1):
                f.write(f"Group {idx}:\n")
                for item in group:
                    f.write(f"- {item}\n")
                f.write("\n")

        print(f"{len(groups_list)} groups have been created and saved to {filepath_out}!")





    elif choice == 3:
        rnd.shuffle(items)

        os.makedirs(file_dirout, exist_ok=True) #Checks that the directory exists
        with open(filepath_out, "w", encoding="utf-8") as f:
            for item in items:
                f.write(item + "\n")
        print("A shuffled file has now been created.")
    else: 
        print("Please enter a valid choice.")


if __name__ == "__main__":
    main()