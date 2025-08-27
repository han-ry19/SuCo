# -*- coding: UTF-8 -*-
import struct
import os
import sys
import gc
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import ctypes
import skdim
from tqdm import tqdm

if __name__ == '__main__':

    # 参数设置，判断是否已经有相应文件并执行后续操作
    cardinality = 1000000
    dim = 256
    filepath = '/home/dataset/deep1m-256/deep.bin'
    # querypath = '/home/jiuqi/MESSI-RangeQuery/benchmark/query_deep1m_size100.bin'
    # querynum = 100
    # query_k = 50
    # benchmarkpath = '/home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_deep1m_size100_50knn.bin'
    subspace_num = 8
    # subspace_dimensionality = 32
    output_name = 'sub_lids_deep1m.txt'

    if len(sys.argv) == 6:
        cardinality = int(sys.argv[1])
        dim = int(sys.argv[2])
        filepath = sys.argv[3]
        # querypath = sys.argv[4]
        # querynum = int(sys.argv[5])
        # query_k = int(sys.argv[6])
        # benchmarkpath = sys.argv[7]
        subspace_num = int(sys.argv[4])
        # subspace_dimensionality = int(sys.argv[9])
        output_name = sys.argv[5]
    elif len(sys.argv) != 6 and len(sys.argv) != 0:
        print('input error,input num is %d' %(len(sys.argv)))
        sys.exit(1)
    
    subspace_dimensionality = dim // subspace_num
    flag = 0
    last_subspace_dimensionality = subspace_dimensionality
    
    if dim % subspace_num != 0:
        flag = 1
        last_subspace_dimensionality = dim % subspace_num
        print('Warning: the last subspace dimensionality is %d' %(last_subspace_dimensionality))
        
    # 读取数据
    data = np.fromfile(filepath, dtype=np.float32, count=cardinality*dim)
    print('Finish loading data and now reshape it')
    data = data.reshape(-1,dim)
    print('dataset size is [%d, %d]' %(len(data), len(data[0])))

    #estimate global intrinsic dimension
    # danco = skdim.id.DANCo().fit(data)
    # # print('Finish estimate global intrinsic dimension')

    # # estimate local intrinsic dimension (dimension in k-nearest-neighborhoods around each point):
    # lpca = skdim.id.lPCA().fit_pw(data,
    #                             n_neighbors = 100,
    #                             n_jobs = 128)
    
    # tle = skdim.id.TLE().fit(data, n_neighbors = 100, n_jobs = 128)
    batch_size = 5000
    dataset_size = data.shape[0]
    
    subspace_lids = []

    for k in range(subspace_num):
        if k == subspace_num - 1 and flag == 1:
            subspace_dimensionality = last_subspace_dimensionality
        start = k * subspace_dimensionality
        end = (k+1) * subspace_dimensionality
        subspace = data[:, start:end]  # shape = (dataset_size, subspace_dimensionality)
        
        print(f"\nCalculating LID for subspace {k} (shape={subspace.shape})")
        all_lids = []

        for i in tqdm(range(0, dataset_size, batch_size), desc=f"LID batch progress (subspace {k})"):
            batch = subspace[i:i+batch_size]
            ess = skdim.id.ESS().fit(batch, n_jobs=64)
            all_lids.append(ess.dimension_pw_)

        all_lids = np.concatenate(all_lids)
        sub_lids = np.mean(all_lids)
        subspace_lids.append(sub_lids)
        
        print(f"Subspace {k} mean LID: {sub_lids}")
        
    with open(output_name, 'w') as f:
        for k in range(subspace_num):
            mean_lid = subspace_lids[k]   
            f.write(f"Subspace {k} mean LID: {mean_lid:.4f}\n")
            f.flush()  # 及时写入磁盘



