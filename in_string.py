def check_vowels():
    nombre = input()
    a = ("a")
    e = ("e")
    i = ("i")
    o = ("o")
    u = ("u")
    A = ("A")
    E = ("E")
    I = ("I")
    O = ("O")
    U = ("U")
    print ("contiene a:",(a in nombre) or (A in nombre))
    print ("contiene e:",(e in nombre) or (E in nombre))
    print ("contiene i:",(i in nombre) or (I in nombre))
    print ("contiene o:",(o in nombre) or (O in nombre))
    print ("contiene u:",(u in nombre) or (U in nombre))
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
