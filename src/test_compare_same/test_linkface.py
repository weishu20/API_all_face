import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_linkface import Linkface,FaceSet
from utils.base import draw_face_rectangle

path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_same/linkface/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

linkface = Linkface()
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')
confidence = 0.0
total = 0
file_paths = os.listdir(path)[0:20]
for j in range(len(file_paths)):
    file_path = path + file_paths[j]+"/"
    file_outpath = output_path+file_paths[j]+"/"
    files = os.listdir(file_path)
    k = 1
    while k < len(files):
        #time.sleep(1)
        file1 = file_path+files[0]
        file2 = file_path+files[k]
        print(file1, file2)
        img1 = cv2.imread(file1)
        img2 = cv2.imread(file2)
        result = linkface.compare(file1, file2)
        if result["status"] == "OK":
            buf = file1 + " vs " + file2 + "\n" + "confidence:" + str(result["confidence"]) + "\n"
            result_file.writelines(buf)
            k += 1
            confidence += result["confidence"]
            total += 1
        elif result["status"] == "RATE_LIMIT_EXCEEDED":
            continue
        else:
            print("error")
            if result["status"] == "NO_FACE_DETECTED":
                buf = file1 + " vs " + file2 + "\n" + "error: " + str(result["status"]) \
                      + " image: " + str(result["image"]) + "\n"
                result_file.writelines(buf)
                if not os.path.exists(file_outpath):
                    os.makedirs(file_outpath)
                if result["image"] == "selfie":
                    cv2.imwrite(file_outpath + files[0], img1)
                else:
                    cv2.imwrite(file_outpath + files[k], img2)
            k += 1
            continue

print(str(confidence/total))
result_file.flush()
result_file.close()
