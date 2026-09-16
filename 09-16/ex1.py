dados = [
    {"dia": 13, "mes": 9, "ano": 2026, "temp": 17},
    {"dia": 14, "mes": 9, "ano": 2026, "temp": 19},
    {"dia": 15, "mes": 9, "ano": 2026, "temp": 21},
    {"dia": 16, "mes": 9, "ano": 2026, "temp": 18},
]

for info in dados:
    print(f"{info['dia']}/{info['mes']:02d}/{info['ano']} - Temp {info['temp']}°C")