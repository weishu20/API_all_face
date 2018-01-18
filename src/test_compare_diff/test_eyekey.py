import os
import sys
import cv2
import time
import math
import scipy.io as sio
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_eyekey import Eyekey
from utils.base import draw_face_rectangle

def MyDetect(fn,result_file):
    face_id = ""
    result = eyekey.detect(fn)
    try:
        face = result['face'][0]
        face_id = face["face_id"]
    except:
        print("error")
        try:
            buf = str(j) + " " + fn + " : " + result["message"] + "\n"
            result_file.writelines(buf)
        except:
            buf = str(j) + " " + fn + " : 404 " + "\n"
            result_file.writelines(buf)
    return face_id

path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_diff/eyekey/'
eyekey = Eyekey()
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

    face_id1 = MyDetect(file1, result_file)
    face_id2 = MyDetect(file2, result_file)
    if face_id1 != "" and face_id2 != "":
        result = eyekey.compare(face_id1, face_id2)
        try:
            buf = file1 + " vs " + file2 + "\n" + "similarity: " + str(result["similarity"]) + "\n"
            result_file.writelines(buf)
            confidence += result["similarity"]
            j += 1
        except:
            buf = file1 + " vs " + file2 + "\n" + ":405 " + "\n"
            result_file.writelines(buf)

print("confidence: "+str(confidence/num))
result_file.flush()
result_file.close()
