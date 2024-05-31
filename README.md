# yolov8_sleep_recognition

yolov8を使用した寝落ち検出モデル。

精度は全クラスのmAP 0.995, mAP50-95 0.819と良好であった。

以下はデータセット取得の手順である。

（１）データセットはwebカメラ（BRIO 500）を使用。フレームサイズ：640 × 640とする。

（2）起床時、睡眠時の動画（１分）を録画する。服装の違いで推論結果が変わらないよう、異なる服装でも同じ動作を行うよう注意を払う。
　　　服装の組み合わせごとに、訓練動画：評価動画：テスト動画を3:2:1の割合（動画の枚数）で取得している。ここでは、10秒ごとに異なる動作をしている。

（3）動画から一定時間ごとにフレームを抽出する（ここでは10秒ごと）。そのため一つ動画から6枚の異なる動作のフレームが抽出できる。
　　　私のデータセットでは訓練データ：評価データ：テストデータを720:480:240枚とした。

（4）取得した画像ファイルをlabelImgを使用して、アノテーションを行う。

### 1.混合行列（awake=起床、sleep=睡眠, background=背景、未検出）
![confusion_matrix](https://github.com/Yuhei-Handa/yolov8_sleep_recognition/assets/135846516/6bb1c0a5-d164-4f9a-9110-7768bd576dbb)

### 2. PR曲線（曲線の下領域の面積が大きいほど性能が良い）
![PR_curve](https://github.com/Yuhei-Handa/yolov8_sleep_recognition/assets/135846516/fa8c763a-18b7-4168-8ba3-3fd6c4d1110b)

### 3. 各評価指標の推移（エポック）
![results](https://github.com/Yuhei-Handa/yolov8_sleep_recognition/assets/135846516/cefc08f5-8535-4215-915a-69df3cd07a19)

### 4. 訓練データのバウンディボックス（0=起床、1=睡眠：服装の違いで推論結果が変化しないよう注意）
![train_batch2](https://github.com/Yuhei-Handa/yolov8_sleep_recognition/assets/135846516/9961bfa1-9506-44f1-ac62-d6a9375e52a4)

### 5. 推論結果（バウンディボックス、信頼度）
![val_batch2_pred](https://github.com/Yuhei-Handa/yolov8_sleep_recognition/assets/135846516/4fef837f-80ff-485c-824e-4c60c1dc4a63)
