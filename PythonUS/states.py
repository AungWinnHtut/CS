from icecream import ic

def string_to_states(data):
    AESblock_size = 16
    # Convert the input string to bytes
    data_bytes = data.encode('utf-8')

    # Pad the data if needed
    padding_length = AESblock_size - len(data_bytes) % AESblock_size
    padded_data = data_bytes + bytes([padding_length] * padding_length)

    # Divide the padded data into blocks of 16 bytes
    blocks = [padded_data[i:i + AESblock_size] for i in range(0, len(padded_data), AESblock_size)]
    ic(blocks)
    # Print or process each block (state)
    for i, block in enumerate(blocks):
        print(f"State {i + 1}: {block.hex()}")

    return blocks

def states_to_string(states):
    # Concatenate the blocks to get the padded data
    padded_data = b''.join(states)

    # Extract the padding length
    padding_length = padded_data[-1]

    # Unpad the data to remove the padding
    data_bytes = padded_data[:-padding_length]

    # Convert the bytes to a string
    data_string = data_bytes.decode('utf-8')

    return data_string

# Example usage
input_string = "This is မြန်မာစာလုံးများ for AES encryption."
states = string_to_states(input_string)

# If you want to convert the states back to a string
output_string = states_to_string(states)
print(f"\nOutput String: {output_string}")
