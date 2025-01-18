# -*- coding: utf-8 -*-
'''
Program :   Predict procedure.
Author  :   Haoyang Cui, Shanghai MicroPort EP Medtech Co., Ltd..
File    :   predict.py
Date    :   2023/9/22
Version :   V1.0
'''
import os 
import argparse
import model
import time
def run(inputDir,outputDir):        
    for file_id in os.listdir(inputDir):
        if file_id.endswith('.nii.gz'):
            file_path=os.path.join(inputDir,file_id)
            save_path=os.path.join(outputDir,file_id)
            if not os.path.exists(save_path):
                run_st=time.time()              
                model.run_atunet(file_path,save_path)
                print(f'file_id {file_id} ====> run time is :{round(time.time()-run_st,4)}')
            else:
                print(f'file_id {file_id} has been completed')
    print('all file completed')
if __name__=='__main__':      
    parser = argparse.ArgumentParser('Airway Tree Modeling (cuihy)')
    parser.add_argument('-i', "--inputs", default='./inputs', type=str, help="input path of the CT images list")
    parser.add_argument('-o', "--outputs", default='./outputs', type=str, help="output of the prediction results list")
    args = parser.parse_args()
    run(inputDir=args.inputs,outputDir=args.outputs)
