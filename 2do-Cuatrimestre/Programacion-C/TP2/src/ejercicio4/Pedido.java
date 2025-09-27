package ejercicio4;

import java.time.LocalDateTime;
import java.util.ArrayList;

public class Pedido {
	private Empleado empleado;
	private LocalDateTime fecha;
	private ArrayList<LineaDePedido> lineaDePedido = new ArrayList<LineaDePedido>();
	
	public Pedido(Empleado empleado,LocalDateTime fecha) {
		this.empleado = empleado;		
	}

}
