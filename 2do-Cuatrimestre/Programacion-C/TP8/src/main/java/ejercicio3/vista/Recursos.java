package ejercicio3.vista;

import javax.swing.*;

public class Recursos
{
    private ImageIcon imagenes[][];
    public static final String RUTA_BASE = "/ejercicio3/recursos/64";

    public Recursos(int alto,int ancho)
    {
        imagenes = new ImageIcon[alto][ancho];
        for (int i = 0; i < ancho; i++)
        {
            for (int j = 0; j < alto; j++)
                imagenes[i][j] = new ImageIcon(j + "_64px.png");
        }
    }

    public ImageIcon getImagen(int i,int j)
    {
        return imagenes[i][j];
    }
}
