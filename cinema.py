input_text_1 = str(input('do user wants to be an actor? yes / no '))
if input_text_1 == 'yes':
    input_text_2 = str(input('who do you wanna be - hulk or loki? hulk / loki '))
    if input_text_2 == 'hulk':
        input_text_3 = str(input('your biceps? '))
        if int(input_text_3) < 60:
            print('unluck')
        elif int(input_text_3) >= 60:
            print('go filming')
        else:
            print('error 404')
    elif input_text_2 == 'loki':
        input_text_4 = str(input('who do you love more - mom or dad? mom / dad '))
        if input_text_4 == 'dad':
            print('go home bro')
        elif input_text_4 == 'mom':
            print('go ask your dad')
        else:
            print('error 404')    
    else:
        print('error 404')
elif input_text_1 == 'no':
    print('goodbye bro')
else:
    print('error 404')