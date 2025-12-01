import os
import tarfile
import shutil
import scipy.io
import numpy as np
from PIL import Image
from tqdm import tqdm

def extract_tar(tar_path, extract_path):
    print(f"Extracting {tar_path}...")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_path)
    print("Extraction complete.")

def prepare_pascal():
    voc_tar = 'datasets/PASCAL_VOC_2012/VOCtrainval_11-May-2012.tar'
    # SBD is downloaded by torchvision to datasets/sbd
    sbd_root = 'datasets/sbd' 
    
    # Extract VOC
    if not os.path.exists('datasets/PASCAL_VOC_2012/VOCdevkit/VOC2012'):
        extract_tar(voc_tar, 'datasets/PASCAL_VOC_2012')
    
    voc_root = 'datasets/PASCAL_VOC_2012/VOCdevkit/VOC2012'
    target_dir = os.path.join(voc_root, 'SegmentationClassAug')
    os.makedirs(target_dir, exist_ok=True)
    
    print("Processing SBD annotations...")
    # SBD annotations are in datasets/sbd/cls
    sbd_cls_dir = os.path.join(sbd_root, 'cls')
    
    # Copy VOC annotations first
    voc_seg_dir = os.path.join(voc_root, 'SegmentationClass')
    for filename in tqdm(os.listdir(voc_seg_dir), desc="Copying VOC"):
        if filename.endswith('.png'):
            shutil.copy(os.path.join(voc_seg_dir, filename), os.path.join(target_dir, filename))
            
    # Process SBD annotations (they are .mat files)
    # torchvision downloads SBD to datasets/sbd/benchmark_RELEASE/dataset/cls
    # Let's find where it actually is after download finishes
    # Assuming standard structure
    
    # We will run this part after download finishes
    pass

if __name__ == '__main__':
    prepare_pascal()
