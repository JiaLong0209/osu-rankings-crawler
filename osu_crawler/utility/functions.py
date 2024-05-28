
def replace_space(str):
    return str.replace(" ", "").replace("\n", "")

def replace_space_in_list(p_list):
    return list(map(replace_space, p_list))

def print_dict(p_dict):
    print('\n-------print_dict()-----------')
    for k in p_dict:
        print(f'{k}: {p_dict[k]}')
    print('------------------------------\n')

