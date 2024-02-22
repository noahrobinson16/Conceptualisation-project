import math

# Correspond à la constante mathématique e = 2.718281…
from math import e

print(math.e == e)
print(e)

# Correspond à la constante mathématique π = 3.141592…
from math import pi

print(math.pi == pi)
print(pi)

# Correspond à la constance mathématique τ = 6.283185…
from math import tau

print(math.tau == tau)
print(tau)

# Correspond à un point flottant, définition flou
from math import nan

print(math.nan == nan)
print(nan)
nan_plus_un = nan + 1
print(nan_plus_un)

# Correspond à l'infini
from math import inf

print(math.inf == inf)
print(inf)
inf_plus_un = inf + 1
print(inf_plus_un)
inf_négatif = inf * -1
print(inf_négatif)
