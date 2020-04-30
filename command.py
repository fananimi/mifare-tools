from smartcard.util import toHexString

UID = "FF CA 00 00 00"
LOAD_AUTH = "FF 82 00 00 06"
AUTH = "FF 86 00 00 05"
KEY_TYPE_A = "60"
KEY_TYPE_B = "61"


def get_block_auth_cmd(sector, block, key_type):
    block = toHexString([(sector * 4) + block])
    return "%s 01 00 %s %s 00" % (AUTH, block, key_type)


def read_block_cmd(sector, block):
    block = toHexString([(sector * 4) + block])
    return "FF B0 00 %s 10" % (block)
