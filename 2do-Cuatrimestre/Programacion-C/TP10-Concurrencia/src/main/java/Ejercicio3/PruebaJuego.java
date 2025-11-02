package Ejercicio4;

public class PruebaJuego {
    public static void main(String[] args) {
        int NUM_JUGADORES = 4;

        Baraja baraja = new Baraja();
        Jugador[] jugadores = new Jugador[NUM_JUGADORES];
        Mesa mesa = new Mesa( baraja, jugadores);
        Thread[] hilosJugadores = new Thread[NUM_JUGADORES];

        System.out.println("--- INICIANDO JUEGO DE CARTAS CON " + NUM_JUGADORES + " JUGADORES ---");

        for (int i = 0; i < NUM_JUGADORES; i++) {
            jugadores[i] = new Jugador(i, mesa);
            hilosJugadores[i] = new Thread(jugadores[i], "Jugador-" + i);
            hilosJugadores[i].start();
        }

        // Esperar a que todos los hilos terminen
        for (Thread hilo : hilosJugadores) {
            try {
                hilo.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        System.out.println("\n--- JUEGO TERMINADO ---");
        // Determinar el ganador final
        int maxManos = -1;
        String ganadores = "";
        for(Jugador j : jugadores) {
            if (j.getManosGanadas() > maxManos) {
                maxManos = j.getManosGanadas();
                ganadores = "Jugador " + j.getId();
            } else if (j.getManosGanadas() == maxManos) {
                ganadores += " y Jugador " + j.getId();
            }
        }
        System.out.println("🏆 EL GANADOR FINAL ES: " + ganadores + " con " + maxManos + " manos ganadas! 🏆");
    }
}
