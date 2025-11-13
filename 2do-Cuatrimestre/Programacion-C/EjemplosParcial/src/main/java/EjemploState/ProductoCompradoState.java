package EjemploState;

public class ProductoCompradoState implements State
{
    private MaquinaExpendedora maquina;

    public ProductoCompradoState(MaquinaExpendedora maquina)
    {
        this.maquina = maquina;
    }

    public void insertarMoneda()
    {
        System.out.println("Por favor, retire su producto antes de insertar otra moneda.");
    }

    public void seleccionarProducto()
    {
        System.out.println("Por favor, retire su producto antes de seleccionar otro.");
    }

    public void retirarProducto()
    {
        /*
        Lógica para dispensar el producto
         */
         if ( /*no se encuentra el producto */ )
             maquina.setEstado(new AgotadoState(this.maquina));
        else
            maquina.setEstado(new SinMonedaState(maquina));
    }
}
