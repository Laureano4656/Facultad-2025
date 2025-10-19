package ejercicio3;

import ejercicio3.controlador.Controlador;
import ejercicio3.vista.Ventana;

public class Prueba
{
    public static void main(String[] args)
    {
        Controlador controlador = new Controlador();
        controlador.setVista(new Ventana());
    }
}
