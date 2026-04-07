# Order:
# 1 = 1P1/2
# 2 = 1P3/2

# Single Particle Energies (SPE)
SPE = {
    1: 2.419,
    2: 1.129,
}

# Two-Body Matrix Elements (TBME)
# Format: (a, b, c, d, J, T, value)
TBME = [
    (1, 1, 1, 1, 0, 1,  0.2440000),
    (1, 1, 1, 1, 1, 0, -4.2921500),

    (2, 1, 1, 1, 1, 0,  1.2047000),

    (2, 1, 2, 1, 1, 0, -6.5627000),
    (2, 1, 2, 1, 1, 1,  0.7344000),
    (2, 1, 2, 1, 2, 0, -4.0579000),
    (2, 1, 2, 1, 2, 1, -1.1443000),

    (2, 2, 1, 1, 0, 1, -5.0526000),
    (2, 2, 1, 1, 1, 0,  1.7698000),

    (2, 2, 2, 1, 1, 0,  3.2056000),
    (2, 2, 2, 1, 2, 1, -1.7423000),

    (2, 2, 2, 2, 0, 1, -3.3287000),
    (2, 2, 2, 2, 1, 0, -3.4362000),
    (2, 2, 2, 2, 2, 1,  0.0878000),
    (2, 2, 2, 2, 3, 0, -7.2668000),
]

BASIS_6Li = [(1,1), (1,2), (2,1), (2,2)]
print(f"Orbitals : {list(SPE.keys())}")
print(f"SPE values: {list(SPE.values())} MeV")
print(f"Number of TBME : {len(TBME)}")
print(f"Basis dimension : {len(BASIS_6Li)}")

J1T0 = [(n1,n2,n3,n4,V) for (n1, n2, n3, n4, J, T, V) in TBME if J==1 and T ==0 ]
print(f"J = 1, T = 0, elements : {J1T0} ")
J2T0 = [(n1,n2,n3,n4,V) for (n1,n2,n3,n4, J, T, V) in TBME if J==2 and T ==0 ]
print(f"J = 2, T = 0, elements : {J2T0}")
print(f"TBME : {TBME[0][6]}")
print(f"TBME : {TBME[1][6]}")
print(f"TBME : {TBME[2][6]}")
print(f"TBME : {TBME[3][6]}")
print(f"TBME : {TBME[4][6]}")
print(f"TBME : {TBME[5][6]}")
print(f"TBME : {TBME[6][6]}")
