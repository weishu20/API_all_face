import os
import sys
import cv2
import time
import random
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_tencent import Tencent
from utils.base import draw_face_rectangle

def MyCompare(path1,path2,file_outpath1,file_outpath2,num,confidence,result_file):
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
                        if not os.path.exists(file_outpath1):
                            os.makedirs(file_outpath1)
                        cv2.imwrite(file_outpath1 + files1[ran1], img1)
                        buf = file1 + " :" + result["message"] + "\n"
                        result_file.writelines(buf)
                    else:
                        img2 = cv2.imread(file2)
                        if not os.path.exists(file_outpath2):
                            os.makedirs(file_outpath2)
                        cv2.imwrite(file_outpath2 + files2[ran2], img2)
                        buf = file2 + " :" + result["message"] + "\n"
                        result_file.writelines(buf)
                elif result["code"] == 15 or result["code"] == 213:
                    continue
                else:
                    buf = file1 + " vs " + file2 + " " + result["message"] + "\n"
                    result_file.writelines(buf)
        else:
            continue
    result_file.writelines("\n\n\n")
    return confidence


path1 = '/home/shushi/Pic/ZhuJiaWen/'
path2 = '/home/shushi/Pic/ZhuJiaYi/'
output_path = '../result/compare_twins/tencent/'
output_path1 = '../result/compare_twins/tencent/ZhuJiaWen/'
output_path2 = '../result/compare_twins/tencent/ZhuJiaYi/'
if not os.path.exists(output_path):
    os.makedirs(output_path)
tencent = Tencent()
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')

num = 100
confidence1 = 0.0
confidence2 = 0.0

confidence1 = MyCompare(path1,path1,output_path1,output_path1,num,confidence1,result_file)
confidence1 = MyCompare(path2,path2,output_path2,output_path2,num,confidence1,result_file)
confidence2 = MyCompare(path1,path2,output_path1,output_path2,num*2,confidence2,result_file)

print("confidence1: "+str(confidence1/num/2))
print("confidence2: "+str(confidence2/num/2))
result_file.flush()
result_file.close()