import os
import sys
import cv2
import time
sys.path.append(r"/home/shushi/projects/3face/face_api/src")
from common.api_faceplusplus import FacePlusPlus,FaceSet,Face
from utils.base import draw_face_rectangle

# path1 = '/home/shushi/Pic/test_image.jpg'
faceplus = FacePlusPlus()
# faceset = FaceSet("b2d995a194ccc021a3284b27c3c51a45")
# faceset_token = faceset.faceset_token
# req_dict = faceplus.detect(path1)
# face_tokens = []
# faces = req_dict['faces']
# for face in faces:
#     face_tokens.append(face['face_token'])
# print(face_tokens)
#
# face_token0 = face_tokens[0]
# face_token1 = face_tokens[1]
# face_token_str = ','.join(face_tokens[:4])
#
# faceset.addFace_faceSet(face_token_str)
#

# faceplus.compare("4c8a15d449c1e7aa92e995073f2ef059","4c8a15d449c1e7aa92e995073f2ef059",is_file=1)
faceplus.compare("4c8a15d449c1e7aa92e995073f2ef059","611b1efc78642f721365d68186ebcb29",is_file=1)
# faceplus.compare("4c8a15d449c1e7aa92e995073f2ef059","df40b2692f179ebb50fa1c69201c7132",is_file=1)
faceplus.compare("4c8a15d449c1e7aa92e995073f2ef059","e19bb0155eeb45c2200f23f9cb7da9b5",is_file=1)
# faceplus.search(face_token0,faceset_token,4)

