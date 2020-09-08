# Importacion Librerias
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(15, GPIO.OUT)

# Clase
class bombaDeAgua:

# Declarar funciones  
  def menu(self):
    print(" SISTEMA DE RIEGO ")
    print(" PIN 3) Deposito de Agua (Marcado=Vacio) (Desmarcado=Lleno) ")
    print(" PIN 5) Epoca Verano (Marcado=Verano) (Desmarcado=Restante del año) ")
    print(" PIN 7) Dia/Noche (Marcado=Dia) (Desmarcado=Noche) ")
    print(" PIN 8) Tierra (Marcado=Seca) (Desmarcado=Humeda) ")
    print("\nSelecciones un pin:")
    def leer(self,mensaje):
        print(mensaje)
    men1=float(input())
    return men1
  
  def estadosCircuito(self):
        V = GPIO.input(3) # Deposito de agua
        S = GPIO.input(8) # Tipo de Tierra
        D = GPIO.input(7) # Dia/Noche
        R = GPIO.input(5) # Restricciones, verano.
        
        if (V == GPIO.HIGH): # Deposito de agua vacio
            GPIO.output(15, GPIO.LOW)
            print("No podra trabajar la bomba de agua, ya que su deposito de agua esta vacio")
            time.sleep(0.3)
        elif (V == GPIO.LOW and R == GPIO.HIGH and D == GPIO.LOW):
            GPIO.output(15, GPIO.HIGH)
            print("Bomba encendida")
            time.sleep(0.3)
        elif ((V == GPIO.LOW and R == GPIO.LOW and S == GPIO.HIGH and D == GPIO.HIGH) or (V == GPIO.LOW and R == GPIO.LOW and S == GPIO.HIGH and D == GPIO.LOW)):
            GPIO.output(15, GPIO.HIGH)
            print("Bomba encendida")
            time.sleep(0.3)
        else:
            GPIO.output(15, GPIO.LOW)
            print("No selecciono ninguna opcion valida")
            time.sleep(0.3)

            GPIO.cleanup()

# Instanciar / Crear nuevo objeto / Llamar
b = bombaDeAgua()
b.menu()
b.estadosCircuito()
