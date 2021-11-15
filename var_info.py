# This code is not intended to be beautiful, clever or well structured.
# It should work the way I want it...which it does...until proven otherwise!

import inspect
import sys


def _parse_var_name(var):
    for f in reversed(inspect.stack()):
        return [k for k, v in f.frame.f_locals.items() if v is var][0]


def _assemble(var, box=True, iter_list=False, iter_name="", list_idx=0, iter_set=False, iter_dict=False):
    var_name, var_addr, var_type, var_size = \
        _get_var_info(var, iter_list, iter_name, list_idx, iter_set, iter_dict)
    name, value, memory_address, datatype, instance_size = \
        _make_lines(iter_dict, var, var_name, var_addr, var_type, var_size)

    _print(box, iter_dict, name, value, memory_address, datatype, instance_size)


def _get_var_info(var, iter_list, iter_name, list_idx, iter_set, iter_dict):
    var_name = f'{iter_name}[{list_idx}]' if iter_list \
        else f'{iter_name} @ {list_idx}' if iter_set \
        else f'{iter_name}' if iter_dict \
        else _parse_var_name(var)

    var_addr = hex(id(var))
    var_type = type(var)
    var_size = sys.getsizeof(var)

    return var_name, var_addr, var_type, var_size


def _make_lines(iter_dict, var, var_name, var_addr, var_type, var_size, value=""):
    if iter_dict:
        name, value = f'Key: {var_name}', f'Value: {var}'
    else:
        name = f'Name: {var_name}'
    memory_address = f'Memory address: {var_addr}'
    datatype = f'Datatype: {var_type}'
    instance_size = f'Size in memory: {var_size} bytes'

    return name, value, memory_address, datatype, instance_size


def _print(box, iter_dict, name, value, memory_address, datatype, instance_size):
    line_lengths = [len(name), len(value), len(memory_address), len(datatype), len(instance_size)]
    longest_line = max(line_lengths)
    box_width = longest_line + 4
    title = "Information"
    box_top_symbols = box_width - (len(title)) - 4

    first_end_padding = longest_line - line_lengths[0]
    second_end_padding = longest_line - line_lengths[1]
    third_end_padding = longest_line - line_lengths[2]
    forth_end_padding = longest_line - line_lengths[3]
    fifth_end_padding = longest_line - line_lengths[4]

    new_line = "\n"
    side_symbol = "|"
    top_symbol = "*"  # Overscore -> ‾
    bottom_symbol = "*"
    front_symbol = f'{side_symbol} ' * box
    back_symbol = f' {side_symbol}' * box

    print(f'{new_line * box}{front_symbol}'
          f'{title * box} {top_symbol * box_top_symbols * box}{side_symbol * box}{new_line}', end='')
    print(f'{front_symbol}{name}'
          f'{" " * first_end_padding * box}{back_symbol}{new_line}', end='')
    if iter_dict:
        print(f'{front_symbol}{value}'
              f'{" " * second_end_padding * box}{back_symbol}{new_line}', end='')
    print(f'{front_symbol}{memory_address}'
          f'{" " * third_end_padding}{back_symbol}{new_line}', end='')
    print(f'{front_symbol}{datatype}'
          f'{" " * forth_end_padding}{back_symbol}{new_line}', end='')
    print(f'{front_symbol}{instance_size}'
          f'{" " * fifth_end_padding * box}{back_symbol}{new_line}'
          f'{bottom_symbol * box_width * box}{new_line * box}')


def information(var, box=True, is_list_of_vars=False):
    if isinstance(var, list) and is_list_of_vars:
        for v in var:
            _assemble(v, box)
    elif isinstance(var, (list, tuple)):
        _assemble(var, box)
        for idx, item in enumerate(var):
            _assemble(item, box, iter_list=True, iter_name=_parse_var_name(var), list_idx=idx)
    elif isinstance(var, set):
        for idx, item in enumerate(var):
            _assemble(item, box, iter_name=_parse_var_name(var), list_idx=idx, iter_set=True)
    elif isinstance(var, dict):
        _assemble(var)
        for k, v in var.items():
            _assemble(v, box, iter_name=k, iter_dict=True)
    else:
        _assemble(var, box)
