#!/usr/bin/env python3
import os
import sys
from term_line_summary import *

def main(args):
    prefix = args[1]
    directory = args[2]
    txt_type = args[3]
    paragraph_dir = args[4]
    redirect_file = args[5]
    input_file = prefix+'.term_instance_map'
    output_file = prefix+'.summary'
    cluster_strategy='big_centroid_max'
    generate_summaries_from_term_file_map(input_file,output_file,directory,cluster_sample_strategy=cluster_strategy,
                                          txt_file_type=txt_type, paragraph_dir=paragraph_dir, redirect_file=redirect_file)

    
if __name__ == '__main__': sys.exit(main(sys.argv))
