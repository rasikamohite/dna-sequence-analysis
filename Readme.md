 # 🧬 DNA Sequence Analysis Using Python

A beginner-friendly bioinformatics project that analyzes a DNA sequence step
by step: validation, base counting, GC content, transcription, and protein
translation.

**Author:** Rasika Mohite

---

## 📌 Project Overview

This project demonstrates a simple computational biology pipeline in Python.
Given a DNA sequence, the program cleans and validates it, then performs a
full analysis, ending with a plain-English report.

## 🎯 Objectives

- Analyze a DNA sequence using Python
- Count the four nucleotide bases: A, T, G, C
- Calculate GC content
- Validate DNA sequences (only A, T, G, C allowed)
- Perform DNA → RNA transcription
- Perform RNA → protein translation (using the full 64-codon table)
- Generate a final analysis report

## 🧪 Workflow

```text
DNA Sequence
      ↓
Cleaning & Validation
      ↓
Nucleotide Counting
      ↓
GC Content Calculation
      ↓
DNA → RNA Transcription
      ↓
RNA → Protein Translation
      ↓
Final Analysis Report
```

## 🚀 How to Run

1. Make sure Python 3 is installed on your machine.
2. Clone this repository:
   ```bash
   git clone https://github.com/rasikamohite/dna-sequence-analysis.git
   cd dna-sequence-analysis
   ```
3. Run the script:
   ```bash
   python3 dna_analysis.py
   ```
4. Enter your own DNA sequence when prompted, or just press **Enter** to use
   the built-in sample sequence.

## 💻 Example Output

```
=== DNA Sequence Analysis Tool ===
Enter a DNA sequence (or press Enter to use a sample sequence): ATGAAACGCTAA

----- DNA Analysis Report -----
Sequence      : ATGAAACGCTAA
Length        : 12 bases
Base Counts   : A=6  T=2  G=2  C=2
GC Content    : 33.33%
RNA Sequence  : AUGAAACGCUAA
Protein       : MKR
--------------------------------
```

## 🧠 What I Learned

- How to represent and manipulate biological sequences as strings in Python
- How DNA transcription (DNA → RNA) and translation (RNA → protein) work
- How to build and use a full codon-to-amino-acid lookup table
- How to structure a script into small, reusable functions instead of one
  long block of code

## 🔮 Future Improvements

- Accept sequences from a `.fasta` file
- Support reverse complement calculation
- Add unit tests
- Build a simple web interface (Flask/Streamlit)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
