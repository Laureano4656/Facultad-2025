package ejercicio3.vista;

import ejercicio3.modelo.Celda;
import ejercicio3.modelo.ICelda;

import javax.swing.*;
import javax.swing.border.BevelBorder;
import java.awt.*;
import java.awt.event.ActionListener;

public class PanelConCelda extends JPanel implements ICelda
{
    private ICelda celda;
    private ImageIcon imagen;

    public void setImageIcon(ImageIcon imageIcon)
    {
        this.imagen = imageIcon;
    }

    public PanelConCelda(int i, int j)
    {
        this.setBorder(new BevelBorder(BevelBorder.RAISED));
        this.celda = new Celda(i, j);
    }

    @Override
    public void paint(Graphics g)
    {
        super.paint(g);
        if (this.imagen != null)
        {
            System.out.println("this.imagen");
            int dx = (this.getWidth() - this.imagen.getIconWidth()) / 2;
            int dy = (this.getHeight() - this.imagen.getIconHeight()) / 2;
            g.drawImage(this.imagen.getImage(), dx, dy, null);
        }
    }

    @Override
    public int getI()
    {
        return celda.getI();
    }

    @Override
    public int getJ()
    {
        return celda.getJ();
    }
}
