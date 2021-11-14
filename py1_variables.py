from support_magic import var_info
# 0
# Variables and data types
# Breytur og gagnatög

# Variable er nafn á minnisplássi í tölvunni
# Staður til að geyma og vísa í gildi/gögn sem við viljum nota á meðan forritið keyrir

# Tala um:
    # Python er túlkað mál...munurinn á því og þýddu.
    # Muna að minna á að það er ekki nauðsynlegt að skilja nema brot af því sem við erum að tala um hér.
    # Mikilvægast að hafa séð það til að skilja samhengið seinna.
    # Eina sem þarf að taka frá þessu myndbandi er það að það er hægt að geima stuff í breytum og vinna svo með það.

# 1
#################
# Numeric types #
#################

# int
my_int = 1729
print("my_int:", my_int)
var_info(my_int, isl=True)

#
# # 2
# # float
# # Það er ekki endalaus nákvæmni á float tölu
# # En það eru til aðrar leiðir til að fá mikið meiri nákvæmni
# my_float = 6.283185307179586476
# print("my_float:", my_float)
# var_info(my_float)
#
#
# # 3
# # complex
# my_complex_number = 2+3j
# print("my_complex_number:", my_complex_number)
# var_info(my_complex_number)
# # 3.1
# print("my_complex_number.real:", my_complex_number.real)
# my_complex_real = my_complex_number.real
# var_info(my_complex_real)
# print("my_complex_number.imag:", my_complex_number.imag)
# my_complex_imag = my_complex_number.imag
# var_info(my_complex_imag)
#
#
# # 4
# ################
# # boolean type #
# ################
#
# my_false_bool = False
# my_true_bool = True
# print("my_false_bool:", my_false_bool)
# var_info(my_true_bool)
# print("my_true_bool:",  my_true_bool)
# var_info(my_false_bool)
#
# # 5
# ##################
# # Sequence types #
# ##################
#
# # string
# my_string = "Þetta er strengur (string)"
# print("my_string:", my_string)
# var_info(my_string)

# 6
# list
list_item = 2021
#   Index 0      1         2      3   4          5   6
my_list = [6.28, "Python", False, 15, list_item, 15, "15"]
print("my_list:", my_list)
var_info(my_list)
# 6.1
print("my_list[0]:", my_list[0])
my_list_at_0 = my_list[0]
var_info(my_list_at_0)


# 7
# tuple
my_tuple = (6.28, "Python", "-1", 15, True, 15, "15")
print("my_tuple:", my_tuple)
var_info(my_tuple)

# # 8
# #######
# # set #
# #######

my_set = {6.28, "Python", False, 15, list_item, 15, "15"}
print("my_set:", my_set)
var_info(my_set)
print(my_set)
# # 9
# ##############
# # dictionary #
# ##############
#
# my_dict = {"character": "Winston Smith", "book": "1984"}
# print("my_dict:", my_dict)
# var_info(my_dict)
# # 9.1
# print("my_dict.keys():", my_dict.keys())
# my_dick_keys = my_dict.keys()
# var_info(my_dick_keys)
# print("my_dict.values():", my_dict.values())
# my_dict_values = my_dict.values()
# var_info(my_dict_values)
#
# # 10
# ##################
# # class / object #
# ##################
#
# # Okkar eigið gagnatag
# # Þetta er heilt concept í forritun
# # Object oriented programming / Hlutbundin forritun
#
#
# # 11
# class Player:
#
#     def __init__(self, name, age, number, position, team, nationality):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.position = position
#         self.team = team
#         self.nationality = nationality
#
#     def __str__(self):
#         return f"The {self.age} years old {self.nationality} {self.position.lower()} {self.name} wears number " \
#                f"{self.number} for {self.team}."
#
#
# my_player = Player("Grant Hanley", 29, 5, "Defender", "Norwich", "Scottish")
#
#
# # 12
# print("my_player.name:", my_player.name)
# my_player_name = my_player.name
# var_info(my_player_name)
# # 12.1
# print("my_player.age:", my_player.age)
# my_player_age = my_player.age
# var_info(my_player_age)
# # 12.2
# print("my_player.number:", my_player.number)
# print("my_player.position:", my_player.position)
# print("my_player.team:", my_player.team)
# print("my_player.nationality:", my_player.nationality)
# # 12.3
# print(my_player)
# var_info(my_player)
#
# # 13
# # Galdrar til að sjá af hvaða gagnatagi breyturnar eru.
# varList = [my_int, my_float, my_complex_number, my_false_bool, my_string, my_list, my_set, my_tuple, my_dict, my_player]
#
# var_info(varList, False, True)