from common.api_linkface import Linkface,FaceSet
import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from utils.base import draw_face_rectangle
path = '/home/shushi/Pic/jaffeimages.KDEF/jaffe_img/'
output_path = '../result/emotion/linkface/'
linkface = Linkface()
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
    img = cv2.imread(fn)
    result = linkface.attribute(fn)
    try:
        smile = result['smile']
        angry = result['angry']
        male = result['male']
        emotion = "neutral"
        if male < 0.5:
            count_g += 1
        if smile > 0.5:
            emotion = "happiness"
        if angry > 0.5:
            emotion = "anger"
        real_emo = files[j][3:5]
        if real_emo == label[emotion]:
            count_e += 1
        print(male, emotion, real_emo)

        buf = fn + "  :" + male + "  :" + emotion + "\n"
        result_file.writelines(buf)
        total += 1
        j += 1
    except:
        print("error")
        if result["status"] == "OUT_OF_QUOTA":
            continue
        else:
            buf = fn + result["status"] + "\n"
            result_file.writelines(buf)
            j += 1

print("count_e: "+str(count_e)+" count_g: "+str(count_g)+" total: "+str(total))
print("count_e*1.0/total: "+count_e*1.0/total," count_g*1.0/total: "+ count_g*1.0/total)
result_file.flush()
result_file.close()