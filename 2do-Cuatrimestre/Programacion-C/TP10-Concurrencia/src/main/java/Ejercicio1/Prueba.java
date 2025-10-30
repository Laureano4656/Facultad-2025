package Ejercicio1;
import java.util.ArrayList;
import java.util.List;


public class Prueba {

    public static void main(String[] args) {
        // --- Configuración de la Simulación ---
        int TRENES_TRAMO_1 = 5;
        int TRENES_TRAMO_2 = 5;

        System.out.println("--- INICIANDO SIMULACIÓN DE TRENES ---");

        // --- Elige el monitor que quieres probar ---
        // Descomenta la línea del caso que quieras testear.

        // ControlVias control = new ControlViasCaso1();
        // ControlVias control = new ControlViasCaso2();
        // ControlVias control = new ControlViasCaso3();
        IMonitor control = new MonitorCaso4(); // Usando el caso 4 como ejemplo

        // --- Creación de los hilos (trenes) ---
        List<Thread> todosLosTrenes = new ArrayList<>();

        // Crear trenes que vienen del TRAMO 1
        for (int i = 0; i < TRENES_TRAMO_1; i++) {
            Tren trenRunnable = new Tren(1, control); // Dirección 1
            Thread trenThread = new Thread(trenRunnable, "Tren-" + (i + 1) + "-T1");
            todosLosTrenes.add(trenThread);
        }

        // Crear trenes que vienen del TRAMO 2
        for (int i = 0; i < TRENES_TRAMO_2; i++) {
            Tren trenRunnable = new Tren(2, control); // Dirección 2
            Thread trenThread = new Thread(trenRunnable, "Tren-" + (i + 1) + "-T2");
            todosLosTrenes.add(trenThread);
        }

        System.out.println("Iniciando " + todosLosTrenes.size() + " trenes...");

        // --- Poner en marcha todos los trenes ---
        for (Thread t : todosLosTrenes) {
            t.start();
        }

        // --- Esperar a que todos los trenes terminen su recorrido ---
        // Esto es importante para que el programa principal no termine antes que los hilos.


//        System.out.println("--- SIMULACIÓN FINALIZADA ---");
//        System.out.println("Todos los trenes han completado su recorrido.");
    }
}