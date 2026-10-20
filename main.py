"""Studi Kasus 5 - Human computer interaction and data visualization.
Kasus: evaluasi usability aplikasi dengan System Usability Scale (SUS) pada 12 responden
(data sintetis), lalu visualisasi yang ramah pembaca: palet colorblind-safe, judul berupa
insight, dan anotasi langsung.
"""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
q = [f"Q{i}" for i in range(1, 11)]
pos, neg = ["Q1", "Q3", "Q5", "Q7", "Q9"], ["Q2", "Q4", "Q6", "Q8", "Q10"]
resp = pd.DataFrame(index=range(12), columns=q, dtype=int)
resp[pos] = rng.integers(2, 6, (12, 5))      # pernyataan positif: cenderung tinggi
resp[neg] = rng.integers(1, 4, (12, 5))      # pernyataan negatif: cenderung rendah

# Skor SUS: item ganjil (skor-1), item genap (5-skor), total x 2.5
resp["SUS"] = ((resp[pos] - 1).sum(axis=1) + (5 - resp[neg]).sum(axis=1)) * 2.5
mean = resp.SUS.mean()
grade = "A (Excellent)" if mean >= 80.3 else "B (Good)" if mean >= 68 else "Perlu perbaikan"
print(f"Skor SUS rata-rata: {mean:.1f} -> {grade}  (benchmark rata-rata = 68)")

CB = {"biru": "#0072B2", "oranye": "#E69F00", "abu": "#7F7F7F"}           # palet Okabe-Ito
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
order = resp.SUS.sort_values().index
colors = [CB["oranye"] if v < 68 else CB["biru"] for v in resp.SUS[order]]
ax[0].barh([f"R{i+1}" for i in order], resp.SUS[order], color=colors)
ax[0].axvline(68, ls="--", c=CB["abu"]); ax[0].text(69, 0, "Rata-rata industri (68)", color=CB["abu"], fontsize=9)
ax[0].set(title=f"{(resp.SUS<68).sum()} dari 12 responden menilai di bawah standar", xlabel="Skor SUS")

item = resp[q].astype(float).mean()
ax[1].bar(q, item, color=[CB["biru"] if c in pos else CB["oranye"] for c in q])
ax[1].set(title="Biru: pernyataan positif | Oranye: negatif", ylabel="Rata-rata skor (1-5)")
for a in ax: a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("outputs/case5_hci.png", dpi=150)
print("Gambar tersimpan: outputs/case5_hci.png")
