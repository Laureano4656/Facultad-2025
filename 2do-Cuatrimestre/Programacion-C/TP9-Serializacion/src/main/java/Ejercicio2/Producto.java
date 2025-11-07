package Ejercicio2;

public class Producto
{
    private int codigo;
    private String descripcion;
    private double preciounitario;
    private long serialVersionUID;

    public Producto(int codigo, String descripcion, double preciounitario, long serialVersionUID)
    {
        this.codigo = codigo;
        this.descripcion = descripcion;
        this.preciounitario = preciounitario;
        this.serialVersionUID = serialVersionUID;
    }

    public int getCodigo()
    {
        return codigo;
    }

    public void setCodigo(int codigo)
    {
        this.codigo = codigo;
    }

    public String getDescripcion()
    {
        return descripcion;
    }

    public void setDescripcion(String descripcion)
    {
        this.descripcion = descripcion;
    }

    public double getPreciounitario()
    {
        return preciounitario;
    }

    public void setPreciounitario(double preciounitario)
    {
        this.preciounitario = preciounitario;
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
        return Integer.hashCode(codigo);
    }

    @Override
    public boolean equals(Object obj)
    {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Producto producto = (Producto) obj;
        return codigo == producto.codigo;
    }
}
