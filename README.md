# BMC Conserved Amino Acid Analysis Pipeline

## Project Overview

This project performs sequence conservation analysis on Bacterial Microcompartment (BMC) shell proteins, specifically focusing on BMC-P (pentameric vertex proteins) and BMC-T1 (tandem-domain shell proteins).

The pipeline identifies conserved amino acid residues across homologous sequences using a reproducible workflow based on BLAST, multiple sequence alignment, and entropy-based conservation scoring, followed by 3D structural visualization in PyMOL.

## Biological Context

### What are Bacterial Microcompartments?

Bacterial microcompartments (BMCs) are protein-based organelles that encapsulate metabolic pathways within a selectively permeable shell.

**Key shell protein types:**

- **BMC-P (Pentamer)**: Forms the vertices of the microcompartment shell (5-fold symmetry)
- **BMC-T (Tandem-domain proteins, e.g. BMC-T1)**: Larger shell proteins that form facets, often involved in metabolite transport

### Why Analyze Conservation?

Evolutionarily conserved residues are strong indicators of:

- **Structural importance** – maintaining protein fold and oligomerization
- **Functional importance** – e.g. pore formation, substrate transport
- **Evolutionary constraint** – mutations are deleterious and selected against

**This analysis helps:**

- Identify critical residues
- Infer functional regions (e.g. pores, interfaces)
- Guide mutagenesis and engineering
- Support structural interpretation

## Pipeline Workflow

### Step 1: Homolog Search (BLAST)

**Input:** Query protein FASTA (e.g. from UniProt)

**Method:**
- Homologous sequences are retrieved using BLASTp against the NCBI nr database
- Typically ~50–100 top hits are collected

**Output:**
- FASTA file of homologous protein sequences (results/BMC-T1/raw/BMC-T1_homologs.fasta)

### Step 2: Multiple Sequence Alignment (MSA)

**Tool:** MAFFT

**Method:**
- Query sequence is combined with BLAST homologs
- Alignment performed using:
  ```
  mafft --auto input.fasta > aligned.fasta
  ```

**Output:**
- Aligned FASTA file (*_aligned.fasta)

### Step 3: Conservation Scoring

Each alignment column is analyzed using Shannon entropy:

$$H = -\sum_{i=1}^{n} p_i \log_2(p_i)$$

**Where:**
- $p_i$ = frequency of amino acid $i$

**Conservation score:**
$$\text{Conservation} = H_{\text{max}} - H_{\text{position}}$$

- Low entropy → conserved
- High entropy → variable

**Additional metrics:**
- Occupancy: fraction of non-gap residues
- Consensus residue: most frequent amino acid
- Query mapping: alignment positions mapped back to the query sequence

### Step 4: Structure Mapping (PyMOL)

Conservation scores are mapped onto 3D structures (e.g. SWISS-MODEL predictions) by:

- Writing scores into the B-factor field
- Coloring structure using: `spectrum b, blue_white_red`

**Color interpretation:**

| Color | Meaning |
|-------|---------|
| <span style="color: red;">Red</span> | Highly conserved |
| <span style="color: lightgray;">White</span> | Intermediate |
| <span style="color: blue;">Blue</span> | Variable |

## Directory Structure

```
Conserved_AA/
├── data/
│   ├── BMC-P/
│   │   ├── BMC-P.fasta
│   │   └── D0LHE5_updated/
│   │       └── swis_model_pentamer.cif
│   └── BMC-T/
│       └── BMC-T1/
│           ├── BMC-T1.fasta
│           └── BMC-T1_swiss_model.cif
├── results/
│   ├── BMC-P/
│   │   ├── raw/
│   │   ├── alignment/
│   │   └── analysis/
│   └── BMC-T1/
│       ├── raw/
│       ├── alignment/
│       └── analysis/
└── scripts/
    └── main.py
```

## Output Files

### CSV Outputs

#### `*_query_residue_scores.csv`

Mapped to the query sequence:

| Column | Description |
|--------|-------------|
| query_residue_number | Residue position in query |
| query_residue | Amino acid type |
| alignment_position | Corresponding MSA column |
| occupancy | Non-gap fraction |
| shannon_entropy | Column entropy |
| conservation_score | Conservation ranking |

### Plots

#### `*_conservation_plot.png`
- X-axis: residue number
- Y-axis: entropy
- Low values = conserved regions

### PyMOL Script

#### `*_color_by_conservation.pml`
- Maps conservation to structure
- Highlights most conserved residues

## Running the Analysis

### Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install biopython numpy pandas matplotlib mafft
```

### Workflow

1. Run BLAST (manual step via NCBI)
2. Download homolog FASTA, store (e.g. results/BMC-T1/raw/BMC-T1_homologs.fasta)
3. Combine with query sequence 
    ```bash
    cat data/BMC-T1/BMC-T1.fasta \
    results/BMC-T1/raw/BMC-T1_homologs.fasta \
    > results/BMC-T1/raw/BMC-T1_all.fasta
    ```
4. Align with MAFFT:
   ```bash
   mafft --auto \
   results/BMC-T1/raw/BMC-T1_all.fasta \
   > results/BMC-T1/alignment/BMC-T1_aligned.fasta
   ```
5. Run analysis (make sure to change main.py paths):
   ```bash
   python scripts/main.py
   ```

## Biological Interpretation

### <span style="color: red;">Conserved Regions</span>
**Likely:**
- subunit interfaces
- structural cores
- functional pores

### <span style="color: blue;">Variable Regions</span>
**Likely:**
- surface-exposed loops
- flexible regions
- lineage-specific variation

### Important filtering note

Positions with occupancy < 0.7 should be interpreted cautiously due to alignment gaps.

## Future Directions

- Compare conservation across BMC types
- Integrate with mutagenesis experiments
- Combine with structural interface analysis

## Notes

This pipeline provides a lightweight, reproducible alternative to ConSurf, using standard bioinformatics tools and custom analysis.