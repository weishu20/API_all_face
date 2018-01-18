import os
import sys
import cv2
import time
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_linkface import Linkface,FaceSet
from utils.base import draw_face_rectangle


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
        time.sleep(1)
        img1 = cv2.imread(file1)
        img2 = cv2.imread(file2)
        result = linkface.compare(file1, file2)
        if result["status"] == "OK":
            buf = file1 + " vs " + file2 + "\n" + "confidence:" + str(result["confidence"]) + "\n"
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
                    cv2.imwrite(undetected + files2[ran1], img1)
                else:
                    cv2.imwrite(undetected + files2[ran2], img2)
            continue
    result_file.writelines("\n\n\n")

    return confidence

path1 = '/home/shushi/Pic/ZhuJiaWen/'
path2 = '/home/shushi/Pic/ZhuJiaYi/'
output_path = '../result/compare_twins/linkface/'
undetected = '../result/compare_twins/linkface/undetected/'
if not os.path.exists(undetected):
    os.makedirs(undetected)

linkface = Linkface()
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