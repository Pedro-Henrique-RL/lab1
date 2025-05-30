def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_c = float(input("Digite a temperatura em graus Celsius: "))
temperatura_f = celsius_para_fahrenheit(temperatura_c)
print(f"{temperatura_c}°C equivalem a {temperatura_f:.2f}°F.")
