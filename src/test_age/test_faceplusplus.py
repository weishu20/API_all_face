import os
import sys
import cv2
import time
import math
import scipy.io as sio
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_faceplusplus import FacePlusPlus,FaceSet,Face
from utils.base import draw_face_rectangle


path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/'
output_path = '../result/age/faceplusplus/'
label_path = '/home/shushi/Pic/IMDB-WIKI/wiki_crop/wiki.mat'
data = sio.loadmat(label_path)
pathA  =data.get("wiki")[0][0][2][0][0:500]
genderA = data.get("wiki")[0][0][3][0][0:500]

label ={"1.0":"Male",
        "0.0":"Female",
        "nan":"nan"}
faceplus = FacePlusPlus()
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
    result = faceplus.detect(fn,return_attributes="gender,age")
    out_dir = output_path + pathA[j][0][0:2]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    try:
        faces = result['faces']
        if len(faces) != 0:
            draw_face_rectangle(faces,img,output_path + pathA[j][0])
            for i in range(len(faces)):
                genderJ = faces[i]["attributes"]["gender"]
                ageJ = faces[i]["attributes"]["age"]
                gender = genderJ["value"]
                age = ageJ["value"]
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
        else:
            buf = str(j) + " " + fn + ": no face" + "\n"
            result_file.writelines(buf)
        j += 1
    except:
        print("error")
        if result["error_message"]=="CONCURRENCY_LIMIT_EXCEEDED":
            continue
        else:
            buf = str(j)+" " + fn + result["error_message"] + "\n"
            result_file.writelines(buf)
            j += 1



print(count_a,count_g,total)
print(count_a*1.0/total, count_g*1.0/total)
print(mse*1.0/total)
result_file.flush()
result_file.close()