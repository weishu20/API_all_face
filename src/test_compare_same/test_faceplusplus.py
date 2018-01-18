import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_faceplusplus import FacePlusPlus,FaceSet,Face
from utils.base import draw_face_rectangle

path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_same/faceplusplus/'
faceplus = FacePlusPlus()
if not os.path.exists(output_path):
    os.makedirs(output_path)
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')
confidence  = 0.0
total = 0
file_paths = os.listdir(path)[0:20]
for j in range(len(file_paths)):
    file_path = path + file_paths[j]+"/"
    file_outpath = output_path+file_paths[j]+"/"
    if not os.path.exists(file_outpath):
        os.makedirs(file_outpath)
    files = os.listdir(file_path)
    file1 = file_path+files[0]
    img1 = cv2.imread(file1)
    k = 1
    while k < len(files):
        time.sleep(1)
        file2 = file_path + files[k]
        print(file1, file2)
        img2 = cv2.imread(file2)
        result = faceplus.compare(file1, file2)
        try:
            face1 = result['faces1']
            draw_face_rectangle(face1, img1, file_outpath + files[0])
            face2 = result['faces2']
            draw_face_rectangle(face2, img2, file_outpath+files[k])
            if len(face1) != 0 and len(face2) != 0:
                buf = file1 + " vs " + file2 + "\n" + "confidence: " + str(result["confidence"]) + "  thresholds:" + str(
                    result["thresholds"]) + "\n"
                result_file.writelines(buf)
                confidence += result["confidence"]
                total += 1
            elif len(face1)==0:
                buf = file1 + " vs " + file2 + "\n" + "no face :" + str(file1) + "\n"
                result_file.writelines(buf)
            elif len(face2)==0:
                buf = file1 + " vs " + file2 + "\n" + "no face :" + str(file2) + "\n"
                result_file.writelines(buf)
            k += 1
        except:
            print("error")
            if result["error_message"] == "CONCURRENCY_LIMIT_EXCEEDED":
                continue
            else:
                buf = file1 + " vs " + file2 + "\n" + result["error_message"] + "\n"
                result_file.writelines(buf)
                k += 1
print(str(confidence/total))
result_file.flush()
result_file.close()
