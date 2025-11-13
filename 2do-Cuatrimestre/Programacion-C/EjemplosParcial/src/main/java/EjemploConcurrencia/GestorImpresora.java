package EjemploConcurrencia;

class GestorImpresora
{

    // Esta es la condición que los hilos deben comprobar.
    private boolean estaOcupada = false;

    /**
     * Método principal que los hilos llamarán.
     * Es 'synchronized' para asegurar que solo UN hilo pueda
     * estar ejecutando este código a la vez (exclusión mutua).
     */
    public synchronized void imprimir(String nombreDocumento)
    {

        // --- EL BLOQUEO PROTEGIDO (Guarded Block) ---
        // 1. Comprobar la condición DENTRO de un 'while'.
        // Se usa 'while' en lugar de 'if' para evitar "despertares espurios"
        // y para re-chequear la condición si múltiples hilos son despertados.
        while (estaOcupada)
        {
            try
            {
                System.out.println("   ... " + nombreDocumento + " está en ESPERA (Impresora ocupada).");

                // 2. LLAMAR A WAIT()
                // El hilo se "duerme" y, crucialmente,
                // ¡LIBERA EL BLOQUEO (synchronized) sobre 'this' (GestorImpresora)!
                // Esto permite que otro hilo (el que está imprimiendo)
                // pueda terminar y llamar a notifyAll().
                wait();

            } catch (InterruptedException e)
            {
                // Buena práctica al manejar InterruptedException
                Thread.currentThread().interrupt();
                System.err.println("Hilo " + nombreDocumento + " fue interrumpido.");
                return;
            }
        }

        // --- SECCIÓN CRÍTICA ---
        // Si el hilo llega aquí, significa que:
        // 1. Tiene el bloqueo (lock).
        // 2. La condición (estaOcupada) era 'false'.
        // 3. Cambiar el estado para reflejar el trabajo
        System.out.println("🖨️ " + nombreDocumento + " COMIENZA A IMPRIMIR...");
        this.estaOcupada = true;
        notifyAll();
    }

    public synchronized void finalizarImpresion(String nombreDocumento)
    {
        // Cambiar el estado para reflejar que la impresora ya no está ocupada
        this.estaOcupada = false;
        System.out.println("   ... " + nombreDocumento + " ha FINALIZADO la impresión.");
        // Notificar a todos los hilos en espera que la condición puede haber cambiado
        notifyAll();
    }
}
