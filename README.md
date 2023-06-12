# DirectMHP_YOLOv7
I just replaced the DirectMHP backend from YOLOv5 to YOLOv7.

# Acknowledgments
1. https://github.com/hnuzhy/DirectMHP
2. https://github.com/WongKinYiu/yolov7

# Data preparation

# Results
## 1. YOLOv7-tiny + CMU-Panoptic 300 epoch
```
  Epoch   gpu_mem       box       obj       cls     total    labels  img_size
299/299     37.5G   0.01288  0.004909         0   0.01878       251       640
            Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95
              all       16216       32738       0.988       0.974       0.993       0.793

left box num: 31938 / 32738; MAE: 8.5607, [pitch, yaw, roll]: 9.4997, 7.9325, 8.2497
left backward box num: 16100 / 31938; MAE: 9.2062, [pitch, yaw, roll]: 10.091, 8.9266, 8.6009
left frontal box num: 15838 / 31938; MAE: 7.9045, [pitch, yaw, roll]: 8.8988, 6.9219, 7.8927
```
