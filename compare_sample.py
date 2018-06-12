""" run with the following command, replace the values in angle brackets:
python compare_sample.py <path_to_sample_data> <path_to_data_to_comapare_to> 
"""
import sys
import pandas as pd

# takes the paths to the files 
compare_to = sys.argv[1]
data_standard = sys.argv[2]

# read the files
df_compare = pd.read_csv(data_standard, header = 0)
df_sample = pd.read_csv(compare_to, header = 0)
# narrow down the data we will want to join
df_sample = df_sample[['number', 'manual prediction of category']]
# join the standard and the sample using the number of the ticket
result = df_sample.join(df_compare, on='number', lsuffix='_l', rsuffix='_r')
left = df_sample.set_index('number')
right = df_compare.set_index('number')
result = left.join(right, lsuffix='_l', rsuffix='_r')
# write results to csv  
result.to_csv('compare.csv')