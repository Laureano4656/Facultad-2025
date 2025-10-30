package Ejercicio1;

public class MonitorCaso3 implements IMonitor {
    private int trenesEnVia = 0;
    private int direccionActualEnVia = 0; // 0: libre, 1: de tramo1, 2: de tramo2

    public synchronized void entrar(int direccion) {
        // Un tren espera si la vía está ocupada por trenes que van en sentido CONTRARIO.
        while (trenesEnVia > 0 && direccionActualEnVia != direccion) {
            try {
                System.out.println(Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ESPERANDO. Vía usada en sentido contrario.");
                wait();
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }

        System.out.println("=> " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ENTRA a la vía.");
        trenesEnVia++;
        direccionActualEnVia = direccion;
        notifyAll();
    }

    public synchronized void salir(int direccion) {
        System.out.println("<= " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") SALE de la vía.");
        trenesEnVia--;

        // Si es el ÚLTIMO tren en salir, la vía queda libre para CUALQUIER dirección.
        if (trenesEnVia == 0) {
            System.out.println("--- La vía central ha quedado LIBRE ---");
            direccionActualEnVia = 0;
            notifyAll(); // Notificamos a todos para que los de la otra dirección puedan intentar pasar.
        }
    }
}