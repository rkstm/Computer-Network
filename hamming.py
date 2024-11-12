def hamming_code(data):
    data = list(data)
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    
    # Insert parity bits at positions that are powers of 2
    for i in range(r):
        data.insert((2 ** i) - 1, '0')
    
    # Calculate parity bits
    for i in range(r):
        parity_position = (2 ** i) - 1
        parity = 0
        for j in range(parity_position, len(data), 2 ** (i + 1)):
            parity ^= sum(int(data[k]) for k in range(j, min(j + 2 ** i, len(data))))
        data[parity_position] = str(parity)
    
    return ''.join(data)

# Example usage
data = "1011"
encoded_data = hamming_code(data)
print("Encoded Hamming Code:", encoded_data)
