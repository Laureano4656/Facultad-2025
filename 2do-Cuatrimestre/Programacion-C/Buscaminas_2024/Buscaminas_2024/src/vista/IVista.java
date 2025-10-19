package vista;

import java.awt.event.ActionListener;

import modelo.IBuscaminas;

public interface IVista
{
    int getAncho();

    int getAlto();

    int getCantidad();

    void setActionListener(ActionListener actionListener);

    void iniciarJuego(int alto, int ancho);

    void dibujar(IBuscaminas tablero);

    void dibujarFinal(IBuscaminas tablero);

    void perder();

    void ganar();
}
