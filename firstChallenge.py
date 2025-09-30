# Crie um método de receber um número inteiro e retornar o valor da potência de 10 relativo à casa
# [1000> 1* 10^3(ignora zeros), 12 > 1:1 2:0]
def decomporAlgarismo(num):
    if num == 0:
        return {0:0}
    output = {}
    numString = str(num)
    lenght=len(numString)

    for i, digito in enumerate(numString):
        if digito != "0":
            # Chaves de dicionário precisam ser únicas ou vai pular chaves repetidas
            output[f"algarismo: {digito} index: {i}"] = f"potência: {lenght - i - 1}"
    return output

print("1000: ", decomporAlgarismo(1000))
print("2445: ", decomporAlgarismo(2445))
print("1431: ", decomporAlgarismo(1431))