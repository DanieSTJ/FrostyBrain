import serial

def obtener_nivel_agua():
    puerto = 'COM9'  
    baud_rate = 9600

    try:
        ser = serial.Serial(puerto, baud_rate, timeout=1)
        ser.flushInput()

        while True:
            if ser.in_waiting > 0:
                linea = ser.readline().decode('utf-8').rstrip()

                if linea.startswith('Nivel de agua'):
                    nivel_agua = int(linea.split(':')[1].strip())
                    return nivel_agua

    except serial.SerialException as e:
        print(f"Error al abrir el puerto serial: {e}")

# Ejemplo de uso
nivel = obtener_nivel_agua()
print(f"Nivel de agua: {nivel}%")
