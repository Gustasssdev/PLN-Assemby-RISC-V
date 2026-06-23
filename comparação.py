import matplotlib.pyplot as plt

# ── Leitura arquivo Python: lê APENAS até o primeiro \n ─────────
with open('/content/Resultado.txt', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()
    linha_python = raw.split('\n')[0]   # só a primeira linha, ignora o resto

lista_python = [linha_python]

# ── Leitura arquivo Assembly: lê APENAS até o primeiro \x00 ─────
with open('/content/resultado.txt', 'rb') as f:
    raw = f.read()
    linha_assembly = raw.split(b'\x00')[0].decode('utf-8', errors='ignore')

lista_assembly = [linha_assembly]

print(f"Python  : {lista_python}")
print(f"Assembly: {lista_assembly}")

# ── String ideal (tratamento perfeito) ──────────────────────────
STRING_IDEAL = "luz e diogo, gustavo sao da computacao"

# ── Levenshtein ─────────────────────────────────────────────────
def levenshtein_ratio(a: str, b: str) -> tuple[int, float]:
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev, dp[0] = dp[:], i
        for j in range(1, n + 1):
            dp[j] = prev[j-1] if a[i-1] == b[j-1] else 1 + min(prev[j], dp[j-1], prev[j-1])
    dist = dp[n]
    pct  = (1 - dist / max(m, n)) * 100 if max(m, n) else 100.0
    return dist, pct

dist_py,  pct_py  = levenshtein_ratio(lista_python[0],  STRING_IDEAL)
dist_asm, pct_asm = levenshtein_ratio(lista_assembly[0], STRING_IDEAL)

print(f"\nString ideal : \"{STRING_IDEAL}\"")
print(f"Python       : {pct_py:.2f}%  (distância: {dist_py} edição(ões))")
print(f"Assembly     : {pct_asm:.2f}%  (distância: {dist_asm} edição(ões))")

# ── Gráfico ─────────────────────────────────────────────────────
labels  = ['Python', 'Assembly']
valores = [pct_py, pct_asm]
diff    = [100 - v for v in valores]
cores   = ['#1D9E75', '#378ADD']

fig, ax = plt.subplots(figsize=(7, 5))

bars = ax.bar(labels, valores, color=cores, width=0.45, label='Similaridade com ideal')
ax.bar(labels, diff, bottom=valores, color='#E0E0E0', width=0.45, label='Diferença para ideal')

for bar, val, dist in zip(bars, valores, [dist_py, dist_asm]):
    ax.text(bar.get_x() + bar.get_width()/2, val/2,
            f'{val:.1f}%', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    ax.text(bar.get_x() + bar.get_width()/2, val + 3,
            f'{dist} edição(ões)', ha='center', va='bottom',
            fontsize=9, color='#555')

ax.set_ylim(0, 115)
ax.set_ylabel('Proximidade à string ideal (%)')
ax.set_title(f'Levenshtein vs ideal: "{STRING_IDEAL}"', fontsize=10, pad=12)
ax.axhline(100, linestyle='--', color='#aaa', linewidth=0.8)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.spines[['top', 'right']].set_visible(False)
ax.legend(fontsize=9)

plt.tight_layout()
plt.show()