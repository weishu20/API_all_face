import os
import sys
import cv2
import time
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
output_path = '../result/campare_same/eyekey/'
eyekey = Eyekey()
if not os.path.exists(output_path):
    os.makedirs(output_path)
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')
confidence = 0.0
total = 0
file_paths = os.listdir(path)[0:20]
for j in range(len(file_paths)):
    file_path = path + file_paths[j]+"/"
    files = os.listdir(file_path)
    file1 = file_path+files[0]
    face_id1 = MyDetect(file1,result_file)
    if face_id1 != "":
        k = 1
        while k < len(files):
            file2 = file_path + files[k]
            face_id2 = MyDetect(file2,result_file)
            if face_id2 != "":
                print(file1,file2)
                print(face_id1,face_id2)
                result = eyekey.compare(face_id1, face_id2)
                try:
                    buf = file1 + " vs " + file2 + "\n" + "similarity: " + str(result["similarity"]) + "\n"
                    result_file.writelines(buf)
                    confidence += result["similarity"]
                    total += 1
                except:
                    buf = file1 + " vs " + file2 + "\n" + ":405 " + "\n"
                    result_file.writelines(buf)
            k += 1
print(str(confidence/total))
result_file.flush()
result_file.close()
