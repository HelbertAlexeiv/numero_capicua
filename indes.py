#Input
num = int(input("Ingrese un numero entero de cinco digitos:"))
#Process/Output
if num <= 99999 and num>9999:
    f_digit = num//10000
    s_digit = (num//1000)-((f_digit*10))
    t_digit = (num//100)-((f_digit*100)+(s_digit*10))
    fo_digit = (num//10)-((f_digit*1000)+(s_digit*100)+(t_digit*10))
    fi_digit = num - ((f_digit*10000)+(s_digit*1000)+(t_digit*100)+(fo_digit*10))

    invert_num = (fi_digit*10000)+(fo_digit*1000)+(t_digit*100)+(s_digit*10)+f_digit
    if num == invert_num:
        print("El numero es capicuo")
    else:
        print("El numero no es capicuo")
else:
    print("El numero no es de cinco digitos")
