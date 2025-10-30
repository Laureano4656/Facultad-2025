package Ejercicio1;

public class MonitorCaso1 implements IMonitor {
    private boolean viaOcupada = false;

    @Override
    public synchronized void entrar(int direccion) { // El parámetro está para mantener la firma
        while (viaOcupada) {
            try {
                System.out.println(Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ESPERANDO. Vía ocupada.");
                wait();
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }
        System.out.println("=> " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ENTRA a la vía.");
        this.viaOcupada = true;

    }
    @Override
    public synchronized void salir(int direccion) {
        System.out.println("<= " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") SALE de la vía.");
        this.viaOcupada = false;
        notifyAll(); // Despierta a TODOS los que esperan, el primero que llegue, entra.
    }
}
