def create_file_with_strings(filename):

    try:
        with open(filename, 'w') as file:
            file.writelines([
                "Number rules the universe 12345334616.\n",
                "You have to be odd to be number one 09873465434641 and s.\n",
                "The number one reason people fail in life is because they listen to their friends, family, and neighbors..\n",
                "text with 00345612.\n"
            ])
    except IOError as e:
        print(f"Error: {e}")


def remove_digits_and_rewrite(input_file, output_file):
    # Reads the contents of the input file, removes digits, and writes the output file.
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        # Deleting numbers in text
        no_digits_text = ''.join([char for char in text if not char.isdigit()])

        # Write to a new file with 10 characters per line
        with open(output_file, 'w') as file:
            for i in range(0, len(no_digits_text), 10):
                file.write(no_digits_text[i:i + 10] + '\n')
    except IOError as e:
        print(f"Error: {e}")


def read_and_print_file(filename):
    # Reads a file and displays its contents.
    try:
        with open(filename, 'r') as file:
            print("File contents:")
            for line in file:
                print(line, end='')
    except IOError as e:
        print(f"Error: {e}")


# Do
create_file_with_strings('TF10_1.txt')
remove_digits_and_rewrite('TF10_1.txt', 'TF10_2.txt')
read_and_print_file('TF10_2.txt')

