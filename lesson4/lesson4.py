# print(10)
# raise ValueError
# print("am I executed?")
#
# name = '3lena'
# if name[0].isnumeric():
#     raise NameError('Invalid name')
#
# try:
#     print(10/0)
# except:
#     print('An error occured with division bt zero', file=log_file)
#
#
# a = input_small_str('Input less than 10 symbols')
# assert lev(a) < 0
# print(a)

mass = int(input("Enter mass: "))
assert (mass > 0), "Mass can't be less than 0"
print(mass)
