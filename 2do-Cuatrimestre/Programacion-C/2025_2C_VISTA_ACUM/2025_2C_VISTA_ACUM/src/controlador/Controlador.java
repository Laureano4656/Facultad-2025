package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import modelo.Acumulador;

public class Controlador implements ActionListener
{
	private Acumulador acumulador;
	private IVista vista;

	

	public Controlador(Acumulador acumulador, IVista vista)
	{
		
		this.acumulador = acumulador;
		this.vista = vista;
		this.vista.addActionListener(this);
	}

	
	
	@Override
	public void actionPerformed(ActionEvent e)
	{
		String comando=e.getActionCommand();
		if(comando.equalsIgnoreCase(IVista.INCREMENTA))
			this.incrementa();
		else 
			if(comando.equalsIgnoreCase(IVista.DECREMENTA))
				this.decrementa();
				
		
	}
	
	

	
	


	public IVista getVista()
	{
		return vista;
	}



	public void setVista(IVista vista)
	{
		this.vista = vista;
		this.vista.addActionListener(this);
	}



	public Acumulador getAcumulador()
	{
		return acumulador;
	}



	private void decrementa()
	{
		this.acumulador.decrementa(this.vista.getCantidad());
		this.vista.actualizaValor(this.acumulador.getValor());
		
		
	}

	private void incrementa()
	{
		this.acumulador.incrementa(this.vista.getCantidad());
		this.vista.actualizaValor(this.acumulador.getValor());
		
	}

}
