import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Dados de temperatura
temperaturas = [
    25.6, 25.9, 25.9, 25.9, 25.9, 25.9, 25.8, 25.8, 25.8, 25.9, 25.9, 26.0, 26.0, 26.1, 26.1, 26.1, 26.1, 26.1, 
    26.1, 26.1, 26.1, 26.2, 26.1, 26.1, 26.1, 26.1, 26.1, 26.2, 26.1, 26.1, 26.0, 26.0, 26.0, 25.9, 25.9, 25.9, 
    25.8, 25.9, 25.9, 25.8, 25.7, 25.8, 25.8, 25.7, 25.8, 25.8, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 
    25.7, 25.6, 25.7, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 
    25.5, 25.6, 25.6, 25.6, 25.5, 25.6, 25.5, 25.5, 25.5, 25.5, 25.5, 25.5, 25.4, 25.4, 25.6, 25.6, 25.5, 25.6, 
    25.5, 25.5, 25.5, 25.5, 25.5, 25.5, 25.4, 25.4, 25.4, 25.4, 25.5, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 
    25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.3, 25.4, 25.4, 25.4, 25.3, 25.3, 25.3, 25.2, 25.3, 25.2, 25.3, 
    25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.1, 25.1, 25.2, 
    25.1, 25.1, 25.1, 25.1, 25.1, 25.1, 25.1, 25.1
]

# Tempo (em segundos)
tempo_ajustado = np.array(range(len(temperaturas)))

# Selecionar os pontos chave (máximo, mínimo, e alguns intermediários)
indice_max = np.argmax(temperaturas)
indice_min = np.argmin(temperaturas)

# Pontos intermediários escolhidos manualmente
indice_intermediario = int((indice_max + indice_min) / 2)

# Corrigir a concatenação do índice intermediário
indices_chave = np.sort(np.array([indice_max, indice_min, indice_intermediario]))

# Obter os tempos e temperaturas correspondentes aos pontos chave
tempos_chave = tempo_ajustado[indices_chave]
temperaturas_chave = np.array(temperaturas)[indices_chave]

# Interpolação linear entre os pontos chave
tempo_interpolado = np.linspace(tempos_chave[0], tempos_chave[-1], 500)
interp_func = interp1d(tempos_chave, temperaturas_chave, kind='linear')
temperaturas_interpoladas = interp_func(tempo_interpolado)

# Criação da curva de resfriamento interpolada
plt.figure(figsize=(10, 6))
plt.plot(tempo_ajustado, temperaturas, 'o', linestyle='-', color='blue', label='Curva de Resfriamento (Original)')
plt.plot(tempo_interpolado, temperaturas_interpoladas, '-', color='red', label='Curva Suavizada (Interpolada)')
plt.title('Curva de Resfriamento Suavizada a partir de Pontos Chave')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
