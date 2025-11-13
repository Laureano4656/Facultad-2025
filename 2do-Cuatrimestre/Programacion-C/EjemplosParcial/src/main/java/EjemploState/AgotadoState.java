package EjemploState;

public class AgotadoState implements State
{
    private MaquinaExpendedora maquina;

    public AgotadoState(MaquinaExpendedora maquina)
    {
        this.maquina = maquina;
    }

    public void insertarMoneda()
    {
        System.out.println("La máquina está agotada. No se pueden aceptar monedas.");
    }

    public void seleccionarProducto()
    {
        System.out.println("La máquina está agotada. No hay productos disponibles.");
    }

    public void retirarProducto()
    {
        System.out.println("La máquina está agotada. No hay productos para retirar.");
    }
}
