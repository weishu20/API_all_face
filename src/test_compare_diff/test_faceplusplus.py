import os
import sys
import cv2
import time
import math
import scipy.io as sio
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_faceplusplus import FacePlusPlus,FaceSet,Face
from utils.base import draw_face_rectangle


path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_diff/faceplusplus/'
faceplus = FacePlusPlus()
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
    file_outpath1 = output_path + file_paths[ran1] + "/"
    file_outpath2 = output_path+file_paths[ran2]+"/"


    files1 = os.listdir(file_path1)
    files2 = os.listdir(file_path2)
    file1 = file_path1+files1[ran3]
    file2 = file_path2+files2[ran4]
    time.sleep(1)
    img1 = cv2.imread(file1)
    img2 = cv2.imread(file2)
    result = faceplus.compare(file1, file2)
    try:
        face1 = result['faces1']
        if not os.path.exists(file_outpath1):
            os.makedirs(file_outpath1)
        draw_face_rectangle(face1, img1, file_outpath1+files1[ran3])

        face2 = result['faces2']
        if not os.path.exists(file_outpath2):
            os.makedirs(file_outpath2)
        draw_face_rectangle(face2, img2, file_outpath2+files2[ran4])
        if len(face1) != 0 and len(face2) != 0:
            buf = file1 + " vs " + file2 + "\n" + "confidence: " + str(result["confidence"]) + "  thresholds:" + str(
                result["thresholds"]) + "\n"
            confidence += result["confidence"]
            result_file.writelines(buf)
            j += 1
        elif len(face1) == 0:
            buf = file1 + " vs " + file2 + "\n" + "no face :" + str(file1) + "\n"
            result_file.writelines(buf)
        elif len(face2) == 0:
            buf = file1 + " vs " + file2 + "\n" + "no face :" + str(file2) + "\n"
            result_file.writelines(buf)
    except:
        print("error")
        if result["error_message"] == "CONCURRENCY_LIMIT_EXCEEDED":
            continue
        else:
            buf = file1 + " vs " + file2 + "\n" + result["error_message"] + "\n"
            result_file.writelines(buf)
print("confidence: "+str(confidence/num))
result_file.flush()
result_file.close()
