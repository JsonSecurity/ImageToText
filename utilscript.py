#!/usr/bin/env python3

from time import sleep as sleep
import os

R = '\033[31;1m'  # Rojo
G = '\033[32;1m'  # Verde
Y = '\033[33;1m'  # A;1marillo
B = '\033[34;1m'  # Azul
M = '\033[35;1m'  # Magenta
C = '\033[36;1m'  # Cian
W = '\033[37;1m'  # Blanco
N = '\033[30;1m'  # Negro

# Negrita y subrayado
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Fondo
BG_R = '\033[41m'  # Fondo rojo
BG_G = '\033[42m'  # Fondo verde
BG_B = '\033[44m'  # Fondo azul

RESET = '\033[0m'  # Restablecer al estilo normal

_C = G
_B = N
_E = W

_T = f' {_B}[{_C}+{_B}]{_E}'
_A = f' {_B}[{_C}!{_B}]{_E}'
_Q = f' {_B}[{_C}?{_B}]{_E}'
_V = f' {_B}[{_C}*{_B}]{_E}'

_AUTOR = f'\t{_B}[{_C} Json Security{_B} ] {RESET}{_C}'
_GITHUB = f'\t{_B}[{_C} http://github.com/JsonSecurity{_B} ]{RESET}{_C}'
_SCRIPT = f'\t{_B}[{_C} ImageToText {_B} ] {RESET}{_C}'

bb = N
yy = G
banner = f"""{_C}
 
                    {bb}......                     
               .;clodddddddolc;'.               
             .ckkook00000000000Od,              
             'kOc..cO000000000000d.             
             ,k0kook0000000000000x'             
             .:llccllllxO00000000x'{yy} ....        
     {bb}.'clooooooooooooook000000000x'{yy};dxxdo;.     
    {bb}.lOKKKKK000000000000000000000x,{yy}c00KKK0d'    {_AUTOR} 
   {bb}.o0KKKKKK000000000000000000000d,{yy}c00KKKKKo.   
   {bb},OKKKKKK00000000000000000000Ox;{yy},d00KKKKKO,   {_GITHUB} 
   {bb}:0KKKKKK000Oxoolooooooooollc;,{yy};d00KKKKKK0:   
   {bb}:0KKKKK000d;'{yy};:ccclllllllllloxO0000KKKKK0:   {_SCRIPT}
   {bb},OKKKKKK0d'{yy},oxxxkkkkkkkOOOOOO000000KKKKKO,   
   {bb}.o0KKKKK0c'{yy}lxxxxkkkkkkkOOOOOO000000KKKK0l.   
    {bb}.o0KKKK0c'{yy}oxxxxkkkkkkkOOOOOO000000KKKOl.    
    {bb} .;ldddd;'{yy}oxxxxkkkkdllcllllllllooool:.      
         {bb}... {yy}.oxxxxkkkkoccccccccc:.             
             .oxxxxkkkkkkkOOdllxOd'             
             .lxxxxkkkkkkkOk:..cOd'             
              'cdxkkkkkkkkOOxooxd;.             
               ..,;:clllollllc;'.               

    """

tesseract_banner = f"""{bb}
                        .......                         
                     .....    .....                     
                 .....           .....                  
              .....     {yy}........{bb}     .....              
          ......    {yy}.....     .....{bb}     .....           
       .....     {yy}.....     ..     .....{bb}     .....       
      ,:,.      {yy}';'    ..........    .....{bb}     .'.      
     .'......    {yy}....,,..      ..,.      .'{bb},.   .'      
     .'.  {yy}.;{bb}'...     {yy}.....    .....{bb}    ....,,{bb}   .'      
     .'.  {yy}.'{bb}   .....    {yy}.......{bb}     .....{yy}  .'{bb}   .'      {_AUTOR}{bb} 
     .'.  {yy}.'{bb}      .....         ......{yy}     .'{bb}   .'{bb}      
     .'.  {yy}.'    .{bb}    ......  .....{yy}         .'{bb}   .'      
     .'.  {yy}.'   .;...{bb}     .,;,..    {yy}...,,   .'{bb}   .'      {_GITHUB}{bb}
     .'.  {yy}.'   .'  ....{bb}   .,..   {yy}.... .,.  .'{bb}   .'      
     .'.  {yy}.'   .'    .;.{bb}  .,.   {yy}.,    .'.  .'{bb}   .'      {_SCRIPT}{bb}
     .'.  {yy}.'   .,.   .,.{bb}  .,.   {yy}.'   .''   .'{bb}   .'      
     .'.  {yy}.,.    ....';.{bb}  .,.   {yy}.;.....    .,{bb}   .'      
     .'.   {yy}....     .,:.{bb}  .,.   {yy}.:'.    .....{bb}   .'      
      .'.     {yy}.....  .,.{bb}  .,.   {yy}.,   .....{bb}     .'.      
       ......    {yy}....,;.{bb}  .,.   {yy}.;....{bb}     .....        
           .....     {yy}..{bb}   .,.    {yy}..{bb}     .....           
              ......      .,.       .....               
                  .....   .,..   .....                  
                     .....,:,.....                      
                         .',,..                         
                            
"""

def bar(time=2, message='Loading', large=60):
    print('')
    
    large -= len(message)
    iteration = time / 100
    for p in range(101):
        i = int(large * (p / 100))
        barra = '█' * i + '-' * (large - i)
        print(f'\r{_E} {message}:{_B} |{barra}| {_E} {p}%', end='')
        sleep(iteration)
    print('')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")