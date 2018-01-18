import os
import sys
import cv2
import time
import math
import scipy.io as sio
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_baidu import Baidu
from utils.base import draw_face_rectangle_baidu


path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/'
output_path = '../result/age/baidu/'
label_path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/wiki.mat'
data = sio.loadmat(label_path)
pathA  =data.get("wiki")[0][0][2][0][0:500]
genderA = data.get("wiki")[0][0][3][0][0:500]

label ={"1.0":"male",
        "0.0":"female",
        "nan":"nan"}
baidu = Baidu()
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
    result = baidu.detect(fn, face_fields="gender,age")
    out_dir = output_path + pathA[j][0][0:2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    try:
        result_num = result["result_num"]
        faces = result['result']
        if result_num != 0:
            draw_face_rectangle_baidu(faces,img,output_path + pathA[j][0])
            gender = faces[0]["gender"]
            age = faces[0]["age"]
            real_age = int(pathA[j][0].split("_")[2][0:4])-int(pathA[j][0].split("_")[1].split("-")[0])
            real_gender = label[str(genderA[j])]
            print(gender,real_gender , age, real_age)
            if real_age == age:
                count_a += 1
            if gender == real_gender:
                count_g += 1
            mse += math.pow(real_age-age,2)
            buf =str(j)+" " +fn + "\n  pre_gender:" + str(gender) + "  real_gender:" + str(real_gender) + "  pre_age:" + str(age)+ "  real_age:" + str(real_age) + "\n"
            result_file.writelines(buf)
            total += 1
        else:
            buf = str(j) + " " + fn + " : no face" + "\n"
            result_file.writelines(buf)
        j += 1
    except:
        print("error")
        if result["error_code"]==18:
            continue
        else:
            buf = str(j)+" " + fn +" "+ result["error_msg"] + "\n"
            result_file.writelines(buf)
            j += 1



print(count_a,count_g,total)
print(count_a*1.0/total, count_g*1.0/total)
print(mse*1.0/total)
result_file.flush()
result_file.close()