package Ejercicio2;

public class LineaDePedido implements Comparable<LineaDePedido>
{
    private int cantidad;
    private Producto producto;
    private long serialVersionUID;

    public LineaDePedido(int cantidad, Producto producto, long serialVersionUID)
    {
        this.cantidad = cantidad;
        this.producto = producto;
        this.serialVersionUID = serialVersionUID;
    }

    public int getCantidad()
    {
        return cantidad;
    }

    public void setCantidad(int cantidad)
    {
        this.cantidad = cantidad;
    }

    public Producto getProducto()
    {
        return producto;
    }

    public void setProducto(Producto producto)
    {
        this.producto = producto;
    }

    public long getSerialVersionUID()
    {
        return serialVersionUID;
    }

    public void setSerialVersionUID(long serialVersionUID)
    {
        this.serialVersionUID = serialVersionUID;
    }

    @Override
    public int hashCode()
    {
        return Long.hashCode(serialVersionUID);
    }

    @Override
    public boolean equals(Object obj)
    {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        LineaDePedido other = (LineaDePedido) obj;
        return serialVersionUID == other.serialVersionUID;
    }

    @Override
    public int compareTo(LineaDePedido o)
    {
        return Long.compare(this.serialVersionUID, o.serialVersionUID);
    }
}
