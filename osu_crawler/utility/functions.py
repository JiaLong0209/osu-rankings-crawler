import re

def str_preprocess(s):
    return re.sub(r'[#\s]+', '', s)

def str_preprocess_in_list(p_list):
    return list(map(str_preprocess, p_list))

def print_dict(p_dict):
    print('\n-------print_dict()-----------')
    for k in p_dict:
        print(f'{k}: {p_dict[k]}')
    print('------------------------------\n')

