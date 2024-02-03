def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    :param data:
    :return:
    """
    num_bytes = 0

    for byte in data:
        if not num_bytes:
            if byte & 0b10000000 == 0:
                continue
            mask = 1 << 7
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1

    return num_bytes == 0
