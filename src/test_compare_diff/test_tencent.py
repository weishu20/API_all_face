import os
import sys
import cv2
import time
import math
import scipy.io as sio
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_tencent import Tencent
from utils.base import draw_face_rectangle_tencent


path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_diff/tencent/'
tencent = Tencent()
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

    print(file1, file2)
    result = tencent.compare(file1, file2)
    if result != {}:
        if result["code"] == 0:
            similarity = result["data"]["similarity"]
            buf = file1 + " vs " + file2 + "\n" + "similarity: " + str(similarity) + "\n"
            confidence += similarity
            result_file.writelines(buf)
            j += 1
        else:
            print("error")
            if result["code"] == -1101 or result["code"] == -1305:
                fail_flag = result["data"]["fail_flag"]
                if fail_flag == 1:
                    img1 = cv2.imread(file1)
                    file_outpath1 = output_path + file_paths[ran1] + "/"
                    print(file_outpath1)
                    if not os.path.exists(file_outpath1):
                        os.makedirs(file_outpath1)
                    cv2.imwrite(file_outpath1+files1[ran3], img1)
                    buf = file1 + " :"+result["message"] + "\n"
                    result_file.writelines(buf)
                else:
                    img2 = cv2.imread(file2)
                    file_outpath2 = output_path + file_paths[ran2] + "/"
                    print(file_outpath2)
                    if not os.path.exists(file_outpath2):
                        os.makedirs(file_outpath2)
                    cv2.imwrite(file_outpath2+files2[ran4], img2)
                    buf = file2 + " :"+result["message"] + "\n"
                    result_file.writelines(buf)
            elif result["code"] == 15 or result["code"] == 213:
                continue
            else:
                buf = file1 + " vs " + file2 + " " + result["message"] + "\n"
                result_file.writelines(buf)
    else:
        continue

print("confidence: "+str(confidence/num))
result_file.flush()
result_file.close()
