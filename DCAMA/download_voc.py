import torchvision
from torchvision.datasets import VOCSegmentation

print("Downloading VOC 2012...")
# This will download to datasets/PASCAL_VOC_2012/VOCdevkit/VOC2012
dataset = VOCSegmentation(root='datasets/PASCAL_VOC_2012', year='2012', image_set='trainval', download=True)
print("Download complete.")
