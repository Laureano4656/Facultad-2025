package EjemploConcurrencia;

public class Prueba
{
    public static void main(String[] args) {

        System.out.println("Iniciando la cola de impresión...");

        // 1. Se crea UN ÚNICO gestor (el recurso compartido).
        GestorImpresora gestorUnico = new GestorImpresora();

        // 2. Se crean varios hilos (trabajos).
        // Todos comparten la MISMA instancia de 'gestorUnico'.
        Thread t1 = new Thread(new TrabajoImpresion(gestorUnico, "Documento-A"));
        Thread t2 = new Thread(new TrabajoImpresion(gestorUnico, "Informe-Anual-B"));
        Thread t3 = new Thread(new TrabajoImpresion(gestorUnico, "Foto-C"));
        Thread t4 = new Thread(new TrabajoImpresion(gestorUnico, "Contrato-D"));

        // 3. Se lanzan los hilos (no necesariamente en este orden)
        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }
}
