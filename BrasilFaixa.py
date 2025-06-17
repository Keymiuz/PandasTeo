# %%
import matplotlib.pyplot as plt
import numpy as np

# Dados estimados da pirâmide etária do Brasil em 1900
faixas_etarias = [
    '80+', '75-79', '70-74', '65-69', '60-64',
    '55-59', '50-54', '45-49', '40-44', '35-39',
    '30-34', '25-29', '20-24', '15-19',
    '10-14', '5-9', '0-4'
]

# Distribuição percentual aproximada para homens e mulheres
homens = np.array([0.2, 0.3, 0.4, 0.5, 0.6,
                    0.8, 1.0, 1.2, 1.4, 1.6,
                    1.9, 2.1, 2.5, 3.0,
                    4.5, 5.0, 6.0])

mulheres = np.array([0.2, 0.3, 0.4, 0.5, 0.6,
                      0.8, 1.0, 1.2, 1.4, 1.6,
                      1.9, 2.1, 2.5, 3.0,
                      4.5, 5.0, 6.0])

faixas_etarias = faixas_etarias[::-1]
homens = homens[::-1]
mulheres = mulheres[::-1]  ## inverti para visualização facilitada

## Configurações de eixo
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(faixas_etarias, -homens, color='blue', label='Homens')
ax.barh(faixas_etarias, mulheres, color='pink', label='Mulheres')
ax.set_xlabel('Percentual da População (%)')
ax.set_title('Pirâmide Etária do Brasil em 1900 (Estimativa)')
ax.set_xlim(-7, 7)
ax.set_xticks(np.arange(-7, 8, 1))
ax.set_xticklabels([abs(x) for x in np.arange(-7, 8, 1)])
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()



# Dados estimados da pirâmide etária do Brasil em 2025
faixas_etarias_2025 = [
    '80+', '75-79', '70-74', '65-69', '60-64',
    '55-59', '50-54', '45-49', '40-44', '35-39',
    '30-34', '25-29', '20-24', '15-19',
    '10-14', '5-9', '0-4'
]

homens_2025 = np.array([1.5, 1.7, 1.9, 2.0, 2.2,
                         2.4, 2.5, 2.6, 2.7, 2.8,
                         2.9, 3.0, 3.1, 2.8,
                         2.4, 2.2, 2.0])

mulheres_2025 = np.array([2.0, 2.2, 2.4, 2.5, 2.7,
                           2.9, 3.0, 3.1, 3.2, 3.3,
                           3.4, 3.5, 3.6, 3.2,
                           2.7, 2.5, 2.3])

faixas_etarias_2025 = faixas_etarias_2025[::-1]
homens_2025 = homens_2025[::-1]
mulheres_2025 = mulheres_2025[::-1]
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(faixas_etarias_2025, -homens_2025, color='blue', label='Homens')
ax.barh(faixas_etarias_2025, mulheres_2025, color='pink', label='Mulheres')
ax.set_xlabel('Percentual da População (%)')
ax.set_title('Pirâmide Etária do Brasil em 2025 (Estimativa)')
ax.set_xlim(-5, 5)
ax.set_xticks(np.arange(-5, 6, 1))
ax.set_xticklabels([abs(x) for x in np.arange(-5, 6, 1)])
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()



# %%
