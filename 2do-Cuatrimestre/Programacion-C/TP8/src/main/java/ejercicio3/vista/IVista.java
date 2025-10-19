package ejercicio3.vista;

import ejercicio3.modelo.IMemoTest;

public interface IVista
{
    int getAncho();

    int getAlto();

    void iniciarJuego(int alto, int ancho);

    void dibujar(IMemoTest tablero);


}
