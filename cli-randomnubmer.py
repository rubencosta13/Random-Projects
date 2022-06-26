#!/usr/bin/env python3
#computador gerar 1 numero = 73
# utilizador 1o palpite
# Tentativas +1 No caso de estar certo ou errado
# Se estiver certo, o programa acaba com uma tentativa
# Caso nao estiver certo vai continuar ate a 3a tentativa ou ate o utilizador acertar
import random
import time
random.seed(time.time())
print(random.randint(0,100000))

