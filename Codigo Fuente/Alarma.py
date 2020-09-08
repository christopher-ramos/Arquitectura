import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

class Alarma:
  i=0
  gass=0
  h=0
  tema=0
  temb=0
  
  def menu(self):
    print("\nIndicaciones")
    print("8) Sensor de gas")
    print("10) Sensor de humo")
    print("12) Temperatura 45")
    print("11) Temperatura 60")
  
  def gas(self):
    gass=0
    if GPIO.input(8) == GPIO.HIGH:
      gass=1
    return gass
  def humo(self):
    h=0
    if GPIO.input(10) == GPIO.HIGH:
      h=1
    return h
  def tem45(self):
    tema=0
    if GPIO.input(12) == GPIO.HIGH:
      tema=1
    return tema
  def tem60(self):
    temb=0
    if GPIO.input(11) == GPIO.HIGH:
      temb=1
    return temb
  def incendio(self,gass,h,tema,temb):
    i = temb + gass*tema + gass*h + tema*h
    return i
  
  def imprimir(self,a):
    print("\n\nSE INENDIA, AUXILIO¡¡")
    print("\n\nApagar Alarma pin 37")
    print("Primero desactive los anteriores pins")
   
  def foco(self):
    while (GPIO.input(37) != GPIO.HIGH):
      GPIO.output(40, True)
      time.sleep(0.5)
      GPIO.output(40, False)
      time.sleep(0.5)
     
t=1    

alam=Alarma()
alam.menu()
while (t!=0):
  gas=alam.gas()
  humo=alam.humo()
  tem45=alam.tem45()
  tem60=alam.tem60()
  si=alam.incendio(gas,humo,tem45,tem60)
  if si >= 1:
    alam.imprimir(si)
    alam.foco()
