package Ejercicio2;

public class Pedido
{
    private String fecha;
    private Proveedor proveedor;
    private long serialVersionUID;

    public Pedido(String fecha, Proveedor proveedor, long serialVersionUID)
    {
        this.fecha = fecha;
        this.proveedor = proveedor;
        this.serialVersionUID = serialVersionUID;
    }
    public double total()
    {
        return 0;
    }
    public String detalle(){

    }

    public String getFecha()
    {
        return fecha;
    }

    public void setFecha(String fecha)
    {
        this.fecha = fecha;
    }

    public Proveedor getProveedor()
    {
        return proveedor;
    }

    public void setProveedor(Proveedor proveedor)
    {
        this.proveedor = proveedor;
    }

    public long getSerialVersionUID()
    {
        return serialVersionUID;
    }

    public void setSerialVersionUID(long serialVersionUID)
    {
        this.serialVersionUID = serialVersionUID;
    }
}
