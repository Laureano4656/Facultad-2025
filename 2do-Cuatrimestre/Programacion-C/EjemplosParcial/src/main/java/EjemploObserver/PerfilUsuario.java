package EjemploObserver;

import java.util.Observable;

public class PerfilUsuario extends Observable
{
    /*
        Atributos para el perfil del usuario
     */

    public void publicarActualizacion(String actualizacion)
    {
        /*
            Lógica para agregar la actualización al perfil
         */
        setChanged();
        notifyObservers(actualizacion);
    }
}
