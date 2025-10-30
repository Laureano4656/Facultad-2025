package Ejercicio2;

public class Mostrador extends Thread
{
    private int maxPersonas;
    private int personaAtender = 1;
    public Mostrador(int maxPersonas)
    {
        this.maxPersonas = maxPersonas;
    }
    public synchronized void atenderPersona(int nro)
    {
        while (nro != personaAtender)
        {
            System.out.println("Persona " + nro + " - Va a esperar su turno");
            try
            {
                wait();
            }
            catch (InterruptedException e)
            {
                Thread.currentThread().interrupt();
            }
        }
        System.out.println("Mostrador atendiendo a la Persona " + nro);
        try{
            Thread.sleep(1000);
        } catch (InterruptedException e){
            Thread.currentThread().interrupt();
        }
        System.out.println("Mostrador terminó de atender a la Persona " + nro);
        personaAtender++;
        if (personaAtender > 3)
        {
            personaAtender = 1;
        }
        notifyAll();
    }
}
