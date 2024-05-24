from pytube import YouTube


dire=str('D:\DEVELOPMENT\PythonDownloader\pasta')
Link = str('a')
def diretorio():
    global dire
    print("Digite Cuidadosamente o novo diretorio.\n Minhas habilidades não te prtoegerão.")
    dire=input("Novo Diretorio: ")
    print("Definir '",dire,"' como novo diretorio?(S/N)")
    resposta=input()
    if resposta==('S'):
        print("Diretorio alterado com sucesso")
        MainMenu()
    elif resposta == ('N'):
        print("mantendo diretorio padrão:",dire)
        MainMenu()
    else:
        MainMenu()
def GetInfo():
    global Link
    Link =str(input("\nInsira Link YouTube: "))
    Info_Down()

def Info_Down():
    global Link
    if Link==('C'):
        MainMenu()
    elif YouTube(Link).age_restricted:
        print("Video com Restrição de idade.\n")
        MainMenu()
    else:
        print("Não Restrito, Aguarde...\n")
    Lenght = round((YouTube(Link).length)/60 , 2)
    Title = (YouTube(Link).title)
    resolution = (YouTube(Link).streams.get_highest_resolution().resolution)
    Fps = (YouTube(Link).streams.get_highest_resolution().fps)
    Size = (YouTube(Link).streams.get_highest_resolution().filesize_mb)
    unity = str("Mb")
    if Size >= 1000:
        tamanho=round(Size/1024, 2)
        unity = str("Gb")
        Size = tamanho
    print("Titulo: {Titulo}, Duração: {Duracao},\nResolução: {Resolucao}, FPS: {fps}, Tamanho: {Tamanho}{Unidade}"
          .format(Titulo=Title, Duracao=Lenght,Resolucao=resolution, fps=Fps,Tamanho=Size,Unidade=unity))
    res = input("Deseja Baixar o Video?(S/N/C) ")
    if res==('S'):
        print("Baixando, Aguarde...\n")
        Download()
    elif res == ('N'):
        GetInfo()
    elif res == ('C'):
        MainMenu
    else:
        print("entrada Invalida\n")
        MainMenu()
    MainMenu()
    
def Download():
    global Link , dire
    video= YouTube(Link)
    video= video.streams.get_highest_resolution()
    try:
        video.download(output_path=dire)
    except:
        print("ocorreu um erro no download\n")
        MainMenu()
    
def MainMenu():
    
    print("\nArmazenamento padrão: ", dire)
    res=str(input("\n\n1.Download\n2.Mudar Diretorio\n3.sair\n\n"))
    if res == ('1'):
        GetInfo()
    elif res== ('2'):
        diretorio()
    elif res == ('3'):
        quit()
MainMenu()