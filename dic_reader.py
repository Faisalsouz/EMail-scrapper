import os
import glob
import pandas as pd
#set working directory
os.chdir(r"D:\scraping\output")

#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
    # combined_csv=([pd.read_csv(i,encoding= 'unicode_escape')])
    # print(i)
    # print(combined_csv)
combined_csv = pd.concat([pd.read_csv(f,encoding= 'unicode_escape',header=None) for f in all_filenames ],axis=0).drop_duplicates()
#export to csv
combined_csv.to_csv( "combined-list-NRW.csv", index=False, encoding='utf-8-sig')

















# import re
# with open('restau_output.txt','r')as file:
#     #data=json.load(file)
#     line=file.readlines()
#     for i in line:
#         main_split=i.split('"')
#         main_dict={}
#         for i in main_split:
#
#             reg=re.sub(r"[^\[\],\s]+",'',i)
#             if i!=reg:
#                 print(i)
#             elif i[0].isdigit():

        # email=main_split[0].split(',')
        # print(email)
        # res_names=main_split[1].replace('[[','').split(',')
        # print(res_names)
        # print(len(email),len(res_names))
