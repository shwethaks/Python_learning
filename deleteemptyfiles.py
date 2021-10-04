import os
import argparse
import sys

import shutil

def deleteEmptyFiles(args):
    for root, dirs, files in os.walk(args.rootDirectory):
        '''
        remove empty dir
        for d in dirs:
            dirs.remove(d)
        '''
        for f in files:
            fullname = os.path.join(root, f)
            try:
                if os.path.getsize(fullname) == 0:
                    print ("removing 0 kb file " +fullname)
                    os.remove(fullname)
            except WindowsError:
                continue

        if args.excludeFilesOfSize:
            for f in files:
                fullname = os.path.join(root, f)
                try:
                    if os.path.getsize(fullname) >= (1024.0 *1024.0)*args.excludeFilesOfSize:
                        print("excluding file of size: " + str ((os.path.getsize(fullname)/(1024.0 * 1024.0)))+ "MB: " +fullname)
                        shutil.move(fullname, fullname + '.exclude')
                except WindowsError:
                    continue
def main():

    parser = argparse.ArgumentParser(description ="deletes all empty files and excludes files larger than or equal to a specific size within the specified root")
    parser. add_argument("rootDirectory", help ="Root directory to serch for empty files")
    parser.add_argument(" --excludeFilesOfSize", type=int , help = "Excluded files greater than or equal to specified MB")

    args = parser.parse_args()

    if not os.path.isdir(args.rootDirectory):
        print("Invalid argument error")
        sys.exit(1)

    if args.excludeFilesOfSize == 0:
        print ("invalid argument error")
        sys.exit(1)

    deleteEmptyFiles(args)

if __name__ == "__main__":
    sys.exit(main())