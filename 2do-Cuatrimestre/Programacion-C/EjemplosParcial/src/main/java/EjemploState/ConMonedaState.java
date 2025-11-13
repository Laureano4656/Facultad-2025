package EjemploState;

public class ConMonedaState implements State
{
    private MaquinaExpendedora maquina;

    public ConMonedaState(MaquinaExpendedora maquina)
    {
        this.maquina = maquina;
    }

    public void insertarMoneda()
    {
        System.out.println("Ya hay una moneda insertada.");
    }

    public void seleccionarProducto()
    {
        System.out.println("Producto seleccionado. Retire su producto.");
        maquina.setEstado(new ProductoCompradoState(this.maquina));
    }

    public void retirarProducto()
    {
        System.out.println("Debe seleccionar un producto primero.");
    }
}
