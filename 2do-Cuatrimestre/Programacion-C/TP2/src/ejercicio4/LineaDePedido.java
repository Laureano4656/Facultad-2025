package ejercicio4;

public class LineaDePedido {
	private Producto producto;
	private int cantidad;
	
	public LineaDePedido(Producto producto) {
		this.producto = producto;
		this.cantidad = 0;
	}
	public Producto getProducto() {
		return producto;
	}
	public void setProducto(Producto producto) {
		this.producto = producto;
	}
	public int getCantidad() {
		return cantidad;
	}
	public void setCantidad(int cantidad) {
		this.cantidad = cantidad;
	}
	
}
