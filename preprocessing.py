import cv2
import numpy as np
import os

kernel_size = 5
kernel_v = np.zeros((kernel_size, kernel_size))
kernel_h = np.copy(kernel_v)
kernel_v[:, int((kernel_size - 1)/2)] = np.ones(kernel_size)
kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)
kernel_v /= kernel_size
kernel_h /= kernel_size

def motion_blur(img):
    vertical_mb = cv2.filter2D(img, -1, kernel_v)
    vertical_mb = cv2.filter2D(vertical_mb, -1, kernel_h)
    return vertical_mb

def create_blurred_images(folder):
    os.mkdir("blur_imgs")
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        new_img = motion_blur(img)
        if img is not None:
            cv2.imwrite(os.path.join("blur_imgs",filename),new_img)

#orig_imgs folder contains all the original images of documents
img_dir = "orig_imgs"

create_blurred_images(img_dir)
