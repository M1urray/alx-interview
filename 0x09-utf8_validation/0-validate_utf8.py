def is_valid_utf8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.

    Args:
    - data: a list of integers representing a UTF-8 encoded string.

    Returns:
    - True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0
    for byte in data:
        binary = format(byte, '#010b')[-8:]
        if num_bytes == 0:
            if binary[0] == '1':
                num_bytes = len(binary.split('0')[0])
                if num_bytes == 1 or num_bytes > 4:
                    return False
            elif binary[0] == '0':
                continue
            else:
                return False
        else:
            if not (binary[0] == '1' and binary[1] == '0'):
                return False
            num_bytes -= 1
    return num_bytes == 0