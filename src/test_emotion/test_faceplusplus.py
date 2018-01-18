import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_faceplusplus import FacePlusPlus,FaceSet,Face
from utils.base import draw_face_rectangle
#gender
path = '/home/shushi/Pic/jaffeimages.KDEF/jaffe_img/'
output_path = '../result/emotion/faceplusplus/'
faceplus = FacePlusPlus()
if not os.path.exists(output_path):
    os.makedirs(output_path)
files = os.listdir(path)

file_name = output_path+"emotion.txt"
result_file = open(file_name,'a+')
label = {
    "anger":"AN",
    "disgust":"DI",
    "fear":"FE",
    "happiness":"HA",
    "neutral":"NE",
    "sadness":"SA",
    "surprise":"SU"
}
count_e = 0
count_g = 0
total = 0
print(files)
j = 0
while j < len(files):
    time.sleep(1)
    fn = path + files[j]
    print(fn)
    img = cv2.imread(fn)
    result = faceplus.detect(fn, return_attributes="gender,emotion")
    try:
        faces = result['faces']
        if len(faces) != 0:
            draw_face_rectangle(faces,img,output_path+files[j])
            print(len(faces))
            for i in range(len(faces)):
                genderJ = faces[i]["attributes"]["gender"]
                emotionJ = faces[i]["attributes"]["emotion"]
                emotion = sorted(emotionJ.items(), key=lambda d: d[1])[len(emotionJ) - 1][0]
                gender = genderJ["value"]
                real_emo = files[j][3:5]
                print(gender, emotion, real_emo)
                if real_emo == label[emotion]:
                    count_e += 1
                if gender == "Female":
                    count_g += 1
                buf = fn + "  :" + gender + "  :" + emotion + "\n"
                result_file.writelines(buf)
                total += 1
        else:
            buf = fn + ": no face" + "\n"
            result_file.writelines(buf)
        j += 1
    except:
        print("error")
        if result["error_message"] == "CONCURRENCY_LIMIT_EXCEEDED":
            continue
        else:
            buf = fn + result["error_message"] + "\n"
            result_file.writelines(buf)
            j += 1


print(count_e*1.0/total, count_g*1.0/total)
result_file.flush()
result_file.close()