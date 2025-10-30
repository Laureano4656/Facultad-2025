package Ejercicio2;

public class Persona implements Runnable
{
    private int nro;
    private Mostrador mostrador;
    public Persona(int nro, Mostrador mostrador)
    {
        this.nro = nro;
        this.mostrador = mostrador;
    }


    @Override
    public void run()
    {
        for (int i = 0; i < 5; i++)
        {
            System.out.println("Persona " + nro + " - Va a intentar atenderse");
            mostrador.atenderPersona(this.nro);
        }
    }
}
