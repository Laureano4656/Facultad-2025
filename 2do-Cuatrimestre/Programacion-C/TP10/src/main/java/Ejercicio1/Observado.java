package Ejercicio1;

import java.util.ArrayList;

public abstract class Observado
{
    private ArrayList <IObservador> observers;

    public Observado()
    {
        observers = new ArrayList<>();
    }
    public void agregarObservador(IObservador observer)
    {
        observers.add(observer);
    }
    public void eliminarObservador(IObservador observer)
    {
        observers.remove(observer);
    }
    public void notificarObservadores()
    {
        for (IObservador observer : observers)
        {
            observer.observadoActualizado(this, this.getEstado());
        }
    }

    public abstract Object getEstado();

}
