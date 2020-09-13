import hashlib
import base58
import binascii


def validate_btc_address(address):
    decoded_address = base58.b58decode(address).hex()
    prefix = decoded_address[:-8]
    checksum = decoded_address[len(prefix):]

    calc_checksum = prefix
    for x in range(1,3):
        calc_checksum = binascii.unhexlify(calc_checksum)
        calc_checksum = hashlib.sha256(calc_checksum).hexdigest()

    return calc_checksum[:8] == checksum
