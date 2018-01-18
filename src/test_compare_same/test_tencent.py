import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_tencent import Tencent

path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_same/tencent/'
tencent = Tencent()
if not os.path.exists(output_path):
    os.makedirs(output_path)
file_name = output_path+"compare.txt"
result_file = open(file_name, 'a+')
confidence  = 0.0
total = 0
file_paths = os.listdir(path)[0:20]
for j in range(len(file_paths)):
    file_path = path + file_paths[j]+"/"
    files = os.listdir(file_path)
    file1 = file_path+files[0]
    k = 1
    while k < len(files):
        file2 = file_path + files[k]
        print(file1, file2)
        result = tencent.compare(file1, file2)
        if result != {}:
            if result["code"] == 0:
                similarity = result["data"]["similarity"]
                buf = file1 + " vs " + file2 + "\n" + "similarity: " + str(similarity) + "\n"
                confidence += similarity
                result_file.writelines(buf)
                total += 1
                k += 1
            else:
                print("error")
                if result["code"] == -1101 or result["code"] == -1305:
                    fail_flag = result["data"]["fail_flag"]
                    if fail_flag == 1:
                        img1 = cv2.imread(file1)
                        file_outpath1 = output_path + file_paths[j] + "/"
                        print(file_outpath1)
                        if not os.path.exists(file_outpath1):
                            os.makedirs(file_outpath1)
                        cv2.imwrite(file_outpath1 + files[0], img1)
                        buf = file1 + " :" + result["message"] + "\n"
                        result_file.writelines(buf)
                    else:
                        img2 = cv2.imread(file2)
                        file_outpath2 = output_path + file_paths[j] + "/"
                        print(file_outpath2)
                        if not os.path.exists(file_outpath2):
                            os.makedirs(file_outpath2)
                        cv2.imwrite(file_outpath2 + files[k], img2)
                        buf = file2 + " :" + result["message"] + "\n"
                        result_file.writelines(buf)
                    k += 1
                elif result["code"] == 15 or result["code"] == 213:
                    continue
                else:
                    buf = file1 + " vs " + file2 + " " + result["message"] + "\n"
                    result_file.writelines(buf)
                    k += 1
        else:
            continue

print(str(confidence/total))
result_file.flush()
result_file.close()
