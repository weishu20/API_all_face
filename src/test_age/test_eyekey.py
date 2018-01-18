import os
import sys
import cv2
import time
import math
import scipy.io as sio
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_eyekey import Eyekey
from utils.base import draw_face_rectangle


path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/'
output_path = '../result/age/eyekey/'
label_path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/wiki.mat'
data = sio.loadmat(label_path)
pathA  =data.get("wiki")[0][0][2][0][0:500]
genderA = data.get("wiki")[0][0][3][0][0:500]

label ={"1.0":"Male",
        "0.0":"Female",
        "nan":"nan"}
eyekey = Eyekey()
if not os.path.exists(output_path):
    os.makedirs(output_path)
file_name = output_path+"age.txt"
result_file = open(file_name, 'a+')
count_a = 0
count_g = 0
total = 0
j = 0
mse = 0
while j < 500:
    time.sleep(1)
    fn = path + pathA[j][0]
    print(fn)
    img = cv2.imread(fn)
    result = eyekey.detect(fn)
    try:
        faces = result['face']
        for i in range(len(faces)):
            gender = faces[i]["attribute"]["gender"]
            age = faces[i]["attribute"]["age"]

            real_age = int(pathA[j][0].split("_")[2][0:4])-int(pathA[j][0].split("_")[1].split("-")[0])
            real_gender = label[str(genderA[j])]
            print(gender,real_gender , age, real_age)
            if real_age == age:
                count_a += 1
            if gender == real_gender:
                count_g += 1
            mse += math.pow(real_age-age,2)
            buf =str(j)+" " +fn + "  pre_gender:" + str(gender) + "  real_gender:" + str(real_gender) + "  pre_age:" + str(age)+ "  real_age:" + str(real_age) + "\n"
            result_file.writelines(buf)
            total += 1
        j += 1
    except:
        print("error")
        try:
            buf = str(j)+" " + fn + " : " + result["message"] + "\n"
            result_file.writelines(buf)
            j += 1
        except:
            buf = str(j) + " " + fn + " : 404 " + "\n"
            result_file.writelines(buf)
            j += 1

print(count_a,count_g,total)
print(count_a*1.0/total, count_g*1.0/total)
print(mse*1.0/total)
result_file.flush()
result_file.close()