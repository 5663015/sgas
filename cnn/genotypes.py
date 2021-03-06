from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]

NASNet = Genotype(
  normal = [
    ('sep_conv_5x5', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 0),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 0),
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
  ],
  normal_concat = [2, 3, 4, 5, 6],
  reduce = [
    ('sep_conv_5x5', 1),
    ('sep_conv_7x7', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('sep_conv_5x5', 0),
    ('skip_connect', 3),
    ('avg_pool_3x3', 2),
    ('sep_conv_3x3', 2),
    ('max_pool_3x3', 1),
  ],
  reduce_concat = [4, 5, 6],
)

AmoebaNet = Genotype(
  normal = [
    ('avg_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 2),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 3),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 1),
    ],
  normal_concat = [4, 5, 6],
  reduce = [
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('max_pool_3x3', 0),
    ('sep_conv_7x7', 2),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('max_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('conv_7x1_1x7', 0),
    ('sep_conv_3x3', 5),
  ],
  reduce_concat = [3, 4, 6]
)

# ****************************  SGAS CRITERION 1  ****************************** #
# Experiment  Validation error (%)  Params (M)  Test error (%)  Evaluation ranking
# Cri1_CIFAR_1       16.94             3.75         2.44                 2
Cri1_CIFAR_1 = Genotype(normal=[('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))
# Cri1_CIFAR_2       17.33             3.73         2.50                 3
Cri1_CIFAR_2 = Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
# Cri1_CIFAR_3       17.90             3.80         2.39                 1
Cri1_CIFAR_3 = Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('sep_conv_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 1)], reduce_concat=range(2, 6))
# Cri1_CIFAR_4       17.90             3.32         2.63                 6
Cri1_CIFAR_4 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('dil_conv_3x3', 2), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri1_CIFAR_5       17.99             3.45         2.78                 8
Cri1_CIFAR_5 = Genotype(normal=[('dil_conv_5x5', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('avg_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri1_CIFAR_6       18.43             3.47         2.68                 7
Cri1_CIFAR_6 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('skip_connect', 1), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 3), ('skip_connect', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
# Cri1_CIFAR_7       18.72             3.83         2.51                 4
Cri1_CIFAR_7 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 1), ('dil_conv_5x5', 3), ('avg_pool_3x3', 0), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))
# Cri1_CIFAR_8       19.82             3.66         2.61                 5
Cri1_CIFAR_8 = Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))
# Cri1_CIFAR_9       19.93             3.98         3.18                 10
Cri1_CIFAR_9 = Genotype(normal=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 1), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri1_CIFAR_10      21.53             3.61         2.87                 9
Cri1_CIFAR_10 = Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))

Cri1_CIFAR_Best = Cri1_CIFAR_3
# -------------------------------------------------------------------------------#

# Experiment        Test error top-1 (%)  Test error top-5 (%)  Params (M)  ×+
# Cri1_ImageNet_1           24.47                 7.23            5.25      578
Cri1_ImageNet_1 = Cri1_CIFAR_1
# Cri1_ImageNet_2           24.53                 7.40            5.23      574
Cri1_ImageNet_2 = Cri1_CIFAR_2
# Cri1_ImageNet_3           24.22                 7.25            5.29      585
Cri1_ImageNet_3 = Cri1_CIFAR_3

Cri1_ImageNet_Best = Cri1_ImageNet_3
# ****************************  SGAS CRITERION 1  ****************************** #


# ****************************  SGAS CRITERION 2  ****************************** #
# Experiment  Validation error (%)  Params (M)  Test error (%)  Evaluation ranking
# Cri2_CIFAR_1       16.48             4.14         2.57                 4
Cri2_CIFAR_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_2       17.26             3.88         2.60                 6
Cri2_CIFAR_2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('sep_conv_5x5', 1), ('sep_conv_3x3', 2), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 1)], reduce_concat=range(2, 6))
# Cri2_CIFAR_3       17.31             4.09         2.44                 1
Cri2_CIFAR_3 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_4       17.47             3.91         2.49                 2
Cri2_CIFAR_4 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('avg_pool_3x3', 1)], reduce_concat=range(2, 6))
# Cri2_CIFAR_5       17.53             3.69         2.52                 3
Cri2_CIFAR_5 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 2), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('skip_connect', 1), ('max_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 3), ('max_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_6       17.98             3.95         3.12                 10
Cri2_CIFAR_6 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('dil_conv_5x5', 2), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_5x5', 3), ('max_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_7       18.28             3.69         2.58                 5
Cri2_CIFAR_7 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 1), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_8       18.28             4.33         2.85                 8
Cri2_CIFAR_8 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('skip_connect', 2)], reduce_concat=range(2, 6))
# Cri2_CIFAR_9       19.48             3.73         2.85                 9
Cri2_CIFAR_9 = Genotype(normal=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 1), ('dil_conv_3x3', 3), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 2), ('sep_conv_3x3', 3), ('avg_pool_3x3', 0), ('max_pool_3x3', 1)], reduce_concat=range(2, 6))
# Cri2_CIFAR_10      19.98             3.68         2.66                 7
Cri2_CIFAR_10 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3), ('max_pool_3x3', 0), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('sep_conv_5x5', 0), ('skip_connect', 2), ('max_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))

Cri2_CIFAR_Best = Cri2_CIFAR_3
# -------------------------------------------------------------------------------#

# Experiment        Test error top-1 (%)  Test error top-5 (%)  Params (M)  ×+
# Cri2_ImageNet_1           24.44                 7.41            5.70      621
Cri2_ImageNet_1 = Cri2_CIFAR_3
# Cri2_ImageNet_2           24.13                 7.31            5.44      598
Cri2_ImageNet_2 = Cri2_CIFAR_4
# Cri2_ImageNet_3           24.55                 7.44            5.20      571
Cri2_ImageNet_3 = Cri2_CIFAR_5

Cri2_ImageNet_Best = Cri2_ImageNet_2
# ****************************  SGAS CRITERION 2  ****************************** #




v2_8_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 3), ('skip_connect', 2), ('dil_conv_5x5', 4), ('skip_connect', 3)], reduce_concat=range(2, 6))
v2_8_2 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1)], reduce_concat=range(2, 6))
v2_8_3 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 3), ('max_pool_3x3', 0), ('dil_conv_5x5', 3), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_4 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_5 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 2), ('skip_connect', 1), ('dil_conv_5x5', 4), ('dil_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('avg_pool_3x3', 0), ('dil_conv_5x5', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_6 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 3), ('skip_connect', 0), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('skip_connect', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_7 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 3), ('skip_connect', 0), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('skip_connect', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_8 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('skip_connect', 2), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
v2_8_9 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 3), ('skip_connect', 2), ('skip_connect', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_10 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 3), ('skip_connect', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
v2_8_11 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 3), ('sep_conv_5x5', 2), ('sep_conv_3x3', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
v2_8_12 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_13 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('dil_conv_3x3', 2), ('skip_connect', 3), ('skip_connect', 2), ('skip_connect', 4)], reduce_concat=range(2, 6))
v2_8_14 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 3), ('skip_connect', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v2_8_15 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_3x3', 3), ('skip_connect', 0), ('dil_conv_3x3', 3), ('sep_conv_3x3', 0)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('avg_pool_3x3', 1), ('skip_connect', 2), ('skip_connect', 3), ('skip_connect', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))


v5_0 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 3), ('dil_conv_3x3', 2), ('dil_conv_5x5', 4), ('dil_conv_5x5', 2)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v5_0_1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                  reduce=[('max_pool_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
v5_1 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 3), ('dil_conv_5x5', 4)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('sep_conv_3x3', 2), ('avg_pool_3x3', 0), ('dil_conv_3x3', 3), ('dil_conv_3x3', 3), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
v5_2 = Genotype(normal=[('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_3x3', 3), ('dil_conv_5x5', 1), ('dil_conv_3x3', 3), ('dil_conv_5x5', 4)], normal_concat=range(2, 6),
				reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 2)], reduce_concat=range(2, 6))
v5_3 = Genotype(normal=[('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('dil_conv_3x3', 2), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v5_4 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 3), ('sep_conv_5x5', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 1), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
v5_5 = Genotype(normal=[('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 1), ('dil_conv_5x5', 3), ('sep_conv_3x3', 1), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
v5_6 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6),
                reduce=[('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('dil_conv_3x3', 3), ('max_pool_3x3', 0), ('dil_conv_5x5', 4), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v5_7 = Genotype(normal=[('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('sep_conv_5x5', 1), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_3x3', 2), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))

v11_0 = Genotype(normal=[('sep_conv_5x5', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                 reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 2), ('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 3), ('avg_pool_3x3', 0), ('skip_connect', 3)], reduce_concat=range(2, 6))
v11_1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 1), ('dil_conv_5x5', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6),
                 reduce=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
v11_2 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), ('dil_conv_3x3', 3), ('dil_conv_3x3', 2), ('dil_conv_5x5', 4), ('dil_conv_3x3', 2)], normal_concat=range(2, 6),
                 reduce=[('avg_pool_3x3', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('dil_conv_5x5', 3), ('avg_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
v11_3 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 3), ('avg_pool_3x3', 0)], reduce_concat=range(2, 6))
v11_4 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('dil_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
v11_5 = Genotype(normal=[('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_5x5', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 3), ('skip_connect', 2), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))
v11_6 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 3), ('skip_connect', 0), ('dil_conv_5x5', 4), ('sep_conv_3x3', 1)], normal_concat=range(2, 6),
                reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))
v11_10 = Genotype(normal=[('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
                    reduce=[('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))
v11_11 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('dil_conv_5x5', 3), ('dil_conv_5x5', 4), ('dil_conv_5x5', 3)], normal_concat=range(2, 6),
                reduce=[('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 3), ('dil_conv_5x5', 4), ('skip_connect', 2)], reduce_concat=range(2, 6))
v11_12 = Genotype(normal=[('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 0), ('skip_connect', 1), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 3), ('avg_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
v11_13 = Genotype(normal=[('sep_conv_3x3', 1), ('dil_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_5x5', 4), ('sep_conv_3x3', 1)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 3), ('avg_pool_3x3', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))
v11_14 = Genotype(normal=[('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_5x5', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_5x5', 4), ('dil_conv_3x3', 2)], normal_concat=range(2, 6),
                reduce=[('avg_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('skip_connect', 3), ('avg_pool_3x3', 1), ('avg_pool_3x3', 1), ('dil_conv_3x3', 4)], reduce_concat=range(2, 6))
v11_15 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('skip_connect', 0), ('dil_conv_5x5', 3), ('skip_connect', 0), ('dil_conv_5x5', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
				reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('avg_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))
v11_16 = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4), ('dil_conv_3x3', 3)], normal_concat=range(2, 6),
				reduce=[('max_pool_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('avg_pool_3x3', 1), ('skip_connect', 3), ('avg_pool_3x3', 1), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))

#-------------------------
# NoisyDARTS
# ------------------------
# factor = 0.6
s2_0 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 4), ('skip_connect', 2)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('sep_conv_3x3', 4), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))
s2_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 2), ('skip_connect', 1), ('sep_conv_3x3', 4)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
s2_2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 1), ('sep_conv_3x3', 4), ('skip_connect', 1)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
# factor = 0.7
s2_factor07_0 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 2), ('sep_conv_3x3', 4), ('skip_connect', 1)], normal_concat=range(2, 6),
                        reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
# factor = 0.8
s2_factor08_0 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 4), ('skip_connect', 1)], normal_concat=range(2, 6),
                         reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))

# factor=1.
s2_factor1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4), ('skip_connect', 1)], normal_concat=range(2, 6),
                      reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))

# factor = 0.6
s3_0 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))
s3_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))
s3_2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1)], reduce_concat=range(2, 6))
# factor = 1.
s3_factor1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                      reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))
s3_factor1_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                        reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
s3_factor1_2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                       reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))

# factor = 0.8
s3_factor09_0 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                         reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1)], reduce_concat=range(2, 6))
s3_factor09_1 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('skip_connect', 1)], normal_concat=range(2, 6),
                         reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1)], reduce_concat=range(2, 6))



# early stop
s5_es_0 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('sep_conv_3x3', 4), ('sep_conv_3x3', 2)], normal_concat=range(2, 6),
                   reduce=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 1), ('sep_conv_5x5', 4), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))
s5_es_1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 3), ('sep_conv_5x5', 4)], normal_concat=range(2, 6),
                   reduce=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 3), ('dil_conv_3x3', 2), ('dil_conv_3x3', 4), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))

# nohup python -u train.py --auxiliary --cutout --arch v11_14 --exp_name full_train_v11_14 --gpu 5 > full_train_v11_14.log 2>&1 &