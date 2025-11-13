package EjemploObserver;

import java.util.ArrayList;
import java.util.Observable;
import java.util.Observer;

public class Seguidor implements Observer
{
    private ArrayList<PerfilUsuario> seguidos;

    public Seguidor(PerfilUsuario p)
    {
        seguidos = new ArrayList<PerfilUsuario>();
        seguidos.add(p);
        p.addObserver(this);
    }

    public void seguir(PerfilUsuario p)
    {
        seguidos.add(p);
        p.addObserver(this);
    }

    @Override
    public void update(Observable o, Object arg)
    {
        if (!this.seguidos.contains(o))
            throw new IllegalArgumentException("El perfil no es seguido por este seguidor.");
        /*
            Lógica para manejar la actualización del perfil seguido
        */
    }
}
