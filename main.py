from argparse import ArgumentParser, Namespace
from modules.fos import FileSort
import sys

parser = ArgumentParser()
# Creates a file sort object which containes all the functions to sort
fos = FileSort()

# Creates basic sort argument
parser.add_argument('-b', '--basic',
                    help="Sorts your files into basic folders namely Photos, AudioVideo, Documents, CodingFiles, Folders, Others",
                    action="store_true",
                    )

# Creates deep sort argument
parser. add_argument('-d', '--deep',
                     help="Further sorts the folders into sub categories based on extensions",
                     action='store_true',
                     )

# args is a variable of type NameSpace which stores in all the arguments created
args: Namespace = parser.parse_args()

if args.deep:
    # Calls the deep sorting algorithm
    fos.deep_sort("Doing a deep sort for yout files...\n")

elif args.basic:
    # Calls the basic sorting algorithm created by us
    fos.basic_sort("Doing a basic sort for your files...\n")

else:
    parser.print_help(sys.stderr)
