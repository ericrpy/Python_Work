import pyautogui as py


try:
    img1 = py.locateCenterOnScreen('8.png')
    
    if img1 is not None:  # Verifica se a imagem foi encontrada
        py.click(img1)
    else:
        raise py.ImageNotFoundException()  # Lança a exceção se não encontrado

except py.ImageNotFoundException:
    print('Imagem não encontrada')

