package modelo;

import java.util.Random;

public class Tablero implements IBuscaminas
{
    private Casillero[][] matriz;
    private static final Random r = new Random();
    private int ancho;
    private int alto;
    private int cantidad;
    private int pisadas = 0;

    public Tablero(int alto, int ancho, int cantidad)
    {
	matriz = new Casillero[alto][ancho];
	int c, i, j;
	for (c = 0; c < cantidad; c++)
	{
	    do
	    {
		i = r.nextInt(alto);
		j = r.nextInt(ancho);
	    } while (matriz[i][j] != null);
	    matriz[i][j] = new Casillero(true);
	}

	for (i = 0; i < alto; i++)
	    for (j = 0; j < ancho; j++)
	    {
		if (matriz[i][j] == null)
		{
		    matriz[i][j] = new Casillero(false);
		}
	    }
	this.ancho = ancho;
	this.alto = alto;
	this.cantidad = cantidad;

	for (i = 0; i < alto; i++)
	    for (j = 0; j < ancho; j++)
		if (!matriz[i][j].isMina())
		    matriz[i][j].setCantidadEntorno(this.cuenta(i, j));
    }

    @Override
    public int getAncho()
    {
	return ancho;
    }

    @Override
    public int getAlto()
    {
	return alto;
    }

    @Override
    public int getCantidad()
    {
	return cantidad;
    }

    private int cuenta(int i, int j)
    {
	int respuesta = 0;
	int ii, jj;
	for (ii = i - 1; ii <= i + 1; ii++)
	    for (jj = j - 1; jj <= j + 1; jj++)
		if ((ii >= 0) && (ii < this.alto) && (jj >= 0) && (jj < this.ancho) && matriz[ii][jj].isMina())
		    respuesta++;
	return respuesta;
    }

    @Override
    public boolean pisa(int i, int j)
    {
	this.pisadas++;
	this.matriz[i][j].pisar();
	if (!this.matriz[i][j].isMina() && this.matriz[i][j].getCantidadEntorno() == 0)
	{
	    if (i > 0 && !matriz[i - 1][j].isPisado() && !matriz[i - 1][j].isMarcado())
		pisa(i - 1, j);
	    if (i < alto - 1 && !matriz[i + 1][j].isPisado() && !matriz[i + 1][j].isMarcado())
		pisa(i + 1, j);
	    if (j > 0 && !matriz[i][j - 1].isPisado() && !matriz[i][j - 1].isMarcado())
		pisa(i, j - 1);
	    if (j < ancho - 1 && !matriz[i][j + 1].isPisado() && !matriz[i][j + 1].isMarcado())
		pisa(i, j + 1);
	    if ((i > 0) && (j > 0) && !matriz[i - 1][j - 1].isPisado() && !matriz[i - 1][j - 1].isMarcado())
		pisa(i - 1, j - 1);
	    if ((i < alto - 1) && (j > 0) && !matriz[i + 1][j - 1].isPisado() && !matriz[i + 1][j - 1].isMarcado())
		pisa(i + 1, j - 1);
	    if ((i > 0) && (j < ancho - 1) && !matriz[i - 1][j + 1].isPisado() && !matriz[i - 1][j + 1].isMarcado())
		pisa(i - 1, j + 1);
	    if ((i < alto - 1) && (j < ancho - 1) && !matriz[i + 1][j + 1].isPisado()
		    && !matriz[i + 1][j + 1].isMarcado())
		pisa(i + 1, j + 1);
	}
	
	return this.matriz[i][j].isMina();

    }

    @Override
    public String toString()
    {
	StringBuilder sb = new StringBuilder();
	// return "Tablero [matriz=" + Arrays.toString(matriz) + "]";
	for (int i = 0; i < this.alto; i++)
	{
	    for (int j = 0; j < ancho; j++)
		sb.append(this.matriz[i][j]);
	    sb.append("\n");

	}
	sb.append("\nPisadas: " + this.pisadas);
	return sb.toString();
    }

    @Override
    public void marca(int i, int j)
    {
	if (!this.matriz[i][j].isPisado())
	{
	    this.matriz[i][j].setMarcado(!this.matriz[i][j].isMarcado());
	}
    }

    @Override
    public int getEntorno(int i, int j)
    {
	return this.matriz[i][j].getCantidadEntorno();

    }

    @Override
    public boolean isPisado(int i, int j)
    {
	// TODO Auto-generated method stub
	return this.matriz[i][j].isPisado();
    }

    @Override
    public boolean isMarcado(int i, int j)
    {
	// TODO Auto-generated method stub
	return this.matriz[i][j].isMarcado();
    }

    @Override
    public boolean isMina(int i, int j)
    {
	// TODO Auto-generated method stub
	return this.matriz[i][j].isMina();
    }

    @Override
    public int getPisadas()
    {
	return pisadas;
    }
    
    public boolean gano() 
    {
    	return this.pisadas==this.ancho*this.alto-this.cantidad;
    } 

}
