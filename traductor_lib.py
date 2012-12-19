#!/usr/bin/env python
# coding=UTF-8

# traductor_lib v3.5
# Librería para utilizar el servicio web de http://mymemory.translated.net
# Copyright (C) 2010, 2011, 2012, Sebastián Scarano, @develsas

# traductor_lib es software libre: usted puede redistribuirlo y/o modificarlo 
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
# Script de ejemplo para explicar los principios del software libre
# 
# Librería para utilizar el servicio web de http://mymemory.translated.net
# para traducir frases de un idioma al otro
# 
# Actualmente el uso gratuito de esta herramienta se 
# encuentra limitado a 2.000 traducciones por día
# 
# Más información acerca del servicio web en:
# http://mymemory.translated.net/doc/spec.php
# 
# Ejemplo de uso:
# 
# http://mymemory.translated.net/api/get?q=Hola amigos&langpair=es|en
# 

# declaramos librerías a utilizar
import httplib2, urllib, json

# función traducir: Traduce el texto ingresado de un idioma a otro
# 
# Parámetros:
#   idioma_fuente:  idioma del texto a traducir. Ej: es
#   idioma_destino: idioma al cual se quiere traducir el texto. Ej: en
#   texto:          texto a traducir
# 
# Retorna:
#   el texto traducido, o un mensaje de error si no pudo utilizar el servicio web

def traducir(idioma_fuente, idioma_destino, texto):

  url_base = "http://mymemory.translated.net/api/get?"

  # formateamos los idiomas de entrada y salida para agregar al url
  idiomas = idioma_fuente + "|" + idioma_destino
  parametros = urllib.urlencode({'q': texto, 'langpair': idiomas})

  # armamos el url completo
  url = url_base + parametros

  try:

    setencoding()

    # intentamos acceder al servicio web de traducción
    respuesta, contenido = httplib2.Http().request(url)

    # verificamos si hubo un error
    if respuesta.status != 200:
      return "error accessing web service"

    # decodificamos la información devuelta en formato json
    json_data = json.loads(contenido)

    # extraemos el texto traducido y lo retornamos
    return str(json_data["responseData"]["translatedText"])

  except:
    return "error al traducir el texto"

def setencoding():
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")
