# import random
# from pandas import DataFrame
# from pandas import concat
#
#
# cpr = []
# ot = []
# er = []
# stake = []
# wr = []
# sr = []
# exec = []
#
# for i in range(0, 1000):
#     cpr.append(round(random.uniform(100, 20000), 2))
#     ot.append(random.randint(1, 24))
#     er.append(round(random.uniform(0, 1), 2))
#     stake.append(random.randint(0, 1000000))
#     wr.append(round(random.uniform(0, 1), 2))
#     sr.append(round(random.uniform(0, 1), 2))
#     exec.append(round(random.uniform(0, 100), 2))
#
# cpr_df = DataFrame(cpr)
# ot_df = DataFrame(ot)
# er_df = DataFrame(er)
# stake_df = DataFrame(stake)
# wr_df = DataFrame(er)
# sr_df = DataFrame(sr)
# exec_df = DataFrame(exec)
#
# df = concat([cpr_df, ot_df, er_df, stake_df, wr_df, sr_df, exec_df], axis=1)
# df.to_csv('nodesdata_new.csv', header=['cpr', 'ot', 'er', 'stake', 'wr', 'sr', 'exec'])
#

from sklearn.preprocessing import Normalizer
from pandas import read_csv
from pandas import DataFrame

df = read_csv('nodesdata_n.csv')

norm = Normalizer().fit(df)
norm_np = norm.transform(df)

norm_df = DataFrame(norm_np)
norm_df.to_csv('nodesdata_n_n.csv')