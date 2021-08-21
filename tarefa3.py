# 3. Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada.
nome = str(input("Qual o seu nome?"))
diaNascimento = int(input("Em que dia você nasceu?"))
mesNascimento = int(input("Em que mês você nasceu?"))
anoNascimento = int(input("Em que ano você nascseu?"))
print("Você é {}, nascido em {}/{}/{}, você é digno.". format(nome,diaNascimento,mesNascimento,anoNascimento))
