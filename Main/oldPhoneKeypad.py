"""
 Initialize keypad mapping to decode Numeric input.
 Returns: Mapping of (digit, repeats) to character.
 """
def mapping():
    keymap = {
        ('2', 1): 'a', ('2', 2): 'b', ('2', 3): 'c',
        ('3', 1): 'd', ('3', 2): 'e', ('3', 3): 'f',
        ('4', 1): 'g', ('4', 2): 'h', ('4', 3): 'i',
        ('5', 1): 'j', ('5', 2): 'k', ('5', 3): 'l',
        ('6', 1): 'm', ('6', 2): 'n', ('6', 3): 'o',
        ('7', 1): 'p', ('7', 2): 'q', ('7', 3): 'r', ('7', 4): 's',
        ('8', 1): 't', ('8', 2): 'u', ('8', 3): 'v',
        ('9', 1): 'w', ('9', 2): 'x', ('9', 3): 'y', ('9', 4): 'z',
        ('0', 1): ' '  # space for 0
    }
    return keymap

"""
    Converts a given numeric code to old keypad text.
    ^ Handles '*' to ignore all previous strokes 
    
    Args: Numeric code input followed by a '#'
    Returns: Decoded text message as a string or Input Error
"""
def numericToText(num_code):
    keymap = mapping()
    result = []
    current_digit = ''
    count = 0
    sequences = []  # To store the decoded sequences for backtracking

    # Remove the trailing '#' if present
    if num_code.endswith('#'):
        num_code = num_code[:-1]
    else:
        return "Error: Input must end with '#'"

    for char in num_code:
        if char == '*':
            # Handle '*' by removing the LAST sequence from the same digit
            while sequences and sequences[-1][0] == current_digit:
                result.pop()  # Remove last character from result
                sequences.pop()  # Remove from sequences tracking list
            current_digit = ''
            count = 0
            continue

        if char.isdigit():
            # If the same digit is encountered, increase the count
            if char == current_digit:
                count += 1
            else:
                # Decode previous sequence if a new digit is found
                if current_digit:
                    if (current_digit, count) not in keymap:
                        return "Error: Invalid input sequence"
                    decoded_char = keymap[(current_digit, count)]
                    result.append(decoded_char)
                    sequences.append((current_digit, decoded_char))
                current_digit = char
                count = 1
        elif char == ' ':
            # Decode the current sequence if space is found
            if current_digit:
                if (current_digit, count) not in keymap:
                    return "Error: Invalid input sequence"
                decoded_char = keymap[(current_digit, count)]
                result.append(decoded_char)
                sequences.append((current_digit, decoded_char))
                current_digit = ''
                count = 0
        else:
            return "Error: Invalid character in input"

    # Handle the last sequence at the end of the input
    if current_digit:
        if (current_digit, count) not in keymap:
            return "Error: Invalid input sequence"
        decoded_char = keymap[(current_digit, count)]
        result.append(decoded_char)
        sequences.append((current_digit, decoded_char))

    return ''.join(result).upper()
