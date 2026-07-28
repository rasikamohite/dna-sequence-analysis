"""
DNA Sequence Analysis Using Python
Author: Rasika Mohite

A beginner-friendly bioinformatics project that:
- Validates a DNA sequence
- Counts nucleotide bases (A, T, G, C)
- Calculates GC content
- Transcribes DNA -> RNA
- Translates RNA -> Protein
- Prints a final analysis report
"""

# ---------------------------------------------------------
# Full codon table (all 64 codons -> amino acids)
# "*" means STOP codon
# ---------------------------------------------------------
CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

VALID_BASES = set("ATGC")


# ---------------------------------------------------------
# Functions
# ---------------------------------------------------------

def clean_sequence(sequence):
    """Remove whitespace and convert the sequence to uppercase."""
    return sequence.strip().upper().replace(" ", "").replace("\n", "")


def is_valid_dna(sequence):
    """Check that the sequence only contains A, T, G, C."""
    return set(sequence).issubset(VALID_BASES)


def count_bases(sequence):
    """Return a dictionary with the count of each base."""
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
    }


def gc_content(sequence):
    """Calculate the percentage of G and C bases in the sequence."""
    if len(sequence) == 0:
        return 0.0
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    return round((g_count + c_count) / len(sequence) * 100, 2)


def transcribe_to_rna(sequence):
    """Convert a DNA sequence to RNA by replacing T with U."""
    return sequence.replace("T", "U")


def translate_to_protein(rna_sequence):
    """
    Translate an RNA sequence into a protein sequence using the codon table.
    Translation stops early if a STOP codon is found.
    """
    protein = ""
    # Step through the RNA sequence 3 letters (1 codon) at a time
    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "?")

        if amino_acid == "*":  # Stop codon reached
            break

        protein += amino_acid

    return protein


def print_report(sequence, rna_sequence, protein):
    """Print a clean summary report of the whole analysis."""
    base_counts = count_bases(sequence)

    print("\n----- DNA Analysis Report -----")
    print(f"Sequence      : {sequence}")
    print(f"Length        : {len(sequence)} bases")
    print(f"Base Counts   : A={base_counts['A']}  T={base_counts['T']}  "
          f"G={base_counts['G']}  C={base_counts['C']}")
    print(f"GC Content    : {gc_content(sequence)}%")
    print(f"RNA Sequence  : {rna_sequence}")
    print(f"Protein       : {protein}")
    print("--------------------------------\n")


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

def main():
    print("=== DNA Sequence Analysis Tool ===")
    user_input = input(
        "Enter a DNA sequence (or press Enter to use a sample sequence): "
    )

    # If the user doesn't type anything, use a sample sequence
    sequence = clean_sequence(user_input) if user_input else "ATGCGTACGTTAGC"

    if not is_valid_dna(sequence):
        print("Error: sequence contains invalid characters. "
              "Only A, T, G, and C are allowed.")
        return

    rna_sequence = transcribe_to_rna(sequence)
    protein = translate_to_protein(rna_sequence)

    print_report(sequence, rna_sequence, protein)


if __name__ == "__main__":
    main()
