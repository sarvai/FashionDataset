import argparse
from config import config
from data import dataset
from analytics import analytics

def parse_commandline():
    parser = argparse.ArgumentParser(description='Fashion Dataset Viewer')
    parser.add_argument('-r','--dataroot', help='Path to stored data', required=True )
    parser.add_argument('-o','--output', help='Path to a pickle file to save intermediate results', required=True)
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_commandline()
    cfg = config( args.dataroot )

    d = dataset( cfg )
    a = analytics( cfg, d )

    a.validate( args.output )
