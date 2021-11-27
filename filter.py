from PIL import Image
import numpy as np
import sys

def convert_image_to_mosaic(img_in = 'img2.jpg', img_out ='res.jpg', block_size = 10, gradation_step = 50):
    img_in = Image.open(img_in)
    arr = np.array(img_in)
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[0]):
            s = np.mean(arr[i:i + block_size, j:j + block_size][:])
            arr[i:i + block_size, j:j + block_size][:] = int(s // gradation_step) * gradation_step
            j = j + block_size
        i = i + block_size
    res = Image.fromarray(arr)
    res.save(img_out)

convert_image_to_mosaic(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))

