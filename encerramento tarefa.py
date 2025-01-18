import pyautogui as py
import time

# funções do mouse
py.click(x=919, y=1060) # abrir o chrome
time.sleep(12)
py.click(x=108, y=23) # abrir a aba de tarefas
time.sleep(12)
py.click(x=362, y=420) # fechar aba 1
time.sleep(3)
py.click(x=368, y=461) # fechar aba 2
time.sleep(3)
py.click(x=358, y=578) # abrir a tarefa
time.sleep(10)
py.click(x=682, y=620) # clicar no campo
time.sleep(5)
py.click(x=474, y=689)
time.sleep(2)
py.write("1,01")
py.press("down")
py.write("1,02")
py.press("down")
py.write("1,03")
py.press("down")
py.write("1,04")
py.press("down")
py.write("1,05")
py.press("down")
py.press("backspace")
py.write("1,06")
py.press("down")
py.write("1,01")
py.click(x=1342, y=646) # atribuir a mim
time.sleep(2)
py.click(x=1108, y=470) # barra
time.sleep(2)
py.click(x=1055, y=384) # ...
time.sleep(3)
py.click(x=874, y=633) # toggle all
time.sleep(2)

# Repetição de cliques para baixar a barra
for barra in range(10):
    py.click(x=1108, y=964)
time.sleep(3)
py.click(x=365, y=304)
py.click(x=365, y=406)
py.click(x=365, y=567)
py.click(x=368, y=669)
py.click(x=366, y=833)

for barra in range(15):
    py.click(x=1108, y=964)
time.sleep(3)

py.click(x=367, y=330)
py.click(x=367, y=497)
py.click(x=366, y=597)
py.click(x=368, y=761) # venda credito claro smart
py.click(x=366, y=859)

for barra in range(9):
    py.click(x=1108, y=964)
time.sleep(3)

py.click(x=367, y=692)
#py.click(x=1082, y=463) # barra
#py.click(x=1085, y=459) # barra
py.click(x=1080, y=539) # barra

time.sleep(1)
py.click(x=367, y=412) # estorno credito smart 2
py.click(x=364, y=576) # venda crédito tef
py.click(x=366, y=646) # estorno credito tef

# finalizando chamado
# py.click(x=1285, y=607) # responsável
time.sleep(5)
py.click(x=1191, y=714) # atribuir a mim
time.sleep(7)
py.click(x=1365, y=491) # tipo de problema
time.sleep(3)
py.click(x=1378, y=604) # n/a
time.sleep(2)
py.moveTo(x=362, y=420)
time.sleep(3)
py.click(x=1402, y=419)
py.write('0,3')
time.sleep(2)
py.click(x=1405, y=375) # canais
time.sleep(4)
py.click(x=1374, y=486) # tef
time.sleep(2)
py.click(x=1387, y=427) # pos
time.sleep(2)

#encerrar
py.click(x=1199, y=275)
# py.click(x=1213, y=390)