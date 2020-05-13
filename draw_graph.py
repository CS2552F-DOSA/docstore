import numpy as np
import matplotlib.pyplot as mplt
import math

from matplotlib.backends.backend_pdf import PdfPages


# pdf = PdfPages('des_file_name.pdf')


# dimension = [1, 5, 10, 50, 100, 500, 1000, 2000]
# # compressed_time = [] # microseconds
# # de_compressed_time = []

# # compressed_size = []
# # compressed_ratio = []

# # compressed_data_rate = [] # mb/s
# # de_compressed_ratio = [] # mb/s

# # gorilla compression

# dimension = [1, 5, 10, 64, 100, 500, 1000, 2000]
# compressed_time1 = [16611, 44026, 76672,
#                     438504, 681674, 3385909, 6905494, 13867785]
# compressed_time1 = [item / (10 ** 6) for item in compressed_time1]
# de_compressed_time1 = [12885, 25922, 41495,
#                        184721, 273168, 1284334, 2903435, 5173882]
# de_compressed_time1 = [item / (10 ** 6) for item in de_compressed_time1]

# compressed_size1 = [87848, 374526, 732984,
#                     4605051, 7186568, 35870806, 71725572, 143432729]
# compressed_size1 = [item / (10 ** 6) for item in compressed_size1]
# compressed_ratio1 = [2.3313, 1.64047, 1.53673,
#                      1.44537, 1.43913, 1.4302, 1.42909, 1.42856]

# compressed_data_rate1 = [12.3292, 13.9554,
#                          14.6912, 15.1789, 15.1721, 15.1517, 14.8436, 14.7754]
# decompressed_data_rate1 = [15.8945, 23.7019,
#                            27.1454, 36.0327, 37.861, 39.9447, 35.3038, 39.6032]

# small file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
equivalence_data_rate = [109.66567492748771, 155.54926190222304, 360.8001352945454, 1026.4528843128792,
                         1469.680660208109, 2832.4237009544727, 7135.534237766162, 6826.521417231918, 13098.227714015899, 14418.521973292385]
avg_wall_time_post = [0.009730786085128784, 0.010060800446404351, 0.010080728530883789, 0.010908617692835191,
                      0.011781817390805199, 0.010342690077694979, 0.01040374791180646, 0.009830611817380215, 0.009767753737313407, 0.01026493130308209]
avg_wall_time_get = [0.010991036891937256, 0.011313083171844483, 0.01122492790222168, 0.011552472114562989, 0.012135641574859619,
                     0.011155095100402832, 0.011095385551452636, 0.010722799301147461, 0.011451082229614258, 0.010948750972747803]

# small file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
equivalence_data_rate = []
delta_data_rate = []
avg_wall_time_post = []
avg_wall_time_get = []

# middle file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
equivalence_data_rate = [1093.3602391585232, 1549.2351933471703, 3569.056390361087, 10301.625928617546,
                         14508.710523084217, 29881.329835880915, 65073.46079852864, 93296.36152767167, 149344.50367640393, 194540.47686833702]
avg_wall_time_post = [0.011124687535422189, 0.010797013839085897, 0.01064179539680481, 0.010283021365894991, 0.010417551829897124,
                      0.010592626802849047, 0.010785893031529019, 0.01041783889134725, 0.011291098594665528, 0.009860763947168985]
avg_wall_time_get = [0.011895878314971924, 0.011400468349456787, 0.010941574573516846, 0.011097769737243652, 0.011019721031188964,
                     0.0108654522895813, 0.010730087757110596, 0.011204841136932374, 0.012500851154327393, 0.010982799530029296]

# middle file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
equivalence_data_rate = []
delta_data_rate = []
avg_wall_time_post = []
avg_wall_time_get = []


# large file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]

equivalence_data_rate = [10930.838607154536, 15569.469596869594, 36103.96537325542, 102185.33730965114,
                         144368.37219420233, 313607.46632654994, 821488.9962389877, 677005.9377748476, 929942.1774057723, 1542200.1195725154]
avg_wall_time_post = [0.012769203919630785, 0.01321872381063608, 0.013043729882491263, 0.012825942808581937,
                      0.013624362945556641, 0.013364040851593017, 0.012605088097708566, 0.012703657150268555, 0.013540008488823385, 0.01252685546875]
avg_wall_time_get = [0.012287945747375488, 0.012277476787567139, 0.012703912258148193, 0.012191905975341796,
                     0.012280492782592774, 0.012859435081481933, 0.012797636985778809, 0.01218264102935791, 0.0125789213180542, 0.012289159297943116]

# large file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
equivalence_data_rate = []
delta_data_rate = []
avg_wall_time_post = []
avg_wall_time_get = []


# test_0_ratio_1 = [1.43913]
# test_1_ratio_1 = [1.63106]
# test_2_ratio_1 = [11.5562]
# test_3_ratio_1 = [4.88582]
# test_4_ratio_1 = [5.36213]
# test_5_ratio_1 = [6.24631]
# test_6_ratio_1 = [3.60651]
# test_7_ratio_1 = [5.27342]
# test_8_ratio_1 = [2.33795]


# test_0_compression_speed_1 = [14.9452]
# test_1_compression_speed_1 = [17.9407]
# test_2_compression_speed_1 = [53.6276]
# test_3_compression_speed_1 = [33.6774]
# test_4_compression_speed_1 = [49.3843]
# test_5_compression_speed_1 = [38.3083]
# test_6_compression_speed_1 = [27.8271]
# test_7_compression_speed_1 = [50.5827]
# test_8_compression_speed_1 = [18.9642]

# test_0_decompression_speed_1 = [36.9746]
# test_1_decompression_speed_1 = [44.1788]
# test_2_decompression_speed_1 = [97.0161]
# test_3_decompression_speed_1 = [71.8731]
# test_4_decompression_speed_1 = [93.5363]
# test_5_decompression_speed_1 = [81.629]
# test_6_decompression_speed_1 = [63.1906]
# test_7_decompression_speed_1 = [93.5405]
# test_8_decompression_speed_1 = [50.562]

# # middleout compression column order

# dimension = [1, 5, 10, 64, 100, 500, 1000, 2000]

# compressed_time2 = [19197, 57462, 101288,
#                     598465, 955485, 4599711, 9207579, 18883207]

# compressed_time2 = [item / (10 ** 6) for item in compressed_time2]
# de_compressed_time2 = [16218, 40192, 53066,
#                        234252, 356014, 1624529, 3231087, 6539149]
# de_compressed_time2 = [item / (10 ** 6) for item in de_compressed_time2]

# compressed_size2 = [113258, 451347, 873740,
#                     5437413, 8479525, 42280632, 84532286, 169033321]
# compressed_size2 = [item / (10 ** 6) for item in compressed_size2]
# compressed_ratio2 = [1.80826, 1.36126, 1.28917,
#                      1.22411, 1.21969, 1.21338, 1.21258, 1.2122]

# compressed_data_rate2 = [10.6683, 10.6923,
#                          11.1208, 11.1218, 10.8242, 11.1534, 11.1324, 10.851]
# decompressed_data_rate2 = [12.6279, 15.2866,
#                            21.2264, 28.4138, 29.0505, 31.5799, 31.7238, 31.3347]

# test_0_ratio_2 = [1.21969]
# test_1_ratio_2 = [1.30825]
# test_2_ratio_2 = [4.75608]
# test_3_ratio_2 = [2.97592]
# test_4_ratio_2 = [4.87255]
# test_5_ratio_2 = [3.6032]
# test_6_ratio_2 = [2.6537]
# test_7_ratio_2 = [4.65443]
# test_8_ratio_2 = [1.73786]


# test_0_compression_speed_2 = [11.4987]
# test_1_compression_speed_2 = [12.2912]
# test_2_compression_speed_2 = [37.0923]
# test_3_compression_speed_2 = [25.3618]
# test_4_compression_speed_2 = [38.6652]
# test_5_compression_speed_2 = [29.838]
# test_6_compression_speed_2 = [22.6402]
# test_7_compression_speed_2 = [38.273]
# test_8_compression_speed_2 = [15.9293]

# test_0_decompression_speed_2 = [30.2927]
# test_1_decompression_speed_2 = [31.6845]
# test_2_decompression_speed_2 = [68.1367]
# test_3_decompression_speed_2 = [40.1445]
# test_4_decompression_speed_2 = [66.8377]
# test_5_decompression_speed_2 = [59.608]
# test_6_decompression_speed_2 = [51.0582]
# test_7_decompression_speed_2 = [68.1277]
# test_8_decompression_speed_2 = [37.9224]

# # middleout compression row order

# dimension = [1, 5, 10, 64, 100, 500, 1000, 2000]

# compressed_time3 = [23241, 57108, 102560,
#                     568498, 888915, 4427654, 9080194, 17906841]
# compressed_time3 = [item / (10 ** 6) for item in compressed_time3]

# de_compressed_time3 = [19272, 29877, 50456,
#                        208477, 309453, 1509173, 2987363, 5960578]
# de_compressed_time3 = [item / (10 ** 6) for item in de_compressed_time3]

# compressed_size3 = [113258, 451408, 873930,
#                     5436268, 8479204, 42280079, 84534952, 169034096]
# compressed_size3 = [item / (10 ** 6) for item in compressed_size3]
# compressed_ratio3 = [1.80826, 1.36107, 1.28889,
#                      1.22437, 1.21974, 1.21339, 1.21254, 1.2122]

# compressed_data_rate3 = [8.81201, 10.7586,
#                          10.9828, 11.708, 11.6349, 11.5868, 11.2886, 11.4427]
# decompressed_data_rate3 = [10.6268, 20.5643,
#                            22.3244, 31.9268, 33.4216, 33.9937, 34.312, 34.3763]

# test_0_ratio_3 = [1.21974]
# test_1_ratio_3 = [4.58692]
# test_2_ratio_3 = [2.69062]
# test_3_ratio_3 = [2.38914]
# test_4_ratio_3 = [4.45457]
# test_5_ratio_3 = [4.85052]
# test_6_ratio_3 = [2.99425]
# test_7_ratio_3 = [4.98294]
# test_8_ratio_3 = [2.54536]


# test_0_compression_speed_3 = [11.8108]
# test_1_compression_speed_3 = [40.2444]
# test_2_compression_speed_3 = [24.484]
# test_3_compression_speed_3 = [22.4155]
# test_4_compression_speed_3 = [41.1977]
# test_5_compression_speed_3 = [40.5779]
# test_6_compression_speed_3 = [27.4065]
# test_7_compression_speed_3 = [45.3911]
# test_8_compression_speed_3 = [23.9257]

# test_0_decompression_speed_3 = [34.1703]
# test_1_decompression_speed_3 = [87.791]
# test_2_decompression_speed_3 = [61.9662]
# test_3_decompression_speed_3 = [59.2425]
# test_4_decompression_speed_3 = [84.8398]
# test_5_decompression_speed_3 = [98.1518]
# test_6_decompression_speed_3 = [67.868]
# test_7_decompression_speed_3 = [93.1387]
# test_8_decompression_speed_3 = [59.9379]


mplt.figure()
mplt.xlabel('Test Type')
mplt.ylabel('Decompressin Speed (MB/sec)')
name_list = ['Data1', 'Data2', 'Data3', 'Data4',
             'Data5', 'Data6', 'Data7', 'Data8', 'Data9']
x = list(range(len(name_list)))
num_list1 = [36.9746, 44.1788, 97.0161, 71.8731,
             93.5363, 81.629, 63.1906, 93.5405, 50.562]
num_list2 = [30.2927, 31.6845, 68.1367, 40.1445,
             66.8377, 59.608, 51.0582, 68.1277, 37.9224]
num_list3 = [34.1703, 87.791, 61.9662, 59.2425,
             84.8398, 98.1518, 67.868, 93.1387, 59.9379]

total_width, n = 0.8, 3
width = total_width / n
#tick_label = name_list

mplt.bar(x, num_list1, width=width, label='Gorilla')
for i in range(len(x)):
    x[i] = x[i] + width

mplt.bar(x, num_list2, width=width,
         label='Middle-Out Column Order', tick_label=name_list)
for i in range(len(x)):
    x[i] = x[i] + width

mplt.bar(x, num_list3, width=width,
         label='Middle-Out Row Order')
# mplt.title('Compressed time for different dimension with Gorilla, Middle-Out Column Order, and Middle-Out Row Order')

# mplt.plot(dimension, decompressed_data_rate1, label="Gorilla")
# mplt.plot(dimension, decompressed_data_rate2, label="Middle-Out Column Order")
# mplt.plot(dimension, decompressed_data_rate3,
#           label="Middle-Out Row Order")
mplt.ylim((0, 128))
mplt.legend()
mplt.savefig(
    fname="/Users/tiancan/Desktop/test_decompressin_speed.pdf", format="pdf")
mplt.show()


# pdf.savefig(mplt)
mplt.close()
# pdf.close()
