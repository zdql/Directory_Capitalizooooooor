import json
import os
import sys

def subdirs(path):
    """Yield directory names not starting with '.' under given path."""
    for entry in os.scandir(path):
        yield entry.name


def capitalizer(file):
    try:
        if file[-5:] == '.json':
            f = open(file)
            j = json.load(f)
            f.close()

            os.remove(file)

            modified_file_name = ''

            for c in range(len(file)):
                if c == 0:
                    modified_file_name += file[c].upper()
                else:
                    modified_file_name += file[c]

            print(modified_file_name)

            with open(modified_file_name, 'w') as outfile:
                json.dump(j, outfile)

    except Exception as e:
        pass
        print(e)


def main(dir):
    sd = [i for i in subdirs(dir)]

    for fi in sd:
        capitalizer(fi)


if __name__ == '__main__':
    if len(sys.argv) > 1:
      main(sys.argv[1])
    else:
      print("Must provide directory.")
      
