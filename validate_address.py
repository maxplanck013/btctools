import argparse
import btctools


parser = argparse.ArgumentParser()
verbosity = parser.add_mutually_exclusive_group()
parser.add_argument("btc_address", type=str, help="a bitcoin address.")
verbosity.add_argument("-q", "--quiet", action="store_true", default=False, help="don't output anything.")
verbosity.add_argument("-v", "--verbose", action="store_true", default=False, help="show intermediate steps.")

args = parser.parse_args()

address = args.btc_address
quiet = args.quiet

if btctools.validate_btc_address(address, verbose=args.verbose):
    if not quiet: print(address)
    exit(0)
else:
    if not quiet: print("Invalid address")
    exit(1)
