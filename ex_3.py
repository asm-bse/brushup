import sympy as sp

x = sp.symbols('x')

f = 5 * x**3
g = sp.sqrt(x)
h = sp.ln(x)
p = sp.exp(x)

f_prime = sp.diff(f, x)
g_prime = sp.diff(g, x)
h_prime = sp.diff(h, x)
p_prime = sp.diff(p, x)

print(f"f'(x) = {f_prime}")
print(f"g'(x) = {g_prime}")
print(f"h'(x) = {h_prime}")
print(f"p'(x) = {p_prime}")
