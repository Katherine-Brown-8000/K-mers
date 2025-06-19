sequence = "ATCGAT"
k = 3

def kmer_index(sequence, k):
    index = []
    
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        index.append((kmer, i))
        
    index.sort(key=lambda x: x[1]) # key lambda sorts it by position
    
    return index

index = kmer_index(sequence, k)

print("K-mer index:")
for kmer, pos in index:
    print(f"{kmer} at position {pos}")
