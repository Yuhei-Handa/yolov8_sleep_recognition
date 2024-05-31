import numpy as np
import cv2
from glob import glob
import os




#動画からフレーム画像を抽出する関数
#一つの動画から任意の数のフレームを抽出する
def output_frame(num_frame):

    data_dir = './video_data'

    output_dir = './dataset'

    print(output_dir)

    train_video_dir_list = glob(os.path.join(data_dir, 'train') + '/*' + '/*.mp4')
    valid_video_dir_list = glob(os.path.join(data_dir, 'val') + '/*' + '/*.mp4')
    test_video_dir_list = glob(os.path.join(data_dir, 'test') + '/*' + '/*.mp4')

    print('train_video_dir_list:', train_video_dir_list)

    #画像ファイルの出力先   
    train_frame_dir = os.path.join(output_dir, 'images', 'train')
    valid_frame_dir = os.path.join(output_dir, 'images', 'val')
    test_frame_dir = os.path.join(output_dir, 'images', 'test')

    print('フレーム画像の出力を開始します。')

    #動画ファイルをフレーム画像に変換

    #訓練データ
    video2frame(train_video_dir_list, train_frame_dir, num_frame)

    #検証データ
    video2frame(valid_video_dir_list, valid_frame_dir, num_frame)

    #テストデータ
    video2frame(test_video_dir_list, test_frame_dir, num_frame)


    print('フレーム画像の出力が完了しました。')


#動画からフレーム画像を等間隔に抽出する関数
def video2frame(video_dir_list, frame_dir, num_frame=10):
    for video_dir in video_dir_list:
        cap = cv2.VideoCapture(video_dir)
        if not cap.isOpened():
            print('Error: Could not open video.')
            return

        frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = int(frame_num / num_frame)

        for i in range(num_frame):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_rate)
            ret, frame = cap.read()
            if ret:
                frame_name = os.path.splitext(os.path.basename(video_dir))[0] + '_frame' + str(i) + '.jpg'
                frame_path = os.path.join(frame_dir, frame_name)
                cv2.imwrite(frame_path, frame)
            else:
                print('Error: Could not read frame.')
                break


        cap.release()

def main():
    output_frame(20)

if __name__ == '__main__':
    main()