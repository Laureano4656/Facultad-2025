package Ejercicio1;

public class MonitorCaso2 implements IMonitor {
    private boolean viaOcupada = false;
    private int esperandoTramo1 = 0;
    private int esperandoTramo2 = 0;

    // Para dar prioridad, necesitamos saber quién fue el último en pasar.
    private int ultimoTramoUsado = 0; // 0: ninguno, 1 o 2

    public synchronized void entrar(int direccion) {
        if (direccion == 1) esperandoTramo1++; else esperandoTramo2++;

        // La condición para esperar es más compleja:
        // 1. Si la vía ya está ocupada.
        // 2. Si hay trenes esperando en el lado opuesto y el último tren que pasó iba en MI MISMA dirección (para ceder el paso).
        while (viaOcupada || (direccion == 1 && ultimoTramoUsado == 1 && esperandoTramo2 > 0) || (direccion == 2 && ultimoTramoUsado == 2 && esperandoTramo1 > 0)) {
            try {
                System.out.println(Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ESPERANDO.");
                wait();
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }

        if (direccion == 1) esperandoTramo1--; else esperandoTramo2--;

        System.out.println("=> " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ENTRA a la vía.");
        viaOcupada = true;
        ultimoTramoUsado = 0; // Se resetea para que no afecte al siguiente que salga.
        notifyAll();
    }

    public synchronized void salir(int direccion) {
        System.out.println("<= " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") SALE de la vía.");
        viaOcupada = false;
        ultimoTramoUsado = direccion; // Registramos qué dirección acaba de usar la vía.
        notifyAll(); // Despertamos a todos para que re-evalúen las condiciones.
    }
}
