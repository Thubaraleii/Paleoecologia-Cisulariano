# Plotting without the title on top, as requested

plt.figure(figsize=(6, 10))
plt.plot(df_depth_variation['Número total de fósseis'], df_depth_variation['Profundidade Média (cm)'], marker='o', linestyle='-', color='orange')
plt.xlabel('Número total de fósseis')
plt.ylabel('Profundidade Média (cm)')
plt.gca().invert_yaxis()  # Inverting Y-axis for depth visualization
plt.grid(True)
plt.show()
