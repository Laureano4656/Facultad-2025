package EjemploMVC;

import java.awt.event.ActionListener;

public interface IVista
{
    /* definicion de metodos para actualizar la vista
     y obtener los datos necesarios para el modelo */

    /* método para registrar el controlador como listener de acciones */
    void setActionListener(ActionListener listener);
}
