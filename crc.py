def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def crc(data, generator):
    data += '0' * (len(generator) - 1)
    divisor = generator
    remainder = data[:len(generator)]
    
    while len(generator) <= len(data):
        if remainder[0] == '1':
            remainder = xor(remainder, divisor) + data[len(generator):len(generator)+1]
        else:
            remainder = remainder[1:] + data[len(generator):len(generator)+1]
        data = data[1:]
        
    remainder = remainder[1:]
    return remainder

# Example usage
data = "1101"
generator = "1011"
remainder = crc(data, generator)
transmitted_data = data + remainder
print("Transmitted Data with CRC:", transmitted_data)
