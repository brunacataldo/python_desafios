print('Quiz de Matemática.')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Junior comeu 25% do total de balas. Sabendo que ele tinha 36 balas, quantas balas ainda lhe restam?',
        'respostas': {'a' : '18 balas','b' : '21 balas','c' : '25 balas'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': '90 é quantos porcento de 120?',
        'respostas': {'a': '30%', 'b': '50%', 'c': '75%'},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Um produto que recebeu um desconto de 35%, tem como preço atual de R$320,00. Qual era o preço anterior desde produto?',
        'respostas': {'a': 'R$430,00', 'b': 'R$432,00', 'c': 'R$435,00'},
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Em uma prova Maria obteve 75% dos acertos de 60 questões. Quantas questões ela errou?',
        'respostas': {'a': '15 questões', 'b': '20 questões', 'c': '35 questões'},
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': '45 é quantos porcento de 50?',
        'respostas': {'a': '40%', 'b': '75%', 'c': '90%'},
        'resposta_certa': 'c',
    },

}

respostas_certas = 0
for pk, pv in perguntas.items():                    #pk, pv: pergunta-chave(key), pergunta-valor
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk , rv in pv['respostas'].items():         #rk, rv: resposta-chave(key), resposta-valor
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Resposta correta.')
        respostas_certas += 1
    else:
        print('Resposta errada.')

q_perguntas = len(perguntas)
porcentagem_acerto = int(respostas_certas / q_perguntas * 100)
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')

if porcentagem_acerto > 70:
    print('Parabéns! Você passou no teste.')
if porcentagem_acerto < 70:
    print('Sua nota está abaixo da média. Estude mais na próxima!')
