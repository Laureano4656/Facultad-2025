package vista;

import javax.swing.ImageIcon;

public class Recursos
{
    private ImageIcon bandera = new ImageIcon("bandera.png");
    private ImageIcon explosion = new ImageIcon("explosion.png");
    private ImageIcon mina = new ImageIcon("mina.png");
    private ImageIcon numeros[] = new ImageIcon[8];
    {
	for (int i = 0; i < 8; i++)
	    numeros[i] = new ImageIcon(String.valueOf(i + 1) + ".png");
    }

    public ImageIcon getBandera()
    {
	return bandera;
    }

    public void setBandera(ImageIcon bandera)
    {
	this.bandera = bandera;
    }

    public ImageIcon getExplosion()
    {
	return explosion;
    }

    public void setExplosion(ImageIcon explosion)
    {
	this.explosion = explosion;
    }

    public ImageIcon getMina()
    {
	return mina;
    }

    public void setMina(ImageIcon mina)
    {
	this.mina = mina;
    }

    public ImageIcon getNumero(int i)
    {
	return this.numeros[i - 1];
    }

    public void setNumero(int i, ImageIcon numero)
    {
	numeros[i - 1] = numero;
    }

}
