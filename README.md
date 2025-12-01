# Dense Cross-Query-and-Support Attention Weighted Mask Aggregation for Few-Shot Segmentation

Esta é a implementação do código para o artigo da ECCV'2022 "Dense Cross-Query-and-Support Attention Weighted Mask Aggregation for Few-Shot Segmentation".

<p align="middle">
    <img src="DCAMA/assets/architecture.png">
</p>

## Requisitos

- Python 3.7
- PyTorch 1.5.1
- cuda 10.1
- tensorboard 1.14

Configurações do ambiente Conda:

```bash
conda create -n DCAMA python=3.7
conda activate DCAMA

conda install pytorch=1.5.1 torchvision cudatoolkit=10.1 -c pytorch
conda install -c conda-forge tensorflow
pip install tensorboardX
```

## Preparação dos Datasets

Baixe as imagens e anotações de treino/validação do COCO2014:

```bash
wget http://images.cocodataset.org/zips/train2014.zip
wget http://images.cocodataset.org/zips/val2014.zip
wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip
```

Baixe as anotações de treino/validação do COCO2014 do Google Drive: [[train2014.zip](https://drive.google.com/file/d/1fcwqp0eQ_Ngf-8ZE73EsHKP8ZLfORdWR/view?usp=sharing)], [[val2014.zip](https://drive.google.com/file/d/16IJeYqt9oHbqnSI9m2nTXcxQWNXCfiGb/view?usp=sharing)]. (e localize ambos train2014/ e val2014/ dentro do diretório annotations/).

Crie um diretório 'datasets' e coloque o coco apropriadamente para ter a seguinte estrutura de diretórios:

    datasets/
        └── COCO2014/           
            ├── annotations/
            │   ├── train2014/  # (dir.) máscaras de treino (do Google Drive) 
            │   ├── val2014/    # (dir.) máscaras de validação (do Google Drive)
            │   └── ..alguns arquivos json..
            ├── train2014/
            └── val2014/

## Preparação dos Backbones

Baixe os seguintes backbones pré-treinados:

> 1. [ResNet-50](https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/resnet50_a1h-35c100f8.pth) pré-treinado no ImageNet-1K por [TIMM](https://github.com/rwightman/pytorch-image-models)
> 2. [ResNet-101](https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/resnet101_a1h-36d3f2aa.pth) pré-treinado no ImageNet-1K por [TIMM](https://github.com/rwightman/pytorch-image-models)
> 3. [Swin-B](https://github.com/SwinTransformer/storage/releases/download/v1.0.0/swin_base_patch4_window12_384_22kto1k.pth) pré-treinado no ImageNet por [Swin-Transformer](https://github.com/microsoft/Swin-Transformer)

Crie um diretório 'backbones' para colocar os backbones acima. A estrutura geral do diretório deve ser assim:

    ../                         # diretório pai
    ├── DCAMA/                  # diretório atual (projeto)
    │   ├── common/             # (dir.) funções auxiliares
    │   ├── data/               # (dir.) dataloaders e splits para cada dataset FSS
    │   ├── model/              # (dir.) implementação do DCAMA
    │   ├── scripts/            # (dir.) Scripts para treino e teste
    │   ├── README.md           # instrução para reprodução
    │   ├── train.py            # código para treino
    │   └── test.py             # código para teste
    ├── datasets/               # (dir.) Datasets de Few-Shot Segmentation
    └── backbones/              # (dir.) Backbones pré-treinados

## Treino e Teste

Você pode usar nossos scripts para construir o seu próprio. O treino levará aprox. 1.5 dias até a convergência (treinado com quatro GPUs V100). Para mais informações, consulte ./common/config.py

> ```bash
> sh ./scripts/train.sh
> ```
> 
> - Para cada experimento, um diretório que registra o progresso do treino será gerado automaticamente sob o diretório logs/. 
> - Do terminal, execute 'tensorboard --logdir logs/' para monitorar o progresso do treino.
> - Escolha o melhor modelo quando a curva de validação (mIoU) começar a saturar. 

Para testes, você deve preparar um modelo pré-treinado. Você pode treinar um você mesmo ou apenas baixar nossos [modelos pré-treinados](https://drive.google.com/drive/folders/1vEw35yKoWkuDgkrclJPNSXeDtsTOVy_c?usp=sharing). 
> ```bash
> sh ./scripts/test.sh
> ```

## Licença e Citação

Este repositório contém código relacionado ao artigo original. Todos os direitos e créditos são atribuídos aos autores originais. Se você utilizar este trabalho, por favor cite o artigo original:

```
@inproceedings{shi2022dense,
  title={Dense Cross-Query-and-Support Attention Weighted Mask Aggregation for Few-Shot Segmentation},
  author={Shi, Xinyu and Wei, Dong and Zhang, Yu and Lu, Donghuan and Ning, Munan and Chen, Jiashun and Ma, Kai and Zheng, Yefeng},
  booktitle={European Conference on Computer Vision},
  pages={151--168},
  year={2022},
  organization={Springer}
}
```
