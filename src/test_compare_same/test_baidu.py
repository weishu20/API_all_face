import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_baidu import Baidu

path = '/home/shushi/Pic/idealtest/idealtest/'
output_path = '../result/campare_same/baidu/'
baidu = Baidu()
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
        time.sleep(1)
        file2 = file_path + files[k]
        result = baidu.compare(file1, file2)
        print(file1, file2)
        try:
            result_num = result["result_num"]
            if result_num != 0:
                faces = result['result'][0]
                buf = file1 + " vs " + file2 + "\n" + "score: " + str(faces["score"]) + "\n"
                confidence += faces["score"]
                result_file.writelines(buf)
                total += 1
            else:
                buf = file1 + " vs " + file2 + " : no face"+ "\n"
                result_file.writelines(buf)
            k += 1
        except:
            print("error")
            if result["error_code"] == 18:
                continue
            else:
                buf = file1 + " vs " + file2 + " " + result["error_code"] + "\n"
                result_file.writelines(buf)
                k += 1

print(str(confidence/total))
result_file.flush()
result_file.close()
