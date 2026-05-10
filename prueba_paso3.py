from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import AsesoriaEspecializada
from servicios.reserva_sala import ReservaSala
from excepciones.excepciones import SistemaFJError

def probar_servicios():
    print("--- Probando tus servicios del Paso 3 ---")
    
    try:
        # 1. Probar Alquiler
        laptop = AlquilerEquipo("ALQ-001", "Laptop Gamer", "Laptop")
        costo_alq = laptop.calcular_costo(dias=5, incluir_seguro=True)
        print(f"Prueba Alquiler: {laptop.describir()} -> Costo por 5 días con seguro: ${costo_alq}")

        # 2. Probar Asesoría
        asesoria = AsesoriaEspecializada("ASE-001", "Asesoría Python", "Programación")
        costo_ase = asesoria.calcular_costo(nivel="Senior", horas=3, es_festivo=True)
        print(f"Prueba Asesoría: {asesoria.describir()} -> Costo Senior 3h festivo: ${costo_ase}")

        # 3. Probar Sala
        sala = ReservaSala("SAL-001", "Sala Creativa", 10)
        costo_sala = sala.calcular_costo(horas=2, incluir_refrigerio=True, personas=5)
        print(f"Prueba Sala: {sala.describir()} -> Costo 2h con refrigerio para 5: ${costo_sala}")

        print("\n✅ ¡Todo funciona correctamente! Revisa el archivo 'eventos.log' que se acaba de crear.")

    except SistemaFJError as e:
        print(f"❌ Error controlado: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    probar_servicios()
