import os
import numpy as np

def mkdir_p(dire:str):
    '''make a directory (dir) if it doesn't exist'''
    if not os.path.exists(dir):
        os.mkdir(dire)

job_directory = f"{os.getcwd()}/data"

#this creates a directory if that dir doesn't already exist
mkdir_p(job_directory)

energies = 10**np.linspace(19, 25, 16)

names = np.linspace(1, 16, 16, dtype=int)

for ene, name in zip(energies, names):

    job_file = os.path.join(job_directory, f'submit_{name}.job')

    with open(f'{job_file}', 'w') as fh:
        #write whatever you need in your script here
        fh.writelines("#!/bin/bash\n")
        
        fh.writelines("source /user/anaconda3/bin/activate\n")

        fh.writelines(f"~/anaconda3/bin/python /user/prop_sim_final_high.py {ene} {name}\n" )     

    #os.system(f"qsub -lnodes=1: {job_file}")
