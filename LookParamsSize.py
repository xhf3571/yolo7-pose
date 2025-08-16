import torch
from torchsummary import summary
from thop import profile
from models import Model  # 确保这里正确导入了YOLOv7的模型定义

# 加载模型，这里假设模型定义在'models.py'中并且类名为Model
model = Model(cfg="path_to_your_model_config.yaml", ch=3, nc=80)  # cfg是YOLOv7的配置文件路径
model.eval()

# 为summary和profile设置输入张量的大小
input_tensor = torch.randn(1, 3, 640, 640)  # 假设输入大小为640x640

# 使用torchsummary查看参数
summary(model, (3, 640, 640))

# 使用thop计算FLOPs和参数量
flops, params = profile(model, inputs=(input_tensor, ), verbose=False)

print(f"Floating Point Operations (FLOPs): {flops / 1e9:.3f} G")
print(f"Trainable parameters: {params / 1e6:.3f} M")
