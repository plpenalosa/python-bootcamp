class Numero():
	"""docstring for Numero() __init__(self, arg):
		super(Numero()__init__()
		self.arg = arg
	"""
	texto = {'0':'unidades', '1':'decenas','2':'centenas','3':'millares'}

	def __init__(self, numero):
		self.descomposicion = []
		self.numero = numero
		valor_texto = str(numero)
		pos = 0
		for x in valor_texto[::-1]:
			mult = int('1' + '0'*pos)
			self.descomposicion.append(int(x)*mult)

	def obtener_descomposicion_numero(self):
		print('Numero introducido: {x}'.format(x=self.numero))
		for pos in range(len(self.descomposicion)):
			print(str(self.descomposicion[pos]) + ' ' + self.texto[str(pos)])


def introducir_numero():
	print('\n\n')

	while True:
		try:
			nuevo_num = int(input('Introduce un numero: '))

		except:
			print('Lo que has introducido no es un numero, intentalo de nuevo')
			continue

		else:
			break

	return nuevo_num

def seguir_jugando():
	while True:
		print('\n\n')

		try:
			sigue_in = input('¿Quieres seguir jugando? [S/N] ').upper()
			if sigue_in == 'S':
				sigue = True
				break

			elif sigue_in == 'N':
				sigue = False
				break

			else:
				sigue = False
				continue

		except:
			print('Error al identificar texto, intentalo de nuevo')
			sigue = False
			continue

	return sigue


if __name__ == '__main__':
	sigue_jugando = True

	while sigue_jugando:
		
		nuevo_numero = introducir_numero()
		
		clase_numero = Numero(nuevo_numero)
		clase_numero.obtener_descomposicion_numero()

		sigue_jugando = seguir_jugando()
