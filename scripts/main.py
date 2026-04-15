from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio import AlignIO


PROJECT_ROOT = Path("/Users/gerdalukosiute/Downloads/iGEM/BMC/Conserved_AA")
ALIGNMENT_FILE = PROJECT_ROOT / "results" / "BMC-T1" / "alignment" / "BMC-T1_aligned.fasta"
OUTPUT_DIR = PROJECT_ROOT / "results" / "BMC-T1" / "analysis"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALIGNMENT_CSV = OUTPUT_DIR / "BMC-T1_alignment_scores.csv"
QUERY_CSV = OUTPUT_DIR / "BMC-T1_query_residue_scores.csv"
PLOT_PNG = OUTPUT_DIR / "BMC-T1_conservation_plot.png"
PYMOL_SCRIPT = OUTPUT_DIR / "BMC-T1_color_by_conservation.pml"


def shannon_entropy(residues: list[str]) -> float:
    if not residues:
        return np.nan
    counts = {}
    for aa in residues:
        counts[aa] = counts.get(aa, 0) + 1
    probs = np.array(list(counts.values()), dtype=float) / len(residues)
    return float(-np.sum(probs * np.log2(probs)))


def main() -> None:
    alignment = AlignIO.read(str(ALIGNMENT_FILE), "fasta")
    n_seqs = len(alignment)
    aln_len = alignment.get_alignment_length()

    print(f"Loaded alignment: {n_seqs} sequences, {aln_len} columns")

    query_record = alignment[0]
    query_aligned = str(query_record.seq)

    alignment_rows = []
    query_rows = []

    query_resi = 0

    for i in range(aln_len):
        column = alignment[:, i]
        residues = [aa for aa in column if aa != "-"]
        entropy = shannon_entropy(residues)

        counts = {}
        for aa in residues:
            counts[aa] = counts.get(aa, 0) + 1
        consensus = max(counts, key=counts.get) if counts else "-"
        occ = len(residues) / len(column) if len(column) > 0 else 0.0

        alignment_rows.append(
            {
                "alignment_position": i + 1,
                "consensus_residue": consensus,
                "occupancy": occ,
                "shannon_entropy": entropy,
            }
        )

        query_aa = query_aligned[i]

        if query_aa != "-":
            query_resi += 1
            query_rows.append(
                {
                    "query_residue_number": query_resi,
                    "query_residue": query_aa,
                    "alignment_position": i + 1,
                    "occupancy": occ,
                    "shannon_entropy": entropy,
                }
            )

    aln_df = pd.DataFrame(alignment_rows)
    max_entropy = np.nanmax(aln_df["shannon_entropy"].values)
    aln_df["conservation_score"] = max_entropy - aln_df["shannon_entropy"]
    aln_df.to_csv(ALIGNMENT_CSV, index=False)

    query_df = pd.DataFrame(query_rows)
    query_df["conservation_score"] = max_entropy - query_df["shannon_entropy"]
    query_df.to_csv(QUERY_CSV, index=False)

    plt.figure(figsize=(12, 4))
    plt.plot(query_df["query_residue_number"], query_df["shannon_entropy"])
    plt.xlabel("Query residue number")
    plt.ylabel("Shannon entropy")
    plt.title("BMC-P conservation profile (query residues)")
    plt.tight_layout()
    plt.savefig(PLOT_PNG, dpi=300)

    with open(PYMOL_SCRIPT, "w") as f:
        f.write("reinitialize\n")
        f.write("# Load your structure manually before running these commands if needed\n")
        f.write("hide everything\n")
        f.write("show cartoon\n")
        f.write("spectrum b, blue_white_red, minimum=0, maximum={:.6f}\n".format(max_entropy))
        f.write("set cartoon_transparency, 0.15\n")
        f.write("bg_color white\n")
        f.write("set color_missing, grey70\n")
        f.write("alter all, b=0.0\n")

        for _, row in query_df.iterrows():
            resi = int(row["query_residue_number"])
            score = float(row["conservation_score"])
            f.write(f"alter resi {resi}, b={score:.6f}\n")

        f.write("sort\n")
        f.write("rebuild\n")
        f.write("spectrum b, blue_white_red, minimum=0, maximum={:.6f}\n".format(max_entropy))
        f.write("ramp_new conservation_ramp, all, [0, {:.6f}], [blue, red]\n".format(max_entropy))
        f.write("show sticks, byres (resi ")
        f.write("+".join(str(int(x)) for x in query_df.nlargest(15, "conservation_score")["query_residue_number"]))
        f.write(")\n")
        f.write("set stick_radius, 0.2\n")

    print(f"Saved alignment-level CSV: {ALIGNMENT_CSV}")
    print(f"Saved query-residue CSV: {QUERY_CSV}")
    print(f"Saved plot: {PLOT_PNG}")
    print(f"Saved PyMOL script: {PYMOL_SCRIPT}")
    print(query_df.head(10).to_string(index=False))


if __name__ == "__main__":
    main()