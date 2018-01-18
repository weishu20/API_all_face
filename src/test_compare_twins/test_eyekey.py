import os
import sys
import cv2
import time
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
            buf = fn + " : " + result["message"] + "\n"
            result_file.writelines(buf)
        except:
            buf = fn + " : 404 " + "\n"
            result_file.writelines(buf)
    return face_id

def MyCompare(path1,path2,num,confidence,result_file):
    files1 = os.listdir(path1)
    files2 = os.listdir(path2)
    num1 = len(files1)
    num2 = len(files2)
    j = 0
    while j < num:
        ran1 = random.randint(0, num1 - 1)
        ran2 = random.randint(0, num2 - 1)

        file1 = path1 + files1[ran1]

        file2 = path2 + files2[ran2]
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

    result_file.writelines("\n\n\n")
    return confidence


path1 = '/home/shushi/Pic/ZhuJiaWen/'
path2 = '/home/shushi/Pic/ZhuJiaYi/'
output_path = '../result/compare_twins/eyekey/'

if not os.path.exists(output_path):
    os.makedirs(output_path)


eyekey = Eyekey()
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')

num = 100
confidence1 = 0.0
confidence2 = 0.0

confidence1 = MyCompare(path1,path1,num,confidence1,result_file)
confidence1 = MyCompare(path2,path2,num,confidence1,result_file)
confidence2 = MyCompare(path1,path2,num*2,confidence2,result_file)

print("confidence1: "+str(confidence1/num/2))
print("confidence2: "+str(confidence2/num/2))
result_file.flush()
result_file.close()