#!/bin/bash

python ./lid.py 1000000 256 /home/dataset/deep1m-256/deep.bin 8 sub_lids_deep1m256.txt

python ./lid.py 60000 512 /home/dataset/cifar60k-512/cifar.bin 8 sub_lids_cifar60k512.txt

# python ./lid.py 1000000 96 /home/dataset/sift1m/sift.bin 8 sub_lids_sift1m96.txt

python ./lid.py 1000000 960 /home/dataset/gist1m-960/gist.bin 8 sub_lids_gist1m960.txt

python ./lid.py 2300000 150 /home/dataset/imagenet2.3m-150/imagenet.bin 8 sub_lids_imagenet2.3m150.txt

python ./lid.py 1000000 420 /home/dataset/msong1m-420/msong.bin 8 sub_lids_msong1m420.txt

python ./lid.py 60000 784 /home/dataset/mnist60k-784/mnist.bin 8 sub_lids_mnist60k784.txt