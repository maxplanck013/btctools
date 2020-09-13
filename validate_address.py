import argparse
import btctools


parser = argparse.ArgumentParser()
parser.add_argument("btc_address", help="A bitcoin address.")

address = parser.parse_args().btc_address

if btctools.validate_btc_address(address):
    print(address)
    exit(0)
else:
    print("Invalid address")
    exit(1)
