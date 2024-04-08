def inverter_string(s):
    inverted = ""
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i] 
    
    return inverted

input_string = input("Digite uma string para inverter: ")
inverted_string = inverter_string(input_string)
print("String original:", input_string)
print("String invertida:", inverted_string)

