file_name = r"C:\Users\username\Downloads\phix.fa"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
        sequence = "".join([line.strip() for line in content if not line.startswith('>')])
    return sequence

sequence = read_file(file_name)
k = 3

def generate_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmers.append(kmer)
    return kmers

sets = generate_kmers(sequence, k)
number = len(sets)
print(f"All positions: {sets}")
print(f"The number of kmers: {number}")
