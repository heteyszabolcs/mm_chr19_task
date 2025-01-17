import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('../output/abundance.tab', sep='\t')
data = data[['Gene ID', 'Reference', 'Gene Name', 'TPM']]
data = data.sort_values('TPM', ascending=False)
data = data[data['TPM'] > 1]
data = data[data['Reference'] == '19']
data = data[data['Gene Name'] != '-']
data['log10_TPM'] = np.log10(data['TPM'].to_list())
data.shape

plt.figure(figsize=(12, 6))
sns.barplot(data=data.iloc[1:60,:],
            x='Gene Name',
            y='log10_TPM',
            color='skyblue')

plt.title('Top genes of chr19 ranked by TPM', pad=20, fontsize=18)
plt.xlabel('gene symbol', fontsize=14)
plt.ylabel('log10 TPM', fontsize=14)
plt.xticks(rotation=90, ha='center', fontsize=10)
plt.tight_layout()
plt.show()
plt.savefig("../output/top_genes_chr19-barplot.pdf")
