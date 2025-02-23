# main.py

import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import os
import cv2
import natsort

def preprocessing_img(image):
        
    # Resize image to 128 x 128 pixels (adjust?)
    
    resized_img = cv2.resize(image, (128, 128))
      
    tmp_img = np.zeros(resized_img.shape, resized_img.dtype)
      
    alpha = 1.0 # Contrast (adjust)
    beta = 0 # Brightness (adjust?)
        
    # Enhance contrast for images with linear transformation 
        
    for y in range(resized_img.shape[0]):
        for x in range(resized_img.shape[1]):
            for c in range(resized_img.shape[2]):
                tmp_img[y, x, c] = np.clip(alpha * resized_img[y, x, c] + beta, 0, 255)
                
    return tmp_img
    
def preprocessing_dir(directory):

    imgs_list = []

    # List with the names of the images
    
    imagesList = listdir(directory)
    
    # Make sure that the images are sorted in ascending order
    
    imagesList = natsort.natsorted(imagesList)

    # Read the images
    
    for i in range(len(imagesList)):
        tmp_img = cv2.imread(os.path.join(directory, imagesList[i]))
        
        # Preprocessing for each image in ditrectory 
        
        preprocessed_img = preprocessing_img(tmp_img)
                    
        # Convert the images to numpy arrays
        
        img_arr = np.array(preprocessed_img)
        imgs_list.append(img_arr/255.)

     # Convert the lists to numpy arrays
     imgs = np.asarray(imgs_list)

     return imgs

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
                directory = os.path.join(path, nameF)
                
                # Preprocess all images in directory
                
                preprocessed_imgs = preprocessing_dir(directory)
    
    # Picture option selected 
    
    elif picture == 1:
        print("Picture option selected!")
        
        loop = 0
        
        # loop until user inputs picture that is in directory
        
        while loop != 1:
            nameP = input("Input picture name: ")
        
            loop2 = 0
            ext = ""
            fullnameP = ""
            
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
                picture_path = os.path.join(path, fullnameP)
                image = preprocessing_img(picture_path)
           
if __name__ == "__main__":
    main()