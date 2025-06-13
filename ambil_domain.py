def ambil_domain_saja(file_input: str, file_output: str):
    with open(file_input, 'r') as infile, open(file_output, 'w') as outfile:
        for line in infile:
            # Hapus komentar dan whitespace
            bersih = line.split('#')[0].strip()
            if bersih:
                outfile.write(bersih + '\n')

if __name__ == '__main__':
    import sys
    # Default: input.txt → output.txt
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.txt'
    ambil_domain_saja(input_file, output_file)
