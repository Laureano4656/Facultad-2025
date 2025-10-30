package Ejercicio1;

import Ejercicio1.IMonitor;

public class MonitorCaso4 implements IMonitor
{


    public synchronized void entrar(int direccion) {
        via.agregarTrenEnEspera(direccion);
        // La condición de espera es la más estricta:
        // 1. Si hay trenes circulando en sentido contrario.
        // 2. Si YO quiero entrar por el tramo 1, pero hay gente esperando en el tramo 2 (¡ellos tienen prioridad!)
        // 3. Si YO quiero entrar por el tramo 2, pero hay gente esperando en el tramo 1.
        while ((via.getTrenesEnVia() > 0 && via.getDireccionActualEnVia() != direccion) ||
                (via.getTrenesEnVia() == 0 && via.getTurno() != direccion && via.hayAlguienEsperandoEn(via.getTurno()))) {
            try {
                System.out.println(Thread.currentThread().getName() + " (TRAMO " + direccion + ") ESPERANDO...");
                wait();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        via.quitarTrenDeEspera(direccion);
        via.registrarTrenEntrando(direccion);
        System.out.println("=> " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") ENTRA a la vía.");



    }

    public synchronized void salir(int direccion) {
        System.out.println("<= " + Thread.currentThread().getName() + " (desde TRAMO " + direccion + ") SALE de la vía.");
        via.registrarTrenSaliendo(direccion);

        if (via.getTrenesEnVia() == 0) {
            System.out.println("--- La vía central ha quedado LIBRE ---");

        }
        notifyAll(); // Despertar a todos para que compitan bajo las nuevas condiciones (vía libre).
    }
}