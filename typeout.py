
# PyGame possui uma entrada de dados que fornece uma melhor experiência para a jogabilidade
import pygame, random, time, sys # Por esse motivo foi utilizado para capturar as teclas digitadas pelo jogador


class bcolors: # Cores para as frases. Funciona em terminais Linux.
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node: # Nó utilizado para guardar uma palavra
    def __init__(self,key,n): 
        self.left = None
        self.right = None
        self.val = key
        self.name = n


def search(root,key): # Procura na árvore
    if root is None or root.val == key: 
        return root 
    if root.val < key: 
        return search(root.right,key)  
    return search(root.left,key)


def insert(root,node): # Insere na árvore
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

pygame.init() # Inicia o PyGame
windowSurface = pygame.display.set_mode((1, 1), pygame.NOFRAME) # Cria a janela para captura de entrada

# Variaveis do jogo
nivelDeDificuldade=[25,35,45] # Quanto maior a dificuldade, mais o tempo da polícia é multiplicado
dificuldadeDasPalavras=[0,1,0] # Ativa aleatório ou não
dificuldadeSelecionada=1; # Variável usada para guardar a seleção
random.seed(time.time())
handicap=200 # Distancia da policia ganhada no início da partida

contaTecla=0; # Quantas teclas foram apertadas
letrasCorretas=0; # Contador p/ a comparação de palavras
fator=125; # O fator começa em 125
           # A cada palavra certa, ele diminui em 1
           # Quanto menor o número, mais rápido as palavras obrigatórias aparecem

# Carregamento de texto
caminhoArquivo = open("arquivo.txt", "r");
arquivoAberto = caminhoArquivo.read();

palavra=""
palavraEscrita=""
on=True
policiaPerseguindo=False
iniciadoJogo=False

# Armazena todas as palavras do arquivo em uma árvore binária
r = Node(0,None)
palavr= ""
posicao = 0
notFirstPass = False
for x in range (len(arquivoAberto)):

    if ( not(arquivoAberto[x].isalpha()) ) :
        x+=1
        
        if x < len(arquivoAberto) and arquivoAberto[x].isalpha():
            posicao = x
            
            while(x < len(arquivoAberto) and arquivoAberto[x].isalpha()):
                palavr += arquivoAberto[x]
                x+=1
                
            if len(palavr) > 1:
                
                if notFirstPass:
                    insert(r,Node(posicao,palavr))
                    
                else:
                    r = Node(posicao,palavr)
                    notFirstPass = True;     
            palavr = ""


# Menu inicial
print(r"""
                             __xxxxxxxxxxxxxxxx___.
                        _gxXXXXXXXXXXXXXXXXXXXXXXXX!x_
                   __x!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!x_
                ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx_
              ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!_
            _!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
          gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs
        ,!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
       g!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
      iXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
     ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
     !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
   !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi
  dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXf~~~VXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvvvvXXXXXXXXXXXXXX!
   !XXXXXXXXXXXXXXXf`       'XXXXXXXXXXXXXXXXXXXXXf`          '~XXXXXXXXXXP
    vXXXXXXXXXXXX!            !XXXXXXXXXXXXXXXXXX!              !XXXXXXXXX
     XXXXXXXXXXv`              'VXXXXXXXXXXXXXXX                !XXXXXXXX!
     !XXXXXXXXX.                 YXXXXXXXXXXXXX!                XXXXXXXXX
      XXXXXXXXX!                 ,XXXXXXXXXXXXXX                VXXXXXXX!
      'XXXXXXXX!                ,!XXXX ~~XXXXXXX               iXXXXXX~
       'XXXXXXXX               ,XXXXXX   XXXXXXXX!             xXXXXXX!
        !XXXXXXX!xxxxxxs______xXXXXXXX   'YXXXXXX!          ,xXXXXXXXX
         YXXXXXXXXXXXXXXXXXXXXXXXXXXX`    VXXXXXXX!s. __gxx!XXXXXXXXXP
          XXXXXXXXXXXXXXXXXXXXXXXXXX!      'XXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXP        'YXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXX!     i    !XXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXX!     XX   !XXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXx_   iXX_,_dXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXP
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
           ~vXvvvvXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                    'VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvv~
                      'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX~
                  _    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                 -XX!  !XXXXXXX~XXXXXXXXXXXXXXXXXXXXXX~   Xxi
                  YXX  '~ XXXXX XXXXXXXXXXXXXXXXXXXX`     iXX`
                  !XX!    !XXX` XXXXXXXXXXXXXXXXXXXX      !XX
                  !XXX    '~Vf  YXXXXXXXXXXXXXP YXXX     !XXX
                  !XXX  ,_      !XXP YXXXfXXXX!  XXX     XXXV
                  !XXX !XX           'XXP 'YXX!       ,.!XXX!
                  !XXXi!XP  XX.                  ,_  !XXXXXX!
                  iXXXx X!  XX! !Xx.  ,.     xs.,XXi !XXXXXXf
                   XXXXXXXXXXXXXXXXX! _!XXx  dXXXXXXX.iXXXXXX
                   VXXXXXXXXXXXXXXXXXXXXXXXxxXXXXXXXXXXXXXXX!
                   YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXV
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
                    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                       VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                         VXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                          ~vXXXXXXXXXXXXXXXXXXXXXXXf`
                              ~vXXXXXXXXXXXXXXXXv~
                                 '~VvXXXXXXXV~~
                                       ~~
TTTTTTTTTTTTTTTTTTTTTTT        YYYYYYY       YYYYYYY        PPPPPPPPPPPPPPPPP           EEEEEEEEEEEEEEEEEEEEEE
T:::::::::::::::::::::T        Y:::::Y       Y:::::Y        P::::::::::::::::P          E::::::::::::::::::::E
T:::::::::::::::::::::T        Y:::::Y       Y:::::Y        P::::::PPPPPP:::::P         E::::::::::::::::::::E
T:::::TT:::::::TT:::::T        Y::::::Y     Y::::::Y        PP:::::P     P:::::P        EE::::::EEEEEEEEE::::E
TTTTTT  T:::::T  TTTTTT        YYY:::::Y   Y:::::YYY          P::::P     P:::::P          E:::::E       EEEEEE
        T:::::T                   Y:::::Y Y:::::Y             P::::P     P:::::P          E:::::E
        T:::::T                    Y:::::Y:::::Y              P::::PPPPPP:::::P           E::::::EEEEEEEEEE
        T:::::T                     Y:::::::::Y               P:::::::::::::PP            E:::::::::::::::E
        T:::::T                      Y:::::::Y                P::::PPPPPPPPP              E:::::::::::::::E
        T:::::T                       Y:::::Y                 P::::P                      E::::::EEEEEEEEEE
        T:::::T                       Y:::::Y                 P::::P                      E:::::E
        T:::::T                       Y:::::Y                 P::::P                      E:::::E       EEEEEE
      TT:::::::TT                     Y:::::Y               PP::::::PP                  EE::::::EEEEEEEE:::::E
      T:::::::::T       ......     YYYY:::::YYYY     ...... P::::::::P           ...... E::::::::::::::::::::E ......
      T:::::::::T       .::::.     Y:::::::::::Y     .::::. P::::::::P           .::::. E::::::::::::::::::::E .::::.
      TTTTTTTTTTT       ......     YYYYYYYYYYYYY     ...... PPPPPPPPPP           ...... EEEEEEEEEEEEEEEEEEEEEE ......


                                            Made by Pablo Lodi
""")
print("PRESS S TO START")
print()
print("PRESS E FOR EASY")
print("PRESS N FOR NORMAL")
print("PRESS H FOR HACKER")
print()
print("PRESS Q TO QUIT")

while True:

    if iniciadoJogo:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        
        if seconds*nivelDeDificuldade[dificuldadeSelecionada] >= (contaTecla + handicap) and policiaPerseguindo: # if more than x seconds close the game
            print(bcolors.FAIL+r"""
                           _
      .::::::::::.        -(_)====u         .::::::::::.
    .::::''''''::::.                      .::::''''''::::.
  .:::'          `::::....          ....::::'          `:::.
 .::'             `:::::::|        |:::::::'             `::.
.::|               |::::::|_ ___ __|::::::|               |::.
`--'               |::::::|_()__()_|::::::|               `--'
 :::               |::-o::|        |::o-::|               :::
 `::.             .|::::::|        |::::::|.             .::'
  `:::.          .::\-----'        `-----/::.          .:::'
    `::::......::::'                      `::::......::::'
      `::::::::::'                          `::::::::::'

            """+bcolors.ENDC)
            print(bcolors.FAIL+"\n **-**-** WASTED! **-**-** \n"+bcolors.ENDC);
            print("Final points:",contaTecla);
            sys.exit();
        
        for event in pygame.event.get():

            if contaTecla >= len(arquivoAberto):
                print("\nYEAH YEAH, POLICE WILL NEVER GET YOU");
                sys.exit()
                
            if on == True:
                objeto = search(r,contaTecla)
                if objeto != None:
                    palavra = objeto.name
                    
            if event.type in (pygame.KEYDOWN, pygame.KEYUP) and on:
                 print(arquivoAberto[contaTecla],end="",flush=True)
                 contaTecla+=1;
                 
            if on == False:
                
                if event.type == pygame.KEYDOWN:
                    
                    if pygame.key.name(event.key).lower() == palavra[letrasCorretas].lower():
                        print(palavra[letrasCorretas],end="",flush=True)
                        letrasCorretas+=1;
                        
                    if letrasCorretas == len(palavra):
                        print()

                        letrasCorretas=0;
                        contaTecla+=1;
                        
                        if fator > 50:
                            fator-=1;
                            
                        print(bcolors.BOLD + " LATENCY BETWEEN FBI AND YOU: "+ bcolors.ENDC,str( (contaTecla + handicap) - (seconds*nivelDeDificuldade[dificuldadeSelecionada]))+" ms")

                        policiaPerseguindo = True
                        on = True;
                
            if len(palavra) > 0 and contaTecla%random.randint(fator-dificuldadeDasPalavras[dificuldadeSelecionada], fator)==0 and on == True:
                print("\n"+bcolors.HEADER + " " + palavra + " " + bcolors.ENDC);
                on=False;
                
    else:
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if pygame.key.name(event.key) == "s":
                    
                    print(r"""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
                """)
                    
                    print("STARTING HACKING SESSION...");
                    
                    print("HACKOS v0.00 - NO COPYRIGHTS")
                    
                    print("SESSION READY. START TYPING.")
                    
                                                        # "Ativa a polícia" - No caso, começa a contar os 
                    start_ticks=pygame.time.get_ticks() # segundos que vão ser multiplicados pela dificuldade
                                                        # escolhida, tentando assim vencer o jogador.
                                                        
                    print(bcolors.WARNING+"\n WARNING: FBI IS TRYING TO TRACK YOUR LOCATION. "+bcolors.ENDC)
                    
                    print(bcolors.WARNING+" IT'S BETTER FOR YOU TO START TYPING. RIGHT NOW. \n"+bcolors.ENDC)
                    
                    iniciadoJogo = True;
                    
                elif pygame.key.name(event.key) == "e":
                    dificuldadeSelecionada = 0;
                    print("\nEASY SELECTED")
                    
                elif pygame.key.name(event.key) == "n":
                    dificuldadeSelecionada = 1;
                    print("\nNORMAL SELECTED")
                    
                elif pygame.key.name(event.key) == "h":
                    dificuldadeSelecionada = 2;
                    print("\nHACKER MODE")
                    
                elif pygame.key.name(event.key) == "q":
                    pygame.quit()
