import time
from time import sleep

unlocking_logo_display = "   .................................\n" \
                         ".?5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5Y!\n" \
                         "5#BBBBBBBBBBBBBBBBBBBBBBBGGGGGBBBGGGGB#!\n" \
                         "P############BBBBBBBB#P?^:::::~?GBBBGG#?\n" \
                         "P########BBBBBBBBBBBB7  !Y5P5J^ .JBGGB#?\n" \
                         "P######BBBBBBBBBBBBB7 .5BBBBBBBJ  JBGB#?\n" \
                         "P###BBBBBBBBBBBBBBB5  7BBBBGGGGB7 :GB##?\n" \
                         "P#BBBBBBBBBBBBBBBBBY::5BBGGGGGGG5:^G###?\n" \
                         "P#BBBG^::::::::::::::::~GGGGGGGBBB#####?\n" \
                         "P#BBBP                 :BBBBB##########?\n" \
                         "P#BBBP       JGP!      :BBBBBBB########?\n" \
                         "P#BBBP       ?#B~      :BBBBBBBBBBBBB##?\n" \
                         "PBBBBP       ^#B:      :BBBBBBBBBBBBBB#?\n" \
                         "PBBBB5       !P5~      :GBBBBBBBBBBBBB#?\n" \
                         "PBBBBP:                ~GGGGBBBBBBBBBB#?\n" \
                         "PBBBBBP?!~~~~~~~~~^~~!?PGGGGGGGBBBBBBB#?\n" \
                         "PBBBGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGBBBB#7\n" \
                         " PYGBBBGGGGGGGGGGGGGGGGGGGGGGGGGBBBB#!\n" \
                         "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


modified_logo = unlocking_logo_display.split("\n")

for i in modified_logo:
    print(str(i))
    time.sleep(0.23)
