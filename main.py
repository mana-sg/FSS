from argparse import ArgumentParser, Namespace
from fos import FileSort
import sys

parser = ArgumentParser()
fos = FileSort()

parser.add_argument('-b', '--basic',
                    help="Sorts your files into basic folders namely Photos, AudioVideo, Documents, CodingFiles, Folders, Others",
                    action="store_true",
                    )
parser. add_argument('-d', '--deep',
                     help="Further sorts the folders into sub categories based on extensions",
                     action='store_true',
                     )

args: Namespace = parser.parse_args()

if args.deep:
    fos.deep_sort("Doing a deep sort for yout files...\n")

elif args.basic:
    fos.basic_sort("Doing a basic sort for your files...\n")

else:
    parser.print_help(sys.stderr)
