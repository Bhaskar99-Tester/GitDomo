ItemInCart = 0
if ItemInCart != 2:
    # raise Exception('product cart count not matching')
    pass

assert(ItemInCart == 0)


# try:
#     with open('text.txt','r') as reader:
#         reader.read()
# except Exception as e:
#     print(e)
# finally:
#     print('code done')
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print('cleaning up resource')
