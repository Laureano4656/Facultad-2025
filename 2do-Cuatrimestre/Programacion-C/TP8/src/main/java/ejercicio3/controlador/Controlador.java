package ejercicio3.controlador;

import ejercicio3.modelo.ParametrosInvalidosExcpetion;
import ejercicio3.modelo.Tablero;
import ejercicio3.vista.IVista;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Controlador implements ActionListener
{
    private Tablero tablero;
    private IVista vista;


    public Tablero getTablero()
    {
        return tablero;
    }

    public void setTablero(Tablero tablero)
    {
        this.tablero = tablero;
    }

    public IVista getVista()
    {
        return vista;
    }

    public void setVista(IVista vista)
    {

        this.vista = vista;
        this.vista.setActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        String comando = e.getActionCommand();
        if (comando.equalsIgnoreCase("INICIAR"))
        {
            System.out.println("Iniciando");
            try
            {
                this.tablero = new Tablero(vista.getAlto(), vista.getAncho());

            } catch (ParametrosInvalidosExcpetion err)
            {

            }
            this.vista.iniciarJuego(vista.getAlto(), vista.getAncho());
        } else if (comando.contains("DESCUBRIR"))
        {
            System.out.println("Desubiando");
            String[] partes = comando.split("_");
            int i = Integer.parseInt(partes[1]);
            int j = Integer.parseInt(partes[2]);
            if (!this.tablero.isDescubierta(i, j))
            {
                this.tablero.darVuelta(i, j);
                this.vista.dibujar(tablero);
            }
        }



    }
}
