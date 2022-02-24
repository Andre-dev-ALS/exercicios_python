from pygame import *

a = ''

escolha = int(input('Escolha uma música de 1 a 4'))

if escolha == 1:
    a = 'm1.mp3'
elif escolha == 2:
    a = 'm2.mp3'
elif escolha == 3:
    a = 'm3.mp3'
elif escolha == 4:
    a = 'm4.mp3'
else:
    print('você digitou algo errado, lembre-se que tem que ser um numero de 1 a 4')

mixer.init()

mixer.music.load(a)
nota = int(input('digite um para dar player na música   '))
if nota == 1:
    mixer.music.play()

pause = int(input('Digite 1 para pausar e 2 para dar play'))

while pause!= 3:
    pause = int(input('Digite 1 para pausar e 2 para dar play'))
    if pause == 1:
        mixer.music.pause()
    elif pause == 2:
        mixer.music.unpa    use()