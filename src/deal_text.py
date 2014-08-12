#!/user/bin/python
# -*- coding: utf-8 -*-


import string
import sys
import os
import argparse
import re
import chardet

def process(inp,outp):
    dict_1={}
    input_file= inp
    
    f_in=open(input_file,'r')
    pos_1_lines=f_in.readlines()
    f_in.close()
    for pos_1 in pos_1_lines:
        tmp_pos_1=pos_1.rstrip()
        tmp_pos=re.sub('#[^#]*#','',tmp_pos_1)
        #print tmp_pos
        if tmp_pos in dict_1:
            continue
        else:
            dict_1[tmp_pos]=1
    print len(dict_1)

    dict_file=open('../conf/emotion_dict.txt','r')
    dict_lines=dict_file.readlines()
    dict_file.close()
    all_dict={}
    for dict_line in dict_lines:
        dict_line=dict_line.split('\t')[0]
        if dict_line in all_dict:
            continue
        else:
            all_dict[dict_line] =1
    print len(all_dict)
    
    output_file=outp
    f_save=open(output_file,'w')
    for k,v in dict_1.items():
        f_flag=0
        #print chardet.detect(k)
        for k1,v2 in all_dict.items():
            #print chardet.detect(k1)
            if k1 in k :
                f_flag=1
                break
            else:
                continue
        #print ("%s\t%s"%(f_flag,k))
        f_save.write("%s\t%s"%(f_flag,k))
        f_save.write("\n")
        f_save.flush()
        
    

if __name__ == "__main__":
    input_file="train_2014.07.14.txt"
    output_file="flag_train_2014.07.14.txt"
    process(input_file,output_file)

