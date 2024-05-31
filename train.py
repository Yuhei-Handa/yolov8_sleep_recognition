from ultralytics import YOLO

def train(model_name):
    # モデルの初期化
    model = YOLO(model_name)

    data_path = "C:/Users/user/VScode/python/neoti/yolov8_sleep_recognition/config.yaml"

    # モデルの学習
    model.train(data=data_path, epochs=500, patience=50, batch=8, imgsz=640, save=True,
                device="cuda:0", verbose=True, val=True)

    print('学習が完了しました。')

def main():
    # モデルの学習
    model_name = 'yolov8n'
    train(model_name)

if __name__ == '__main__':
    main()