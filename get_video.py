import rtsp
import cv2
from onvif import ONVIFCamera
import time
import requests
from requests.auth import HTTPDigestAuth
import time
import PySimpleGUI as sg
from glob import glob
import os
import json
import shutil

def get_output_video_dir(output_dir, train_status, awake_status, shirt_color, pant_color):
    video_path_per_status = os.path.join(output_dir, train_status, awake_status)
    if not os.path.exists(video_path_per_status):
        os.makedirs(video_path_per_status)

    #既存の動画ファイルを取得
    files = glob(video_path_per_status + "/*.mp4")
    if len(files) == 0:
        new_number = str(0).zfill(2)
    else:
        max_number = 0
        for file in files:
            number = int(file[-6:-4])
            if number > max_number:
                max_number = number
        new_number = str(max_number + 1).zfill(2)

        #新しいファイル名を作成
    output_video_dir = os.path.join(video_path_per_status,
                                     train_status + "_" + 
                                     awake_status + "_" + 
                                     shirt_color + "_" +
                                     pant_color + "_" +
                                     new_number + ".mp4")
    return output_video_dir

directory = "video_data"


is_neoti = 0
frame_list = []
#最高録画時間は4時間
over_time = 60

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640) 
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
original_fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_dir = get_output_video_dir(directory, "test", "sleep", "white", "blue")
print(output_video_dir)
out = cv2.VideoWriter(output_video_dir, fourcc, original_fps, (width, height), isColor=True)



frame_count = 0

print("start")

time.sleep(3)

print("record")

start_time = time.time()
while True:

    ret, frame = cap.read()

    current_time = time.time()  # 現在時刻を取得
    elapsed_time = current_time - start_time  # 経過時間を計算

    # 画像を保存
    frame_list.append(frame)

    if elapsed_time > over_time:
        break

for frame in frame_list:
     out.write(frame)

print(len(frame_list))

cap.release()
out.release()
