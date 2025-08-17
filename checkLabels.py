import os

# 硬编码：从你提供的日志中提取的所有因 "negative labels" 被忽略的图像路径
corrupted_image_paths = [
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/100822.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/100948.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/102560.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103049.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103090.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103225.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103233.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103289.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103910.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/103977.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/104528.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/104587.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/104816.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/104866.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/105883.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/105956.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/106127.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/106302.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/106414.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/106812.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/107041.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/107559.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/107560.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/108271.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/108377.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/108414.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/108638.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/109304.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/111047.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/111363.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/112146.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/116132.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/117113.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/117208.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/117287.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/117651.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/118342.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/118525.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/118530.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/118976.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/train/images/119453.jpg",
    # 验证集
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/100151.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/101893.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/102255.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/102362.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/103628.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/103676.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/114864.jpg",
    "/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/val/images/104056.jpg""??? 开始删除日志中提到的损坏文件...")

for image_path in corrupted_image_paths:
    # 推导标签文件路径
    if "train/images" in image_path:
        label_path = image_path.replace("train/images", "train/labels").replace(".jpg", ".txt")
    elif "val/images" in image_path:
        label_path = image_path.replace("val/images", "val/labels").replace(".jpg", ".txt")
    else:
        print(f"??  无法识别路径: {image_path}")
        continue

    # 删除图像文件
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"? 已删除图像: {image_path}")
    else:
        print(f"?? 图像未找到 (可能已删除): {image_path}")

