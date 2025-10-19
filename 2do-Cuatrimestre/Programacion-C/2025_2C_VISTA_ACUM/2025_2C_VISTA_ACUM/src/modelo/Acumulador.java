package modelo;


public class Acumulador
{
	private int valor = 0;

	public void incrementa(int cantidad)
	{
		this.valor += cantidad;
	}

	
	public void decrementa(int cantidad)
	{
		this.valor -= cantidad;
	}
	public int getValor()
	{
		return valor;
	}

	
	
	
}
