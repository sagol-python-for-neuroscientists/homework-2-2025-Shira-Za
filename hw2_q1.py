MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-'
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    print("Opening input file...")
    
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    
    with open(input_file, "r") as file:
        english_text = file.read()

    lines = english_text.splitlines()
    morse_lines = []

    for line in lines:
        words = line.split()
        morse_words = []
        for word in words:
            morse_word = ''.join(
                MORSE_CODE[char.upper()] for char in word if char.upper() in MORSE_CODE
                )
            morse_words.append(morse_word)
        morse_line = '\n'.join(morse_words)
        morse_lines.append(morse_line)

    with open(output_file, 'w') as file:
        file.write('\n'.join(morse_lines))

    return output_file 

if __name__ == '__main__':
    # Question 1
    param1 = "lorem.txt"
    param2 = "lorem_morse.txt"
    return_value = english_to_morse(param1, param2)
    print(f"Question 1 solution: {return_value}")