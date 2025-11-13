package EjemploState;

public class MaquinaExpendedora
{
    private State estado;
    /*
     otros atributos como inventario, etc.
    */

    public MaquinaExpendedora()
    {
        estado = new SinMonedaState(this);
    }

    public State getEstado()
    {
        return estado;
    }

    public void setEstado(State estado)
    {
        this.estado = estado;
    }


    public void insertarMoneda()
    {
        estado.insertarMoneda();
    }


    public void seleccionarProducto()
    {
        estado.seleccionarProducto();
    }

    public void retirarProducto()
    {
        estado.retirarProducto();
    }
}
