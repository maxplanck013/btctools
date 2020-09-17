import hashlib
import base58
import binascii


def validate_btc_address(address, verbose=False):
    decoded_address = base58.b58decode(address).hex()
    prefix = decoded_address[:-8]
    checksum = decoded_address[len(prefix):]

    if verbose:
        print(f"[info] decoded address = {decoded_address}")
        print(f"[info] address prefix = {prefix}")
        print(f"[info] address checksum = {checksum}")

    calc_checksum = prefix

    if verbose: print("[info] calculating checksum...")

    for x in range(1,3):
        calc_checksum = binascii.unhexlify(calc_checksum)
        calc_checksum = hashlib.sha256(calc_checksum).hexdigest()

    if verbose: print(f"[info] checksum = {calc_checksum[:8]}")

    return calc_checksum[:8] == checksum
