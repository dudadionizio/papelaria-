assert eh_numero ("24,90")
assert eh_numero ("3")
assert not eh_numero ("dez")
assert not eh_numero ("-5")

assert validar_produto ("caderno", "24,90","15") == []
assert validar_produto ("caderno", "0", "15") == ["o preço precisa ser um numero maior que zero."]
assert len (validar_produto ("", "abc", "1,5")) == 3
assert validar_produto ("Lápis", "1.50", "0") == []

print("OK: todas as regras de validação passaram")
