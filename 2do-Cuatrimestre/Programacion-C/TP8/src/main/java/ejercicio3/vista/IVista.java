package ejercicio3.vista;

import ejercicio3.modelo.IMemoTest;

import java.awt.event.ActionListener;

public interface IVista
{
    int getAncho();

    int getAlto();

    void iniciarJuego(int alto, int ancho);

    void dibujar(IMemoTest tablero);

    void setActionListener(ActionListener actionListener);

}
