import os
import sys
import cv2
import time
import math
import scipy.io as sio
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_baidu import Baidu
from utils.base import draw_face_rectangle_baidu


path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_diff/baidu/'
baidu = Baidu()
if not os.path.exists(output_path):
    os.makedirs(output_path)
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')

file_paths = os.listdir(path)
num = 300
j = 0
confidence = 0.0
while j < num:
    ran1 = random.randint(0, 122)
    ran2 = random.randint(0, 122)
    while ran2 == ran1:
        ran2 = random.randint(0, 122)
    ran3 = random.randint(0, 36)
    ran4 = random.randint(0, 36)

    file_path1 = path + file_paths[ran1]+"/"
    file_path2 = path + file_paths[ran2]+"/"


    files1 = os.listdir(file_path1)
    files2 = os.listdir(file_path2)
    file1 = file_path1+files1[ran3]
    file2 = file_path2+files2[ran4]

    result = baidu.compare(file1, file2)
    print(file1,file2)
    try:
        result_num = result["result_num"]
        if result_num != 0:
            faces = result['result'][0]
            buf = file1 + " vs " + file2 + "\n" + "score: " + str(faces["score"]) + "\n"
            confidence += faces["score"]
            result_file.writelines(buf)
            j += 1
        else:
            buf = file1 + " vs " + file2 + " : no face" + "\n"
            result_file.writelines(buf)
    except:
        print("error")
        if result["error_code"]==18:
            continue
        else:
            buf = file1 + " vs " + file2 + " " + result["error_code"] + "\n"
            result_file.writelines(buf)
print("confidence: "+str(confidence/num))
result_file.flush()
result_file.close()
