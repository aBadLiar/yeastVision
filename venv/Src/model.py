# model .py

import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import os
import torch
import matplotlib.pyplot as plt
import cv2


sys.path.append("..")
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor


def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)
    
    
    
 #Open images current only opening one example image, will turn into a function that accepts a path as args
     
image = cv2.imread('images/example.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




#plot the image
plt.figure(figsize=(20,20))
plt.imshow(image)
plt.axis('off')
plt.show()

#initialize and instantiate SAM class & object

#change these two depending on the name & type of model, (can change to args in a function later for owen
sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

#default parameters
mask_generator = SamAutomaticMaskGenerator(sam)

#Call like this to customize parameters
mask_generator_2 = SamAutomaticMaskGenerator(
    model=sam,
    points_per_side=32,
    pred_iou_thresh=0.86,
    stability_score_thresh=0.92,
    crop_n_layers=1,
    crop_n_points_downscale_factor=2,
    min_mask_region_area=100,  # Requires open-cv to run post-processing
)




#THE MAGIC FUNCTION TO GENERATE MASKS
masks = mask_generator.generate(image)

'''
Mask generation returns a list over masks, where each mask is a dictionary containing various data about the mask. These keys are:

segmentation : the mask
area : the area of the mask in pixels
bbox : the boundary box of the mask in XYWH format
predicted_iou : the model's own prediction for the quality of the mask
point_coords : the sampled input point that generated this mask
stability_score : an additional measure of mask quality
crop_box : the crop of the image used to generate this mask in XYWH format

Example:

print(len(masks))
print(masks[0].keys())

dict_keys(['segmentation', 'area', 'bbox', 'predicted_iou', 'point_coords', 'stability_score', 'crop_box'])

'''

#Show Masks overlayed on image
plt.figure(figsize=(20,20))
plt.imshow(image)
show_anns(masks)
plt.axis('off')
plt.show() 