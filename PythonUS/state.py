from icecream import ic
def text_to_states(text):
    # Ensure the length of the input text is a multiple of 16 (AES block size)
    text = text.ljust((len(text) + 15) // 16 * 16, ' ')

    ic(text)

    # Initialize a 4x4 matrix (list of lists) for states
    states = [[0] * 4 for _ in range(4)]
    ic(states)
    # Fill in the states matrix with the bytes from the input text
    for col in range(4):
        for row in range(4):
            states[row][col] = ord(text[col * 4 + row])

    return states

def print_states(states):
    # Display the states matrix
    for row in states:
        print(' '.join(f'{hex(byte)[2:].zfill(2)}' for byte in row))

# Example usage:
input_text = "Hello, AES! abcdefghijklmnopqrstuvwxyz"
states_matrix = text_to_states(input_text)
print("Original Text:")
print(input_text)
print("\nStates Matrix:")
print_states(states_matrix)
