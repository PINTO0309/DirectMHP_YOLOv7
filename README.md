# DirectMHP_YOLOv7
I just replaced the DirectMHP backend from YOLOv5 to YOLOv7. The reason is that YOLOv5 and YOLOv8 have a problem accepting some input shapes that are multiples of 32.

# Acknowledgments
1. https://github.com/hnuzhy/DirectMHP
2. https://github.com/WongKinYiu/yolov7

# Data preparation

# Results
## 1. YOLOv7-tiny + CMU-Panoptic 5000 epoch
### RTX3080: 16GB
```
$ python train.py \
--workers 8 \
--device 0 \
--epochs 5000 \
--batch-size 96 \
--data data/cmu_panoptic_coco.yaml \
--img-size 640 640 \
--cfg cfg/training/yolov7-tiny_cmupanoptic_head.yaml \
--weights 'yolov7-tiny.pt' \
--name yolov7_tiny \
--hyp data/hyp.scratch.tiny.yaml \
--mse_conf_thre 0.40 \
--mse_loss_w 0.10

     Epoch   gpu_mem       box       obj       cls     total    labels  img_size
 1199/1199     14.5G   0.01066  0.004235         0   0.01346       409       640
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95
                 all       16216       32738       0.992       0.978       0.994       0.784
left bbox number: 31935 / 32738; MAE: 7.9602, [pitch_err, yaw_err, roll_err]: 8.8929, 7.2529, 7.7348
left backward bbox number: 16067 / 31935; MAE: 8.6401, [pitch_err, yaw_err, roll_err]: 9.3878, 8.3266, 8.2057
left frontal bbox number: 15868 / 31935; MAE: 7.2718, [pitch_err, yaw_err, roll_err]: 8.3917, 6.1657, 7.2581
```

## 2. Single GPU YOLOv7 training
```
# A100 RAM:40GB
# 640x640 training
# --img-size 640 640 -> train_size=640,test_size=640
# --name: save to project/name
python train.py \
--workers 12 \
--device 0 \
--epochs 5000 \
--batch-size 64 \
--data data/cmu_panoptic_coco.yaml \
--img-size 640 640 \
--cfg cfg/training/yolov7_cmupanoptic_head.yaml \
--weights 'yolov7.pt' \
--name yolov7_tiny \
--hyp data/hyp.scratch.tiny.yaml \
--mse_conf_thre 0.40 \
--mse_loss_w 0.10

   Epoch   gpu_mem       box       obj       cls     total    labels  img_size
596/4999     40.2G   0.01745  0.004293         0   0.03101       257       640
             Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95
               all       16216       32738       0.991       0.976       0.994       0.806
left bbox number: 32025 / 32738; MAE: 7.5712, [pitch_error, yaw_error, roll_error]: 8.3896, 6.989, 7.3351
left backward bbox number: 16060 / 32025; MAE: 8.2652, [pitch_err, yaw_err, roll_err]: 8.7852, 8.4, 7.6103
left frontal bbox number: 15965 / 32025; MAE: 6.8732, [pitch_err, yaw_err, roll_err]: 7.9916, 5.5697, 7.0583
```

## 3. ONNX export
```
python export.py \
--weights runs/train/last.pt \
--img-size 480 640 \
--grid

onnxsim runs/train/last.onnx runs/train/last.onnx
onnxsim runs/train/last.onnx runs/train/last.onnx
onnxsim runs/train/last.onnx runs/train/last.onnx
```
![image](https://github.com/PINTO0309/DirectMHP_YOLOv7/assets/33194443/f354b20a-1442-4672-b7f4-8bdc658865bb)

