# A = P(1 + R/100) ^ t 

# Compound Interest = A – P 

ci = lambda p,r,t :(p*(1+r/100)**t) - p

print(ci(10000, 10.25, 5))
