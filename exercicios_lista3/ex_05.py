#Fácil 5- Faça um programa para a leitura de duas notas parciais de um aluno.A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;A mensagem “Aprovado com Distinção”, se a média for igual a dez;A mensagem “Reprovado” se a média for menor de do que sete;

nome=input('Digite o nome do aluno: ')
nota_1bi=float(input('Digite a nota do aluno no primeiro bimestre: '))
nota_2bi=float(input('Digite a nota do aluno no segundo semestre: '))

media=(nota_1bi+nota_2bi)/2

if media >= 7 and media<10:
    print('Aprovado com distinção')
elif media==10:
    print('Você é pica menor')
else:
    print('Ramelou na missão: REPROVADO')        