package EjemploMVC;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Controlador implements ActionListener
{
    private Modelo modelo;
    private IVista vista;

    public Controlador(Modelo modelo, IVista vista)
    {
        this.modelo = modelo;
        this.vista = vista;
        this.vista.setActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        /* manejar eventos de la vista y actualizar el modelo y la vista en consecuencia */
    }
}
