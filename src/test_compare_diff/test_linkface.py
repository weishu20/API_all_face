import os
import sys
import cv2
import time
import math
import scipy.io as sio
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_linkface import Linkface,FaceSet
from utils.base import draw_face_rectangle


path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_diff/linkface/'
if not os.path.exists(output_path):
    os.makedirs(output_path)
linkface = Linkface()

file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')

file_paths = os.listdir(path)
num = 300
j = 0
confidence = 0.0
while j < num:
    #time.sleep(1)
    ran1 = random.randint(0, 122)
    ran2 = random.randint(0, 122)
    while ran2 == ran1:
        ran2 = random.randint(0, 122)
    ran3 = random.randint(0, 36)
    ran4 = random.randint(0, 36)

    output_path1 = output_path + file_paths[ran1]+"/"
    output_path2 = output_path + file_paths[ran2]+"/"

    file_path1 = path + file_paths[ran1]+"/"
    file_path2 = path + file_paths[ran2]+"/"

    files1 = os.listdir(file_path1)
    files2 = os.listdir(file_path2)

    file1 = file_path1+files1[ran3]
    file2 = file_path2+files2[ran4]

    img1 = cv2.imread(file1)
    img2 = cv2.imread(file2)
    result = linkface.compare(file1, file2)
    if result["status"] == "OK":

        buf = file1 + " vs " + file2 + "\n" + "confidence: " + str(result["confidence"]) + "\n"
        confidence += result["confidence"]
        result_file.writelines(buf)
        j += 1
    else:
        print("error")
        if result["status"] == "NO_FACE_DETECTED":
            buf = file1 + " vs " + file2 + "\n" + "error: " + str(result["status"]) \
                  + " image: " + str(result["image"]) + "\n"
            result_file.writelines(buf)
            if result["image"] == "selfie":
                if not os.path.exists(output_path1):
                    os.makedirs(output_path1)
                cv2.imwrite(output_path1 + files1[ran3], img1)
            else:
                if not os.path.exists(output_path2):
                    os.makedirs(output_path2)
                cv2.imwrite(output_path2 + files1[ran4], img2)
        continue
print("confidence: "+str(confidence/num))
result_file.flush()
result_file.close()
