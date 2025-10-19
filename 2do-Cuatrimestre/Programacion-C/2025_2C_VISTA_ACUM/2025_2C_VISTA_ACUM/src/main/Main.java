package main;

import controlador.Controlador;
import modelo.Acumulador;
import vista.Ventana;

public class Main
{

	public static void main(String[] args)
	{
		Acumulador acumulador = new Acumulador();
		Ventana v=new Ventana();
		Controlador controlador=new Controlador(acumulador,v);
	}

}
