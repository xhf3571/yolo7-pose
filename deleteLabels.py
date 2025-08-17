import os
import re

log_file = r'/home/disk/xuhaifeng/yolov7-pose/log.txt'  # 你的日志文件名

# 用于匹配图片路径
pattern = re.compile(r'/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/test/images/\d+\.(jpg|png)')

deleted = 0

with open(log_file, 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            img_path = match.group()
            # 标签路径
            base = os.path.splitext(os.path.basename(img_path))[0]
            label_path = f"/home/disk/xuhaifeng/yolov7-pose/dataset/crowdpose/test/labels/{base}.txt"
            if os.path.isfile(img_path):
                os.remove(img_path)
                print(f"Deleted image: {img_path}")
            if os.path.isfile(label_path):
                os.remove(label_path)
                print(f"Deleted label: {label_path}")
            deleted += 1

print(f"\nTotal deleted: {deleted}")