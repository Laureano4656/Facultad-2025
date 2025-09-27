package ejercicio3;

public class Prueba {
    public static void main(String[] args) {
        Surtidor surtidor = new Surtidor(); // Capacidad máxima de 1000 litros

        try {
            surtidor.cargarCombustible("Gasolina", 500); // Carga válida
            surtidor.cargarCombustible("Diesel", 600);   // Carga inválida: excede capacidad
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        try {
            surtidor.cargarCombustible("Gasolina", -100); // Carga inválida: cantidad negativa
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        try {
            surtidor.cargarCombustible("Agua", 200);      // Carga inválida: tipo de combustible no válido
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
