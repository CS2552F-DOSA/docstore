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

# small file size, directly on storage envoy.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
on_storage_equivalence_data_rate = [108.57140891194037, 154.46200656846818, 352.34272448207946, 972.7831896086774,
                                    1355.0634903175962, 2713.284527077686, 5271.098345803501, 6100.791458632996, 6575.183975374162, 8704.65437532925]

on_storage_avg_wall_time_post = [0.007255661487579346, 0.006662466526031494, 0.006679782867431641, 0.007126448154449463,
                                 0.0061804413795471195, 0.00574897289276123, 0.0059486889839172365, 0.006028683185577393, 0.007605113983154297, 0.006353206634521484]
on_storage_avg_wall_time_get = [0.005902416706085205, 0.005486769676208496, 0.005516247749328613, 0.005951163768768311,
                                0.004996566772460937, 0.0047922968864440914, 0.004919826984405518, 0.005001764297485351, 0.006124455928802491, 0.005283710956573487]

# middle file size, directly on storage envoy.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
on_storage_equivalence_data_rate = [1086.5905378959174, 1543.8204497301451, 3511.551641621979, 9807.8167357303,
                                    13347.69783365734, 25619.95303959871, 48326.01470833613, 56553.73426412688, 67766.18913477717, 80721.99218648714]

on_storage_avg_wall_time_post = [0.006845855712890625, 0.006843259334564209, 0.0075415754318237304, 0.006680982112884521,
                                 0.006904442310333252, 0.007186408042907715, 0.007147772312164307, 0.0069037508964538575, 0.007367372512817383, 0.00698838472366333]
on_storage_avg_wall_time_get = [0.005495004653930664, 0.005674831867218018, 0.00571026086807251, 0.005474457740783692,
                                0.005506772994995118, 0.00574887752532959, 0.00561429500579834, 0.005546777248382568, 0.0058649110794067386, 0.005638632774353027]


# large file size, directly on storage envoy.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
on_storage_equivalence_data_rate = [10823.591700333673, 15345.017322076204, 34741.0903720564, 94102.52797518781,
                                    126832.81842677401, 233885.70340257388, 415600.22829602385, 460021.90484400635, 555257.0719861832, 623225.4342918319]

on_storage_avg_wall_time_post = [0.009708876609802247, 0.010090200901031495, 0.009952700138092041, 0.010095591545104981,
                                 0.009995119571685791, 0.0100641131401062, 0.009705967903137207, 0.010068507194519042, 0.010055925846099854, 0.009998228549957276]
on_storage_avg_wall_time_get = [0.006589622497558594, 0.006754868030548096, 0.006675243377685547, 0.0067981863021850586,
                                0.006733222007751465, 0.006967406272888183, 0.006761775016784668, 0.006843397617340088, 0.006754717826843262, 0.0066518855094909665]


# small file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
without_diff_equivalence_data_rate = [109.66567492748771, 155.54926190222304, 360.8001352945454, 1026.4528843128792,
                                      1469.680660208109, 2832.4237009544727, 7135.534237766162, 6826.521417231918, 13098.227714015899, 14418.521973292385]
without_diff_avg_wall_time_post = [0.009730786085128784, 0.010060800446404351, 0.010080728530883789, 0.010908617692835191,
                                   0.011781817390805199, 0.010342690077694979, 0.01040374791180646, 0.009830611817380215, 0.009767753737313407, 0.01026493130308209]
without_diff_avg_wall_time_get = [0.010991036891937256, 0.011313083171844483, 0.01122492790222168, 0.011552472114562989, 0.012135641574859619,
                                  0.011155095100402832, 0.011095385551452636, 0.010722799301147461, 0.011451082229614258, 0.010948750972747803]

# middle file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
without_diff_equivalence_data_rate = [1093.3602391585232, 1549.2351933471703, 3569.056390361087, 10301.625928617546,
                                      14508.710523084217, 29881.329835880915, 65073.46079852864, 93296.36152767167, 149344.50367640393, 194540.47686833702]
without_diff_avg_wall_time_post = [0.011124687535422189, 0.010797013839085897, 0.01064179539680481, 0.010283021365894991, 0.010417551829897124,
                                   0.010592626802849047, 0.010785893031529019, 0.01041783889134725, 0.011291098594665528, 0.009860763947168985]
without_diff_avg_wall_time_get = [0.011895878314971924, 0.011400468349456787, 0.010941574573516846, 0.011097769737243652, 0.011019721031188964,
                                  0.0108654522895813, 0.010730087757110596, 0.011204841136932374, 0.012500851154327393, 0.010982799530029296]

# large file size, modification without file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]

without_diff_equivalence_data_rate = [10930.838607154536, 15569.469596869594, 36103.96537325542, 102185.33730965114,
                                      144368.37219420233, 313607.46632654994, 821488.9962389877, 677005.9377748476, 929942.1774057723, 1542200.1195725154]
without_diff_avg_wall_time_post = [0.012769203919630785, 0.01321872381063608, 0.013043729882491263, 0.012825942808581937,
                                   0.013624362945556641, 0.013364040851593017, 0.012605088097708566, 0.012703657150268555, 0.013540008488823385, 0.01252685546875]
without_diff_avg_wall_time_get = [0.012287945747375488, 0.012277476787567139, 0.012703912258148193, 0.012191905975341796,
                                  0.012280492782592774, 0.012859435081481933, 0.012797636985778809, 0.01218264102935791, 0.0125789213180542, 0.012289159297943116]

# small file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
with_diff_equivalence_data_rate = [107.1991339948944, 151.39663776225592, 337.1035649585148, 869.5419636999234,
                                   1133.783557818322, 1987.1547642064656, 3094.393419709483, 3448.7954975124558, 3725.504106922406, 3785.9743141729987]
with_diff_delta_data_rate = [2.143982679897888, 3.0279327552451187, 6.742071299170298, 17.39083927399847, 22.675671156366445,
                             39.74309528412932, 61.887868394189674, 68.97590995024913, 74.51008213844814, 75.71948628345999]
with_diff_avg_wall_time_post = [0.013430838584899902, 0.012040871381759643, 0.012342588901519775, 0.01256730079650879, 0.013850221633911133,
                                0.01345512866973877, 0.01331497311592102, 0.013556511402130126, 0.013148270845413208, 0.013464205265045166]
with_diff_avg_wall_time_get = [0.01347468137741089, 0.01247637629508972, 0.012585538625717162, 0.012649372816085816, 0.013559309244155883,
                               0.013302607536315918, 0.01324500799179077, 0.013247655630111694, 0.013280625343322755, 0.013424750566482544]


# middle file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
with_diff_equivalence_data_rate = [1071.1793622848302, 1518.2523308135574, 3385.3640445694964, 8784.772572726763,
                                   11292.529489510958, 19380.617930329936, 30087.542899959844, 32540.36695981413, 37378.22828778165, 39442.136401409465]
with_diff_delta_data_rate = [21.423587245696602, 30.365046616271147, 67.70728089138993, 175.69545145453526,
                             225.85058979021915, 387.6123586065987, 601.7508579991969, 650.8073391962827, 747.564565755633, 788.8427280281894]

with_diff_avg_wall_time_post = [0.01307267665863037, 0.013205207586288452, 0.013112626075744628, 0.013143527507781982, 0.013723211288452148,
                                0.012520102262496948, 0.012666409015655517, 0.012444920539855957, 0.0131941556930542, 0.014142385721206664]
with_diff_avg_wall_time_get = [0.013055015802383423, 0.013363107442855834, 0.013196589946746827, 0.01335985541343689, 0.013297070264816285,
                               0.012835425138473511, 0.01288175344467163, 0.012450273036956788, 0.01333204984664917, 0.013912222385406493]

# large file size, modification with file diff.
intervals_between_each_get_and_post_request = [
    1, 0.7, 0.3, 0.1, 0.07, 0.03, 0.01, 0.007, 0.003, 0.001]
with_diff_equivalence_data_rate = [10717.588988674557, 15126.18875689136, 33518.994500141926, 85790.1989245057,
                                   112486.96856462864, 198702.54925627285, 308163.4588002848, 349836.3086587052, 381658.0276754728, 452696.0756104446]
with_diff_delta_data_rate = [214.35177977349116, 302.5237751378272, 670.3798900028385, 1715.8039784901139,
                             2249.7393712925727, 3974.050985125457, 6163.269176005696, 6996.726173174104, 7633.160553509456, 9053.921512208892]
with_diff_avg_wall_time_post = [0.013295341730117798, 0.013576300144195556, 0.013920915126800538, 0.014147014617919921, 0.013948493003845215,
                                0.012584246397018432, 0.012927759885787964, 0.012376983165740967, 0.012935144901275635, 0.011722080707550049]
with_diff_avg_wall_time_get = [0.013054895401000976, 0.013639271259307861, 0.014251220226287841, 0.014072760343551635, 0.013840612173080444,
                               0.012774882316589355, 0.012767581939697266, 0.012066293954849244, 0.012886468172073364, 0.011576782464981079]


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
