package Ejercicio7;

import java.util.ArrayList;

public class Bote
{
    private final int capacidad;
    private int ocupantes;
    private boolean destino; // 0 - Orilla izquierda, 1 - Orilla derecha
    private ArrayList<Persona> personas;

    public Bote(int capacidad, ArrayList<Persona> personas)
    {
        this.capacidad = capacidad;
        this.ocupantes = 0;
        this.destino = false; // Comienza en orilla derecha con destino a izquierda
        this.personas = personas;
    }

    public synchronized void subir(Persona persona)
    {
        while ((ocupantes >= capacidad || this.destino != persona.getDestino() || persona.isEnDestino()) & !sinPersonasOrillaActual())
        {
            try
            {
                // imprimo condicion para debug
//                System.out.println("--- Condición no cumplida para " + persona.getNombre() + ": Ocupantes: " + ocupantes + "/" + capacidad +
//                        ", Destino bote: " + (this.destino ? "derecha" : "izquierda") +
//                        ", Destino persona: " + (persona.getDestino() ? "derecha" : "izquierda") +
//                        ", Persona en destino: " + persona.isEnDestino() +
//                        ", Sin personas en orilla actual: " + sinPersonasOrillaActual());
                System.out.println("... " + persona.getNombre() + " está esperando para subir al bote.");
                wait();
            } catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
        if (sinPersonasOrillaActual())
        {
            zarpar();
        } else
        {
            this.ocupantes++;
            System.out.println(">> " + persona.getNombre() + " ha subido al bote. Ocupantes: " + ocupantes);
            if (ocupantes == capacidad || sinPersonasOrillaActual())
            {
                zarpar();
            }
        }
        notifyAll();
    }

    private synchronized boolean sinPersonasOrillaActual()
    {
        int esperandoEnEstaOrilla = 0;

        // 1. Contamos todas las personas que AÚN NO LLEGAN a su destino
        //    Y que están esperando EN ESTA ORILLA (quieren ir al lado opuesto)
        for (Persona p : this.personas)
        {
            boolean estaEnEstaOrilla = (p.getDestino() == this.destino);

            if (!p.isEnDestino() && estaEnEstaOrilla)
            {
                esperandoEnEstaOrilla++;
            }
        }
        // 2. Si el número de personas esperando es mayor que 0 (hay gente)
        //    Y es igual al número de personas que ya subieron,
        //    entonces no queda nadie más por subir.
//        System.out.println(esperandoEnEstaOrilla + " personas esperando en la orilla ");
        return esperandoEnEstaOrilla == 0; // No queda nadie más en la orilla
// Aún queda gente en la orilla (o no había nadie para empezar)
    }

    private synchronized void zarpar()
    {
        System.out.println("-- Zarpando hacia la orilla " + (this.destino ? "derecha" : "izquierda") + " con " + ocupantes + " ocupantes...");
        int tiempoViaje = (int) (Math.random() * 2000) + 1000; // Tiempo de viaje entre 1 y 3 segundos
        try
        {
            Thread.sleep(tiempoViaje);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }
        System.out.println("<< El bote ha llegado a la orilla " + (this.destino ? "derecha" : "izquierda") + ".");
        this.destino = !this.destino; // Cambiar destino a orilla opuesta
        this.ocupantes = 0;
    }
}
