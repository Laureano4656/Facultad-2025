public class Ambulancia
{
    public synchronized void trasladarALaClinica(Asociado a) {
        assert a != null;

        while (this.isOcupado() && this.isSimulacionActiva()) {
            try {
                setChanged();
                notifyObservers(...);
                wait();
            } catch (InterruptedException e) {
                (...)
            }
        }

        // Si la simulación terminó mientras esperaba, salir
        if (!this.isSimulacionActiva()) {
            return;
        }
        this.setOcupado(true);
        this.setChanged();
        // Cambiar estado primero
        this.estadoActual.SolicitudDeTraslado();
        setChanged();
        notifyObservers(...);
    }
}
