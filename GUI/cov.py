import glob
import os

dem = 1
while True:
    print('Sp thu ',dem,':')
    for file_name in glob.iglob("F:/41/*", recursive=True):
        os.rename(file_name, file_name + '.jpg')
    c = int(input('Tiếp tuc= '))
    if c!=0:
        break
    dem =dem +1