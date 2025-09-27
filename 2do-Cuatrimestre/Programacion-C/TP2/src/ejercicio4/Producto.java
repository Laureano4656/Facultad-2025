package ejercicio4;

public class Producto {
	private String codigo;
	private String descripcion;
	private int precioUnidad;
	
	public Producto(String codigo,String descripcion,int precioUnidad) {
		this.codigo = codigo;
		this.descripcion = descripcion;
		this.precioUnidad = precioUnidad;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public int getPrecioUnidad() {
		return precioUnidad;
	}

	public void setPrecioUnidad(int precioUnidad) {
		this.precioUnidad = precioUnidad;
	}
	
}
