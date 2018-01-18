import os
import sys
import cv2
import time
import math
import scipy.io as sio
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_tencent import Tencent
from utils.base import draw_face_rectangle_tencent


path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/'
output_path = '../result/age/tencent/'
label_path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/wiki.mat'
data = sio.loadmat(label_path)
pathA  =data.get("wiki")[0][0][2][0][0:500]
genderA = data.get("wiki")[0][0][3][0][0:500]

tencent = Tencent()
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
    fn = path + pathA[j][0]
    print(fn)
    img = cv2.imread(fn)
    result = tencent.detect(fn)
    out_dir = output_path + pathA[j][0][0:2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    faces = result['data']["face"]
    draw_face_rectangle_tencent(faces, img, output_path + pathA[j][0])
    if result["code"] == 0:
        gender = str(faces[0]["gender"])
        age = faces[0]["age"]
        real_age = int(pathA[j][0].split("_")[2][0:4])-int(pathA[j][0].split("_")[1].split("-")[0])
        real_gender = str(genderA[j])
        if int(gender)>50:
            gender = "1.0"
        else:
            gender = "0.0"
        print(gender,real_gender , age, real_age)
        if real_age == age:
            count_a += 1
        if gender == real_gender:
            count_g += 1
        mse += math.pow(real_age-age,2)
        buf =str(j)+" " +fn + "\n  pre_gender:" + str(gender) + "  real_gender:" + str(real_gender) + "  pre_age:" + str(age)+ "  real_age:" + str(real_age) + "\n"
        result_file.writelines(buf)
        total += 1
        j += 1
    else:
        print("error")
        if result["code"]==15 or result["code"]==213 :
            continue
        else:
            buf = str(j)+" " + fn +" "+ result["message"] + "\n"
            result_file.writelines(buf)
            j += 1



print(count_a,count_g,total)
print(count_a*1.0/total, count_g*1.0/total)
print(mse*1.0/total)
result_file.flush()
result_file.close()