clf=[3,6,4,8,5]
suma=sum(clf)
prom=suma/5
print("El promedio es", prom)
may=[n for n in clf if n>prom]
print("Los números mayores al promedio son", may)
