package EjemploConcurrencia;

public class TrabajoImpresion implements Runnable
{
    private final GestorImpresora gestorImpresora;
    private String nombreDocumento;
    public TrabajoImpresion(GestorImpresora gestorImpresora, String nombreDocumento)
    {
        this.gestorImpresora = gestorImpresora;
        this.nombreDocumento = nombreDocumento;
    }


    @Override
    public void run()
    {
        gestorImpresora.imprimir(this.nombreDocumento);
        try
        {
            Thread.sleep(2000); // simula tiempo de impresión
        }
        catch (InterruptedException e)
        {}
        gestorImpresora.finalizarImpresion(this.nombreDocumento);
    }
}
