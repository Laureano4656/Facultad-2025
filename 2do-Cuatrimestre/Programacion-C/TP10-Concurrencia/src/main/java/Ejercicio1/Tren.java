package Ejercicio1;

public class Tren implements Runnable
{

    private final int miDireccion;
    private final IMonitor monitor;

    public Tren( int miDireccion, IMonitor monitor)
    {
        this.miDireccion = miDireccion;
        this.monitor = monitor;
    }

    @Override
    public void run() {
        try {
            System.out.println(Thread.currentThread().getName() + " llega para entrar por TRAMO " + miDireccion);

            // El tren intenta entrar por su tramo/dirección asignada
            monitor.entrar(miDireccion);

            // Simula el tiempo en la vía
            System.out.println(">> " + Thread.currentThread().getName() + " está circulando por la vía central...");
            Thread.sleep((long) (Math.random() * 2000));

            // El tren sale de la vía
            monitor.salir(miDireccion);

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
