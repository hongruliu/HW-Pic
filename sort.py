import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file", help='read a file')

args = parser.parse_args()

with open(args.file) as fp: 
    content = fp.readlines()
    content = sorted(content)
    fp.close()

with open('sorted_file.txt', 'w+') as f:
    f.writelines(content)
    f.close()