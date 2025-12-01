python -u -m torch.distributed.launch --nnodes=1 --nproc_per_node=1 --node_rank=0 --master_port=16005 \
./train.py --datapath "datasets" \
           --benchmark pascal \
           --fold 0 \
           --bsz 4 \
           --nworker 4 \
           --backbone resnet50 \
           --feature_extractor_path "backbones/resnet50_a1h-35c100f8.pth" \
           --logpath "./logs" \
           --lr 1e-3 \
           --nepoch 50 \
           --use_original_imgsize
