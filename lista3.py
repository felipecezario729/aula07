fruta = ['maça', 'banana', 'laranja', 'pitaya', ' mamão']
print(f'todas as frutas ===>{fruta}')
print(f'todas as frutas ===>{fruta[4]}')
fruta.remove('laranja')
tamanho = len(fruta)
print(f'O tamanho da lista é {tamanho}')
print('-------')
fruta[1] =  'uva'
print(f'todas as frutas ===>{fruta}')
fruta.insert(1, 'abacaxi')
print(f'lista atualizada  ===>{fruta}')
tamanho = len(fruta)
print(f'O tamanho da lista é {tamanho}')


