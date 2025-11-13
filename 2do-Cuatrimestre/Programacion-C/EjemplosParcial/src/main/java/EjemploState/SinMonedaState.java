package EjemploState;

public class SinMonedaState implements State
{
    private MaquinaExpendedora maquina;

    public SinMonedaState(MaquinaExpendedora maquina)
    {
        this.maquina = maquina;
    }

    public void insertarMoneda()
    {
        System.out.println("Moneda insertada. Ahora puede seleccionar un producto.");
        maquina.setEstado(new ConMonedaState(this.maquina));
    }

    public void seleccionarProducto()
    {
        System.out.println("Debe insertar una moneda primero.");
    }

    public void retirarProducto()
    {
        System.out.println("Debe insertar una moneda y seleccionar un producto primero.");
    }
}
