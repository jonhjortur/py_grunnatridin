# This code is not intended to be beautiful or clever, it should work the way I want it...
# ...which it does!!

import inspect
import sys


def _parse_var_name(var):
    for f in reversed(inspect.stack()):
        return [k for k, v in f.frame.f_locals.items() if v is var][0]


def _printer(var, box, is_list, isl):
    s_name = f'Name: {_parse_var_name(var)}' \
        if not isl else f'Nafn: {_parse_var_name(var)}'
    s_memory_address = f'Memory address: {hex(id(var))}' \
        if not isl else f'Minnisfang: {hex(id(var))}'
    s_type = f'Datatype: {type(var)}' \
        if not isl else f'Gagnatag: {type(var)}'
    s_instance_size = f'Size in memory: {sys.getsizeof(var)} bytes' \
        if not isl else f'Stærð í minni: {sys.getsizeof(var)} bæti'

    l_line_lengths = [len(s_name), len(s_memory_address), len(s_type), len(s_instance_size)]
    i_longest_line = max(l_line_lengths)
    i_box_width = i_longest_line + 4

    i_first_end_padding = i_longest_line - l_line_lengths[0]
    i_second_end_padding = i_longest_line - l_line_lengths[1]
    i_third_end_padding = i_longest_line - l_line_lengths[2]
    i_forth_end_padding = i_longest_line - l_line_lengths[3]

    s_new_line = "\n"
    s_front_hashtag = "# " * box
    s_back_hashtag = " #" * box

    s_top_box_line = f'{s_new_line * box}{s_front_hashtag}{"Info" * box} {"#" * (i_box_width - 7) * box}{s_new_line}'
    s_bottom_box_line = f'{"#" * i_box_width * box}{s_new_line * box}'

    s_name_line = f'{s_front_hashtag}{s_name}' \
                  f'{" " * i_first_end_padding * box}{s_back_hashtag}{s_new_line}'
    s_memory_address_line = f'{s_front_hashtag}{s_memory_address}' \
                            f'{" " * i_second_end_padding}{s_back_hashtag}{s_new_line}'
    s_type_line = f'{s_front_hashtag}{s_type}' \
                  f'{" " * i_third_end_padding}{s_back_hashtag}{s_new_line}'
    s_instance_size_line = f'{s_front_hashtag}{s_instance_size}' \
                           f'{" " * i_forth_end_padding * box}{s_back_hashtag}{s_new_line}'

    print(f'{s_top_box_line}'
          f'{s_name_line}'
          f'{s_memory_address_line}'
          f'{s_type_line}'
          f'{s_instance_size_line}', end='')

    print(f'{s_bottom_box_line}', end='') \
        if is_list else print(f'{s_bottom_box_line}')


def var_info(var, box=True, is_list=False, isl=False):
    """
    Prints info about the variables name, memory address, data type and size in memory.

            Parameters:
                var: Any,
                box: bool = True,
                is_list: bool = False,
                isl: bool = False) -> None
    """

    if is_list:
        for v in var:
            _printer(v, box, is_list, isl)
    else:
        _printer(var, box, is_list, isl)
