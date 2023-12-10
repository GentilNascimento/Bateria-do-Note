import pygame    #controlar a reprodução de músicas
import psutil    #para monitorar o status da bateria
import time      #pausas no código.

def play_music():
    pygame.mixer.init() #prepara o áudio
    pygame.mixer.music.load('saxN.mp3')#carrega o arquivo
    pygame.mixer.music.set_volume(1)#defifne volume máximo
    pygame.mixer.music.play()#inicia reprodução

def stop_music():       #define as funções
    pygame.mixer.music.stop()
    

def check_battery():
    return psutil.sensors_battery().power_plugged, psutil.sensors_battery().percent #retorna se a bateria tá plugada e % da bateria

def main():  #função principal inicializa a flag como False
    play_music_flag = False

    while True:  #Enquanto Verdadeiro:
        plugged, percent = check_battery()#retorna o status atual da bateria (conectado à energia e porcentagem).


        if plugged and percent >= 99: #se plugado na força porcentagem da bateria for maior ou igual a 98%:
            if not play_music_flag: #Se 'play_music_flag' for Falso:
                play_music()  # Inicia a reprodução da música e,
                play_music_flag = True#Define 'play_music_flag' como Verdadeiro.
        else:  #senão
            if play_music_flag: #Se 'play_music_flag' for Verdadeiro:
                stop_music() #Para a reprodução da música
                play_music_flag = False  #Define 'play_music_flag' como Falso.

        if not plugged: # Se o notebook não estiver conectado à energia:
            stop_music() #Para a reprodução da música.
            break  # Sai do loop.

        time.sleep(60)  # Verifica a cada 60 segundos

#Execução:se este arquivo for executado diretamente Chama a função principal 'main()' para iniciar o 
# monitoramento da bateria e reprodução da música.
if __name__ == "__main__":  

    main()
