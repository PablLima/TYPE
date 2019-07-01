# Usei pygame, pois não consegui imprimir cada letra separadamente com outras abordagens
import pygame, sys
import pygame.locals

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

pygame.init()
WIDTH = 1
HEIGHT = 1
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Variaveis do jogo
nivelDeDificuldade=[10,30,40];
dificuldadeSelecionada=1;
contaTecla=0;
contaLetra=0;
fator=125;
caminhoArquivo = open("arquivo.txt", "r");
arquivoAberto = caminhoArquivo.read();
palavra=""
palavraEscrita=""
on=True
policiaPerseguindo=False
iniciarJogo=False

#windowSurface.fill(BLACK)

def findWord():
    if( not(arquivoAberto[contaTecla].isalpha()) ) :
        word=""
        i=contaTecla+1
        while (True):
            if not(arquivoAberto[i].isalpha()):
                word=arquivoAberto[contaTecla+1:i]
                return word;
            i+=1
    return "";

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
    if iniciarJogo:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds*nivelDeDificuldade[dificuldadeSelecionada]>=contaTecla and policiaPerseguindo: # if more than 10 seconds close the game
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
            print(bcolors.FAIL+"\n ********* WASTED! ********** \n"+bcolors.ENDC);
            print("Final points:",contaTecla);
            break;
        for event in pygame.event.get():
            if findWord() and on == True:
                palavra = findWord()
            if event.type in (pygame.KEYDOWN, pygame.KEYUP) and on:
                 print(arquivoAberto[contaTecla],end="",flush=True)
                 contaTecla+=1;
            if on == False:
                if event.type == pygame.KEYDOWN:
                    if pygame.key.name(event.key).lower() == palavra[contaLetra].lower():
                        print(palavra[contaLetra],end="",flush=True)
                        contaLetra+=1;
                    if contaLetra == len(palavra):
                        print()
                        contaLetra=0;
                        contaTecla+=1;
                        fator-=1;
                        print(bcolors.BOLD + "LATENCY BETWEEN NSA AND YOU:"+ bcolors.ENDC,str(contaTecla-(seconds*30))+" ms")
                        policiaPerseguindo = True
                        on = True;
            if fator < 50:
                fator = 50;
            if len(palavra) > 0 and contaTecla%fator==0 and on == True:
                print("\n"+bcolors.HEADER + palavra + bcolors.ENDC);
                on=False;
            if event.type == pygame.locals.QUIT:
                 pygame.quit()
                 sys.exit()
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
                    start_ticks=pygame.time.get_ticks() #starter tick
                    print(bcolors.WARNING+"\nWARNING: NSA IS TRYING TO TRACK YOUR LOCATION"+bcolors.ENDC)
                    print(bcolors.WARNING+"RUN FOREST, RUN\n"+bcolors.ENDC)
                    iniciarJogo = True;
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
                    sys.exit()
