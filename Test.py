def surjection_check(func, domain, codomain):
    rng = set()
    for x in domain:
        rng.add(func(x))
    return rng == set(codomain)

f1 = lambda x: x ** 2
domain = list(range(-10, 11))
codomain = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
print(surjection_check(f1, domain, codomain))