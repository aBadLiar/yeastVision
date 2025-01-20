# main.py

import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import os

def main():
    
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
        nameF = input("Input folder name: ")
        
        # Insert code to search for folder in directory here
    
    # Picture option selected 
    
    elif picture == 1:
        print("Picture option selected!")
        nameP = input("Input picture name: ")
        
        # Insert code to search for picture in directory here
    

if __name__ == "__main__":
    main()