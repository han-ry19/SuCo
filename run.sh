./suco --dataset-path /home/dataset/deep1m-256/deep.bin --query-path /home/jiuqi/MESSI-RangeQuery/benchmark/query_deep1m_size100.bin \
 --groundtruth-path /home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_deep1m_size100_50knn.bin --dataset-size 1000000 --query-size 100 \
 --k-size 50 --data-dimensionality 256 --subspace-dimensionality 32 --subspace-num 8 --candidate-ratio 0.005 --collision-ratio 0.05 \
 --kmeans-num-centroid 50 --kmeans-num-iters 2 --index-path deep1m_index.bin --subspace-lid /home/ruoyu/SuCo/sub_lids_deep1m256.txt

 ./suco --dataset-path /home/dataset/cifar60k-512/cifar.bin --query-path /home/jiuqi/MESSI-RangeQuery/benchmark/query_cifar60k_size100.bin \
 --groundtruth-path /home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_cifar60k_size100_50knn.bin --dataset-size 60000 --query-size 100 \
 --k-size 50 --data-dimensionality 512 --subspace-dimensionality 64 --subspace-num 8 --candidate-ratio 0.005 --collision-ratio 0.05 \
 --kmeans-num-centroid 50 --kmeans-num-iters 2 --index-path cifar60k_index.bin --subspace-lid /home/ruoyu/SuCo/sub_lids_cifar60k512.txt

 ./suco --dataset-path /home/dataset/gist1m-960/gist.bin --query-path /home/jiuqi/MESSI-RangeQuery/benchmark/query_gist1m_size100.bin \
 --groundtruth-path /home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_gist1m_size100_50knn.bin --dataset-size 1000000 --query-size 100 \
 --k-size 50 --data-dimensionality 960 --subspace-dimensionality 120 --subspace-num 8 --candidate-ratio 0.005 --collision-ratio 0.05 \
 --kmeans-num-centroid 50 --kmeans-num-iters 2 --index-path gist1m_index.bin --subspace-lid /home/ruoyu/SuCo/sub_lids_gist1m960.txt

 ./suco --dataset-path /home/dataset/mnist60k-784/mnist.bin --query-path /home/jiuqi/MESSI-RangeQuery/benchmark/query_mnist60k_size100.bin \
 --groundtruth-path /home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_mnist60k_size100_50knn.bin --dataset-size 60000 --query-size 100 \
 --k-size 50 --data-dimensionality 784 --subspace-dimensionality 98 --subspace-num 8 --candidate-ratio 0.005 --collision-ratio 0.05 \
 --kmeans-num-centroid 50 --kmeans-num-iters 2 --index-path mnist60k_index.bin --subspace-lid /home/ruoyu/SuCo/sub_lids_mnist60k784.txt

 ./suco --dataset-path /home/dataset/msong1m-420/msong.bin --query-path /home/jiuqi/MESSI-RangeQuery/benchmark/query_msong1m_size100.bin \
 --groundtruth-path /home/jiuqi/MESSI-RangeQuery/benchmark/benchmark_msong1m_size100_50knn.bin --dataset-size 1000000 --query-size 100 \
 --k-size 50 --data-dimensionality 420 --subspace-dimensionality 52 --subspace-num 8 --candidate-ratio 0.005 --collision-ratio 0.05 \
 --kmeans-num-centroid 50 --kmeans-num-iters 2 --index-path msong1m_index.bin --subspace-lid /home/ruoyu/SuCo/sub_lids_msong1m420.txt