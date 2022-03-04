leituraAnt = int(input("Leitura anterior (kWh) = "))
leituraAtual = int(input("Leitura atual (kWh) = "))
consumo = leituraAtual - leituraAnt
usoSistDistr = consumo * 0.40942
energiaTE = consumo * 0.38317
pisPasep = consumo * 0.01
cofins = consumo * 0.0462
cipSBdoCampoMunicipal = 24.01
valorTotal = usoSistDistr + energiaTE + pisPasep + cofins + cipSBdoCampoMunicipal
print("\nConsumo do mês (kWh) =",consumo)
print("TUSD = R$",round(usoSistDistr,2))
print("TE = R$",round(energiaTE,2))
print("PIS/PASEP = R$ %.2f"%pisPasep)
print("COFINS = R$ %.2F"%cofins)
print("CIP = %.2f"%cipSBdoCampoMunicipal)
print("Total a pagar = R$ %.2f"%valorTotal)