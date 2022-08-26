from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random
import time

x, y = 825, 750
janela = Window(x, y)
janela.set_title('Race Game')
teclado = Window.get_keyboard()

score = 0
press = False
op = 'menu'

#__Objetos e suas Configs Iniciais______________________:

fundo = GameImage('estradafinal2.png')
fundo_menu = Sprite('game_menu.png')
fnd = Sprite('fundo_cinza.png')
#nuvem = Sprite('nuvem.png')

car1 = Sprite('ambulancia.png')
car3 = Sprite('policia.png')
car4 = Sprite('audi.png')
car2_vir = Sprite('carro1.png')
car4_vir = Sprite('audi1.png')
audi = Sprite('audi.png')
mini_truck = Sprite('mini_truck.png')

gamerOver = Sprite('over.png')
scr = Sprite('score.png')
esc = Sprite('esc.png')
esq = Sprite('esc2.png')
scroll = Sprite('scroll_input.png')
sel_car = Sprite('selec_car.png')

jogar = Sprite('jogar.png')
rank = Sprite('rank.png')
sair = Sprite('sair.png')
al2 = Sprite('cursor.png')

car1.x, car1.y, car3.x, car3.y = 200, y, 450, y
car1y_ini, car3y_ini = car1.y, car3.y
car1x_ini, car3x_ini = car1.x,  car3.x
car1.speed, car3.speed = 380,  220

x_fun, y_fun, x_nuv = 0, -750, 1272
car1.set_total_duration(1000)
car3.set_total_duration(1000)

def Pontuacao(pont, scr, ini):
    elasped = int( time.clock() - ini)

    if int(elasped) % 5 == 0 and int(elasped) > 0:
        pont += 20*janela.delta_time()


    scr.draw()
    scr.set_position(180, 40)
    janela.draw_text(str(int(pont)), 265, 35, 28, (195, 0, 0), 'Press Start 2P')

    print('Segundo: {}  |  Pontuação: {} '.format(elasped, pont))

    return pont
#_________________________GAME_LOOP______________________________:
while True:
    al2.y = 395
    while op == 'menu':

        fundo_menu.draw()
        jogar.draw()
        rank.draw()
        sair.draw()
        scroll.draw()

        jogar.set_position(janela.width / 2.8, 400)
        rank.set_position(janela.width / 2.8, 450)
        sair.set_position(janela.width / 2.8, 500)
        scroll.set_position(620, 680)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_i and al2.y > jogar.y - 5:
                    al2.y -= 50
                elif event.key == K_k and al2.y < sair.y - 5:
                    al2.y += 50

                if event.key == K_SPACE:
                    if al2.y == jogar.y - 5:
                        op = 'selec_carros'
                    elif al2.y == rank.y - 5:
                        pass
                    elif al2.y == sair.y - 5:
                        janela.close()

        al2.draw()
        al2.set_position(jogar.x - 80, al2.y)
        janela.update()

    al2.y = 480
    while op == 'selec_carros':

        fundo_menu.draw()
        esc.draw()
        car2_vir.draw()
        car4_vir.draw()
        sel_car.draw()
        esc.set_position(620, 670)
        sel_car.set_position(janela.width / 2.8 - 150, 350)
        car2_vir.set_position(janela.width / 2.8 , 450)
        car4_vir.set_position(janela.width / 2.8 + 5 , 550)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_i and al2.y > car2_vir.y + 30:
                    al2.y -= 100
                elif event.key == K_k and al2.y < car4_vir.y:
                    al2.y += 100

                if event.key == K_SPACE:
                    if al2.y == 480:
                        car2 = mini_truck
                        op = 'start'
                    elif al2.y == 580:
                        car2 = audi
                        op = 'start'
                if event.key == K_ESCAPE:
                    car2 = mini_truck
                    op = 'menu'

        al2.set_position(jogar.x - 80, al2.y)
        al2.draw()
        janela.update()
    car2.x, car2.speed = 410, 300


    ini = int(time.perf_counter())
    while op == 'start':
        #elasped = int((time.perf_counter() - ini))

    #____Movimento dos carros 1 e 3_______________:
        car1.y -= car1.speed * janela.delta_time()
        car3.y -= car3.speed * janela.delta_time()

        if car1.y + car1.height < 0:
            car1.y = y + 160
            car1.x = random.randint(120, 600)

        if car3.y + car3.height < 0:
            car3.y = y + 100
            car3.x = random.randint(120, 600)

        if abs(car1.x - car3.x) <= 90 and abs(car1.y - car3.y) <= 250:
            if abs(car3.x - 140) <= 90:
                car1.x += random.randint(110,150)* janela.delta_time()
            else:
                car1.x -= random.randint(110,150)* janela.delta_time()
            if abs(car3.x - 600.) <= 90:
                car1.x -= random.randint(110,150)* janela.delta_time()
            else:
                car1.x -+ random.randint(110,150)* janela.delta_time()


    #____Entrada de interface_____________________________:
        if teclado.key_pressed('j'):
            if car2.x > 120:
                car2.x -= car2.speed * janela.delta_time()

        if teclado.key_pressed('l'):
            if car2.x + car2.height < janela.height:
                car2.x += car2.speed * janela.delta_time()


        fundo.draw()
        fundo.set_position(x_fun,y_fun)
        #nuvem.draw()
        #nuvem.set_position(x_nuv,0)
        car1.draw()
        car2.draw()
        car3.draw()
        car1.set_position(car1.x, car1.y)
        car2.set_position(car2.x, janela.height/2 - 160)
        car3.set_position(car3.x, car3.y)

        car1.update()
        car3.update()

    #____SCROLLING Fundo____________________________:
        if y_fun >= 0:
            y_fun = -750
        #if x_nuv <= 0:
            #x_nuv = 1272

        y_fun += 180 * janela.delta_time()
        #x_nuv -= 60* janela.delta_time()

    #___Dificuldade conforme o TEMPO________________________:
        if score % 10 == 0 and score > 20:
            car3.speed += 0
            car1.speed += 0

    #____SCORE__________________________________________________________________:
        score = Pontuacao(score, scr, ini)

    #____COLISÕES_Game_Over_____________________________________________:
        if car2.collided_perfect(car1) or car2.collided_perfect(car3) and janela.delta_time() > 0:
            op = 'endgame'
            score, ini = 0, int(time.perf_counter())

            while op == 'endgame':
                fnd.draw()
                gamerOver.draw()
                esq.draw()
                gamerOver.set_position(janela.width/2-230, janela.height/2 - 50)
                esq.set_position(janela.width/2-120, 550)
                janela.update()

                if teclado.key_pressed('ESC'):
                    press = True
                    if press:
                        car1.speed, car3.speed = 300, 220
                        car1.y, car3.y = car1y_ini, car3y_ini
                        op = 'menu'
                    else:
                        press = False



        janela.update()
