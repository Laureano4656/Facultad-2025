package main;

import controlador.Controlador;
import vista.VentanaBuscaminas;

public class Main
{

    public static void main(String[] args)
    {
	Controlador controlador=new Controlador();
	controlador.setVista(new VentanaBuscaminas());
    }

}
