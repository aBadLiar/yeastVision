# main.py

import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import os

# Check that file is in specified directory

def valid(path, file, folder):
    
    # Search for folder in directory
    
    if folder == 1:
        
        # Loop through contents of directory
        
        for entry in os.listdir(path):
            
            # Check for match to folder
            
            if entry == file:
                print(f"Folder {file} Found!")
                print()
                
                return True
            
        # Folder not found
        
        print(f"Folder {file} not found. Try another name")
        print()
        return False
    
    # Search for picture in directory
    
    else:
        
        # Loop through contents of directory
        
        for entry in os.listdir(path):
            
            # Check for match to picture
            
            if entry == file:
                print(f"Picture {file} Found!")
                print()
                
                return True
        
        # Picture not found 
        
        print(f"Picture {file} not found. Try another name")
        print()
        return False
        
        

def main():
    
    path = "C:\Users\hailc\Pictures"
    
    # User menu
    
    print("Welcome to Yeast Vision!")
    print()
    print("Processing Options:")
    print("Folder (1))
    print("Picture (2))
    print()
    
    loop = 0
    folder = 0
    picture = 0
    
    # Loop to determin if user inputs a valid option (1 or 2)
    
    while loop != 1:
        option = input("Select object to process: ")
        numOp = int(option)
    
        # User doesn't enter valid option (continue loop)
        
        if numOp != 1 and numOp != 2:
            print("Error: Not a valid option. Try again!")
            print()
        
        # User enters valid option (end loop)
        
        else:
            loop = 1
            
            if numOp == 1:
                folder = 1
            
            else:
                picture = 1
    
    
    # Folder option selected
    
    if folder == 1:
        print("Folder option selected!")
        
        loop = 0
        
        # Loop until user inputs folder that is in directory
        
        while loop != 1
        
            nameF = input("Input folder name: ")
        
            found = valid(path, nameF, 1)
            
            # Inputted folder is found
            
            if found == True:
                loop = 1
    
    # Picture option selected 
    
    elif picture == 1:
        print("Picture option selected!")
        
        loop = 0
        
        # loop until user inputs picture that is in directory
        
        while loop != 1:
            nameP = input("Input picture name: ")
        
            loop2 = 0
            ext = ""
            
            # Loop until user selects valid image file extension
            
            while loop2 != 1:
                print("Image File Types:")
                print(".png (1)")
                print(".jpg (2)")
                print(".jpeg (3)")
                print()
           
                extension = input("Select image file extension: ")
                
                # .png
                
                if extension == 1:
                    loop2 = 1
                    ext = ".png"
                
                #.jpg
                
                elif extension == 2:
                    loop2 = 1
                    ext = ".jpg"
                
                #.jpeg
                
                elif extension == 3:
                    loop2 = 1
                    ext = ".jpeg"
                
                # Invalid
                
                else:
                    print("Error: Not a valid option. Try again!")
                    print()
                   
                fullnameP = nameP + ext
        
           found = valid(path, fullnameP, 0)
           
           # Picture found in directory
           
           if found == True:
                loop = 1
           
if __name__ == "__main__":
    main()