from torchvision.datasets import SBDataset

print("Downloading SBD...")
# This will download to datasets/sbd
try:
    dataset = SBDataset(root='datasets', image_set='train', mode='segmentation', download=True)
    print("Download complete.")
except Exception as e:
    print(f"Download failed: {e}")
