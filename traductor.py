#!/usr/bin/env python
# coding=UTF-8

# traductor v1.0
# Utilidad de línea de comandos para traducir frases del castellano al inglés
# Copyright (C) 2012, opensas, opensas@gmail.com
# Código disponible en https://github.com/opensas/floss-demo

# traductor_lib v3.5
# Librería para utilizar el servicio web de http://mymemory.translated.net
# Copyright (C) 2010, 2011, 2012, Sebastián Scarano, @develsas
# Código disponible en https://github.com/traductor-play/traductor_lib

# traductor es software libre: usted puede redistribuirlo y/o modificarlo 
# bajo los términos de la Licencia Pública General GNU publicada 
# por la Fundación para el Software Libre, ya sea la versión 3 
# de la Licencia, o (a su elección) cualquier versión posterior.

# Este programa se distribuye con la esperanza de que sea útil, pero 
# SIN GARANTÍA ALGUNA; ni siquiera la garantía implícita 
# MERCANTIL o de APTITUD PARA UN PROPÓSITO DETERMINADO. 
# Consulte los detalles de la Licencia Pública General GNU para obtener 
# una información más detallada. 

# Debería haber recibido una copia de la Licencia Pública General GNU 
# junto a este programa. 
# En caso contrario, consulte <http://www.gnu.org/licenses/>.

# floss-demo
# ==========
# 
# Script de ejemplo para explicar los principios del software librerías
# 
# Utilidad de línea de comandos para traducir 
# una frase del castellano al idioma inglés
# 
# versión 1.0
# 

# declaramos librerías a utilizar
from traductor_lib import traducir

# funciones varias
# 

# leemos los parámetros de la línea de comandos
def leer_parametros():
  from argparse import ArgumentParser
  parser = ArgumentParser(description='Permite traducir una frase del castellano al inglés.')
  parser.add_argument('frase', metavar='frase', help='frase a traducir (entre comillas)')
  args = parser.parse_args()
  return args.frase

# programa principal
# 

# leemos la frase que el usuario ingresó desde la línea de comandos
frase = leer_parametros()

# traducimos la frase
frase_traducida = traducir("es", "en", frase)

# imprimimos la frase traducida
print frase_traducida
