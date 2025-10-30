package Ejercicio4;

public class Mesa
{
    private Baraja baraja;
    private int cantJugadores;
    private int turno = 0;
    private int[] puntajesMano;
    private int jugadoresYaJugaron = 0;
    private final Jugador[] jugadores;
    private boolean juegoTerminado = false;
    private int numeroMano = 0;
    public Mesa(Baraja baraja, Jugador[] jugadores)
    {
        this.baraja = baraja;
        this.jugadores = jugadores;
        this.cantJugadores = jugadores.length;
        this.puntajesMano = new int[cantJugadores];
    }

    private void evaularGanador(){
        int maxPuntaje = 0;
        int ganador = -1;
        for (int i = 0; i < cantJugadores; i++) {
            if (puntajesMano[i] > maxPuntaje) {
                maxPuntaje = puntajesMano[i];
                ganador = i;
            } else if (puntajesMano[i] == maxPuntaje && maxPuntaje != 0) {
                ganador = -1; // Empate
            }
        }
        if (ganador != -1) {
            this.jugadores[ganador].incrementarManosGanadas();
            System.out.println(">> El ganador de la mano es el Jugador " + ganador + " con un puntaje de " + maxPuntaje + ".");
        } else {
            System.out.println(">> No hay ganador en esta mano.");
        }
    }
    public synchronized void jugarMano(int nroJugador) throws InterruptedException
    {
        System.out.println(">> Jugador " + nroJugador + " intenta tomar cartas.");
        while (turno != nroJugador && !juegoTerminado)
        {
            System.out.println(">> No es el turno del jugador " + nroJugador + ". Esperando...");
            wait();
        }
        if (baraja.cantidadCartas() < this.cantJugadores) {
            this.juegoTerminado = true;
            notifyAll(); // Despierta a todos para que salgan de su bucle
            return;
        }
        int puntajeActual = 0;
        System.out.println(">> Es el turno de " + nroJugador );

        while (puntajeActual < 16){
            int carta = baraja.tomarCarta();
            if (carta == 0) {
                System.out.println(">> No hay más cartas en la baraja.");
                break;
            }
            puntajeActual += carta;
            System.out.println(">> Jugador " + nroJugador + " tomó una carta de valor " + carta + ". Puntaje actual: " + puntajeActual);
        }
        puntajesMano[nroJugador] = (puntajeActual > 21) ? 0 : puntajeActual;
        System.out.println(">> Jugador " + nroJugador + " terminó su turno con un puntaje de " + puntajesMano[nroJugador] + ".");
        turno = (turno + 1) % cantJugadores;
        notifyAll();
    }


    public synchronized void esperarYaJugaron() throws InterruptedException
    {
        jugadoresYaJugaron++;
        int miMano = this.numeroMano;
        System.out.println(">> Jugadores que ya jugaron: " + jugadoresYaJugaron + "/" + cantJugadores);
        if (jugadoresYaJugaron == cantJugadores) {
            System.out.println("Fin de la mano");
            evaularGanador();
            this.puntajesMano = new int[cantJugadores];
            this.jugadoresYaJugaron = 0;
            this.turno = 0;
            this.numeroMano++;
            notifyAll();
        } else {

            while (this.numeroMano == miMano && !juegoTerminado) {
                wait();
            }

        }
    }
    public boolean isJuegoTerminado()
    {
        return juegoTerminado;
    }
}
