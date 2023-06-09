def add_round_key(s, k):
    """ Performs an XOR operation between the state matrix (s) and the round key (k). """
    result = []
    for i in range(len(s)):
        row = []
        for j in range(len(s[i])):
            row.append(s[i][j] ^ k[i][j])  # XOR 연산 수행
        result.append(row)
    return result


def bytes_to_matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix. """
    return [list(text[i:i + 4]) for i in range(0, len(text), 4)]


def matrix_to_bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array. """
    byte_array = bytearray()
    for row in matrix:
        for num in row:
            byte_array.append(num)
    return bytes(byte_array)


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

result = add_round_key(state, round_key)
byte_result = matrix_to_bytes(result)

print(byte_result)
