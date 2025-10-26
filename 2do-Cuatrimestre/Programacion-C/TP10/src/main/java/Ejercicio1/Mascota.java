package Ejercicio1;

public class Mascota extends Observado implements Runnable
{
    private EstadoObservado estado;

    public Mascota(String nombre)
    {
        estado = new EstadoObservado(nombre);
    }

    public void jugar(){
        estado.setJugando(true);
        estado.setTieneHambre(false);
        estado.setTieneSed(false);
    }

    public void hambre(){
        estado.setTieneHambre(true);
        estado.setTieneSed(false);
        estado.setJugando(false);
    }

    public void sed(){
        estado.setTieneSed(true);
        estado.setTieneHambre(false);
        estado.setJugando(false);
    }

    private void realizarAccionAleatoria()
    {
        int accion = (int) (Math.random() * 3);
        switch (accion)
        {
            case 0:
                this.jugar();
                break;
            case 1:
                this.hambre();
                break;
            case 2:
                this.sed();
                break;
        }
        try
        {
            Thread.sleep((long) (Math.random() * 5000 + 1000));
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }

    @Override
    public void run()
    {
        // necesito esperar un tiempo aleatorio entre 1 y 5 segundos y elegir una accion aleatoria
        while (true)
        {
            this.realizarAccionAleatoria();
            this.notificarObservadores();
        }

    }

    @Override
    public Object getEstado()
    {
        return this.estado;
    }
}
