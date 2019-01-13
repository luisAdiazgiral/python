from pyfirmata import Arduino, ArduinoMega
from pyfirmata import util

from flask import Flask
app = Flask (__name__)

from flask import render_template

def setBoard(boardType, port):
  if boardType == 'arduino':
    board = Arduino(port)
  else:
    board = ArduinoMega(port)
  return board
board=setBoard('arduino', '/dev/ttyACM0')
reader = util.Iterator(board)
reader.start()

pin_var = board.get_pin("d:12:o")

pin_var3 = board.get_pin("d:11:o")

pin_var5 = board.get_pin("d:7:o")


@app.route ("/on_12", methods=['GET'])
def route():
  pin_var.write(1)
  return str('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
@app.route ("/off_12", methods=['GET'])
def route2():
  pin_var.write(0)
  return str('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
@app.route ("/on_11", methods=['GET'])
def route3():
  pin_var3.write(1)
  return render_template ('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
@app.route ("/off_11", methods=['GET'])
def route4():
  pin_var3.write(0)
  return str('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
@app.route ("/on_7", methods=['GET'])
def route5():
  pin_var5.write(1)
  return str('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
@app.route ("/off_7", methods=['GET'])
def route6():
  pin_var5.write(0)
  return str('<!DOCTYPE html> <html>  <head>  <title>Ejemplo del uso de formularios - aprenderaprogramar.com</title>  </head> <body>   <form method="get" action="http://192.168.108.193:5000/on_12" id="form1"> <Button type="submit" value="Encendido12" form="form1"  /> Encendido12 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_12" id="form2"> <button type="submit" value="Apagado12" form="form2"/>Apagado12</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_11" id="form3"> <Button type="submit" value="Encendido11" form="form3"  /> Encendido11 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_11" id="form4"> <button type="submit" value="Apagado11" form="form4"/>Apagado11</button> </form>  <form method="get" action="http://192.168.108.193:5000/on_7" id="form5"> <Button type="submit" value="Encendido7" form="form5"  /> Encendido7 </button> </form>  <form method="get" action="http://192.168.108.193:5000/off_7" id="form6"> <button type="submit" value="Apagado7" form="form6"/>Apagado7</button> </form> </body> </html>')
app.run (host='0.0.0.0')
