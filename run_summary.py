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
    confidence_order = args[6].lower()
    input_file = prefix+'.term_instance_map'
    output_file = prefix+'.summary'
    cluster_strategy='big_centroid_max'
    
    if confidence_order == 'true':
        breakdown_by_log_10 = True
    else:
        breakdown_by_log_10 = False
	generate_summaries_from_term_file_map(input_file,output_file,directory,cluster_sample_strategy=cluster_strategy,
                                          txt_file_type=txt_type, paragraph_dir=paragraph_dir, redirect_file=redirect_file, breakdown_by_log_10=breakdown_by_log_10)

    
if __name__ == '__main__': sys.exit(main(sys.argv))
