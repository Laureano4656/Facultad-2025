package modelo;

public class Casillero
{
    private boolean mina;
    private boolean pisado = false;
    private boolean marcado = false;
    private int cantidadEntorno = 0;

    public Casillero(boolean mina)
    {
	this.mina = mina;
    }

    public boolean isMina()
    {
	return mina;
    }

    public boolean isPisado()
    {
	return pisado;
    }

    public boolean isMarcado()
    {
	return marcado;
    }

    protected void pisar()
    {
	this.pisado = true;
    }

    protected void setMarcado(boolean marcado)
    {
	this.marcado = marcado;
    }

    public int getCantidadEntorno()
    {
	return cantidadEntorno;
    }

    protected void setCantidadEntorno(int cantidadEntorno)
    {
	this.cantidadEntorno = cantidadEntorno;
    }

    @Override
    public String toString()
    {
	String banderita = String.valueOf(this.cantidadEntorno);
	if (this.isMina())
	    banderita = "*";
	String respuesta = " " + banderita + " ";
	if (this.isPisado())
	    respuesta = "[" + banderita + "]";
	else if (this.isMarcado())
	    respuesta = "{" + banderita + "}";
	return respuesta;
    }
}
