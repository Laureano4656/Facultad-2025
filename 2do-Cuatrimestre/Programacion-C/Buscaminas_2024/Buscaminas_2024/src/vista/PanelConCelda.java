package vista;

import java.awt.Graphics;
import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.BevelBorder;

import modelo.Celda;
import modelo.ICelda;

public class PanelConCelda extends JPanel implements ICelda
{
    private ICelda celda;
    private ImageIcon imageIcon = null;

    public void setImageIcon(ImageIcon imageIcon)
    {
	this.imageIcon = imageIcon;
    }

    public PanelConCelda(int i, int j)
    {
	this.setBorder(new BevelBorder(BevelBorder.RAISED));
	this.celda = new Celda(i, j);
    }

    @Override
    public int getI()
    {
	return this.celda.getI();
    }

    @Override
    public int getJ()
    {
	return this.celda.getJ();
    }

    @Override
    public void paint(Graphics arg0)
    {
	super.paint(arg0);
        if (this.imageIcon != null)
        {
            int dx = (this.getWidth() - this.imageIcon.getIconWidth()) / 2;
            int dy = (this.getHeight() - this.imageIcon.getIconHeight()) / 2;
            arg0.drawImage(this.imageIcon.getImage(), dx, dy, null);
        }
    }
}
