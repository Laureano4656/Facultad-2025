package Ejercicio1;

import java.util.ArrayList;


public class Observador implements IObservador
{
    private ArrayList<Observado> observados;

    public Observador()
    {
        observados = new ArrayList<>();
    }

    public void agregarObservado(Observado observado)
    {
        observados.add(observado);
        observado.agregarObservador(this);
    }


    @Override
    public void observadoActualizado(Observado observado, Object estado)
    {
        if (!observados.contains(observado))
            throw new IllegalArgumentException("El observado no esta registrado en este observador.");

        EstadoObservado estadoObservado = (EstadoObservado) estado;
        if (estadoObservado.isJugando())
        {
            System.out.println(estadoObservado.getNombre() + " esta jugando.");
        } else if (estadoObservado.isTieneHambre())
        {
            System.out.println(estadoObservado.getNombre() + " tiene hambre.");
        } else if (estadoObservado.isTieneSed())
        {
            System.out.println(estadoObservado.getNombre() + " tiene sed.");
        } else
        {
            System.out.println(estadoObservado.getNombre() + " esta aburrido.");
        }
    }
}
