package Ejercicio4;

public class Jugador implements Runnable
{
    private int nro;
    private Mesa mesa;
    private int sumaCartas;
    private int manosGanadas = 0;
    public Jugador(int nro, Mesa mesa)
    {
        this.nro = nro;
        this.mesa = mesa;
    }
    @Override
    public void run() {
        try {
            while (!mesa.isJuegoTerminado()) {
                // El jugador intenta tomar cartas de la mesa
                mesa.jugarMano(nro);

                // Simula el tiempo jugando con las cartas
                mesa.esperarYaJugaron();

            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    public void incrementarManosGanadas() {
        this.manosGanadas++;
    }

    public int getManosGanadas()
    {
        return manosGanadas;
    }
    public int getId()
    {
        return nro;
    }
}
