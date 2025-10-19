package controlador;

import java.awt.event.ActionListener;

public interface IVista
{
	static final String INCREMENTA = "INCREMENTA";
	static final String DECREMENTA = "DECREMENTA";

	int getCantidad();

	void actualizaValor(int valor);

	void addActionListener(ActionListener actionListener);

}
