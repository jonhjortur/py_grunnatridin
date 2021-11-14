# This code is not intended to be beautiful or clever, it should work the way I want it...
# ...which it does!!

import inspect
import sys


def _parse_var_name(var):
    for f in reversed(inspect.stack()):
        return [k for k, v in f.frame.f_locals.items() if v is var][0]


def _printer(var, box=True, is_list_of_vars=False, isl=False,
             iter_list=False, iter_name="", list_idx=0, iter_set=False):
    s_var_name = _parse_var_name(var) if not iter_list else f'{iter_name}[{list_idx}]'\
        if not iter_set else f'{iter_name} @ {list_idx}'
    s_var_addr = hex(id(var))
    var_type = type(var)
    var_size = sys.getsizeof(var)

    s_name = f'Name: {s_var_name}' \
        if not isl else f'Nafn: {s_var_name}'
    s_memory_address = f'Memory address: {s_var_addr}' \
        if not isl else f'Minnisfang: {s_var_addr}'
    s_type = f'Datatype: {var_type}' \
        if not isl else f'Gagnatag: {var_type}'
    s_instance_size = f'Size in memory: {var_size} bytes' \
        if not isl else f'Stærð í minni: {var_size} bæti'

    l_line_lengths = [len(s_name), len(s_memory_address), len(s_type), len(s_instance_size)]
    i_longest_line = max(l_line_lengths)
    i_box_width = i_longest_line + 4
    s_title = "Information" if not isl else "Upplýsingar"
    # Orðin "Information" og "upplýsingar" eru bæði 11 stafir
    # svo þetta er í raun óþarfi á meðan ég skipti ekki um titil
    i_box_top_symbols = i_box_width - (len(s_title)) - 4

    i_first_end_padding = i_longest_line - l_line_lengths[0]
    i_second_end_padding = i_longest_line - l_line_lengths[1]
    i_third_end_padding = i_longest_line - l_line_lengths[2]
    i_forth_end_padding = i_longest_line - l_line_lengths[3]

    s_new_line = "\n"
    s_side_symbol = "|"
    s_top_symbol = "*"  # Overscore -> ‾
    s_bottom_symbol = "*"
    s_front_symbol = f'{s_side_symbol} ' * box
    s_back_symbol = f' {s_side_symbol}' * box

    s_top_box_line = f'{s_new_line * box}{s_front_symbol}' \
                     f'{s_title * box} {s_top_symbol * i_box_top_symbols * box}{s_side_symbol * box}{s_new_line}'
    s_bottom_box_line = f'{s_bottom_symbol * i_box_width * box}{s_new_line * box}'

    s_name_line = f'{s_front_symbol}{s_name}' \
                  f'{" " * i_first_end_padding * box}{s_back_symbol}{s_new_line}'
    s_memory_address_line = f'{s_front_symbol}{s_memory_address}' \
                            f'{" " * i_second_end_padding}{s_back_symbol}{s_new_line}'
    s_type_line = f'{s_front_symbol}{s_type}' \
                  f'{" " * i_third_end_padding}{s_back_symbol}{s_new_line}'
    s_instance_size_line = f'{s_front_symbol}{s_instance_size}' \
                           f'{" " * i_forth_end_padding * box}{s_back_symbol}{s_new_line}'

    print(f'{s_top_box_line}'
          f'{s_name_line}'
          f'{s_memory_address_line}'
          f'{s_type_line}'
          f'{s_instance_size_line}', end='')

    print(f'{s_bottom_box_line}', end='') \
        if is_list_of_vars or iter_list else print(f'{s_bottom_box_line}')


def var_info(var, box=True, is_list_of_vars=False, isl=False):

    if isinstance(var, list) and is_list_of_vars:
        for v in var:
            _printer(v, box, is_list_of_vars, isl)
    elif isinstance(var, (list, tuple)):
        _printer(var)
        for idx, item in enumerate(var):
            _printer(item, iter_list=True, iter_name=_parse_var_name(var), list_idx=idx)
    elif isinstance(var, set):
        for idx, item in enumerate(var):
            _printer(item, iter_list=True, iter_name=_parse_var_name(var), list_idx=idx, iter_set=True)
    else:
        _printer(var, box, is_list_of_vars, isl)
