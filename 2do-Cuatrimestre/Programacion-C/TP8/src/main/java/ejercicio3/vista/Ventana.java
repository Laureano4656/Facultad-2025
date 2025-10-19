package ejercicio3.vista;

import ejercicio3.modelo.ParametrosInvalidosExcpetion;
import ejercicio3.modelo.ICelda;
import ejercicio3.modelo.IMemoTest;

import javax.swing.*;
import javax.swing.border.BevelBorder;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.*;


public class Ventana extends JFrame implements KeyListener, MouseListener, IVista
{



    private JPanel topPanel;
    private JPanel topLeftPanel;
    private JPanel topRightPanel;
    private JPanel centerPanel;
    private JPanel contentPane;
    private JPanel topLeftLeftPanel;
    private JPanel topLeftRightPanel;
    private JPanel topLeftLeftTopPanel;
    private JPanel topLeftLeftBottomPanel;
    private JLabel altoLabel;
    private JLabel anchoLabel;
    private TextField campoAlto;
    private TextField campoAncho;
    private JButton botonAceptarSize;

    private JPanel topRightLeftPanel;
    private JPanel topRightRightPanel;

    private PanelConCelda[][] casillas;
    private Recursos recursos;
    private ActionListener actionListener;

    public Ventana()
    {

        this.contentPane = new JPanel();
        this.contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        this.contentPane.setLayout(new BorderLayout(0, 0));
        this.setContentPane(this.contentPane);

        this.topPanel = new JPanel();

        this.topPanel.setLayout(new BorderLayout(0, 0));
        this.topLeftPanel = new JPanel(); // Top Left Panel campos tamaño y boton aceptar
        this.topLeftPanel.setLayout(new BorderLayout(0,0));
        this.topLeftLeftPanel = new JPanel(); // Top Left Left Panel campos ancho y alto
        this.topLeftLeftPanel.setLayout(new FlowLayout());
        this.topLeftLeftTopPanel = new JPanel();
        this.topLeftLeftTopPanel.setLayout(new FlowLayout());

        // campo y label ancho
        this.anchoLabel = new JLabel("Ancho:");
        this.campoAncho = new TextField(5);
        this.campoAncho.addKeyListener(this);
        this.topLeftLeftTopPanel.add(this.anchoLabel);
        this.topLeftLeftTopPanel.add(this.campoAncho);
        this.topLeftLeftPanel.add(this.topLeftLeftTopPanel);

        // campo y label alto
        this.topLeftLeftBottomPanel = new JPanel();
        this.topLeftLeftBottomPanel.setLayout(new FlowLayout());
        this.altoLabel = new JLabel("Alto:");
        this.campoAlto = new TextField(5);
        this.campoAlto.addKeyListener(this);
        this.topLeftLeftBottomPanel.add(this.altoLabel);
        this.topLeftLeftBottomPanel.add(this.campoAlto);
        this.topLeftLeftPanel.add(this.topLeftLeftBottomPanel);

        this.topLeftPanel.add(this.topLeftLeftPanel, BorderLayout.WEST);

        this.topLeftRightPanel = new JPanel();
        this.botonAceptarSize = new JButton("Aceptar");
        this.botonAceptarSize.setActionCommand("INICIAR");
        this.topLeftRightPanel.add(this.botonAceptarSize);

        this.topLeftPanel.add(this.topLeftRightPanel, BorderLayout.EAST);


        this.topPanel.add(this.topLeftPanel, BorderLayout.WEST);


        this.topRightPanel = new JPanel();
        this.topRightPanel.setLayout(new FlowLayout());
        this.topPanel.add(this.topRightPanel, BorderLayout.EAST);

        this.contentPane.add(this.topPanel, BorderLayout.NORTH);

        this.setContentPane(this.contentPane);
        this.setVisible(true);
        this.setSize(500, 500);
    }

    public void setActionListener(ActionListener actionListener)
    {
        this.botonAceptarSize.addActionListener(actionListener);
        this.actionListener = actionListener;
    }

    @Override
    public int getAncho()
    {
        return Integer.parseInt(this.campoAncho.getText());

    }

    @Override
    public int getAlto()
    {
        return Integer.parseInt(this.campoAlto.getText());
    }

    @Override
    public void iniciarJuego(int alto, int ancho)
    {
        this.campoAncho.setEnabled(false);
        this.campoAlto.setEnabled(false);
        this.botonAceptarSize.setEnabled(false);
        this.anchoLabel.setEnabled(false);
        this.altoLabel.setEnabled(false);

        this.centerPanel = new JPanel();
        System.out.println("Ancho: " + ancho + " Alto: " + alto);
        this.centerPanel.setLayout(new GridLayout(alto, ancho));
        this.contentPane.add(this.centerPanel, BorderLayout.CENTER);
        this.casillas = new PanelConCelda[alto][ancho];

        this.recursos = new Recursos(ancho, alto);

        for (int i = 0; i < alto; i++)
        {
            for (int j = 0; j < ancho; j++)
            {
                PanelConCelda panelConCelda = new PanelConCelda(i, j);
                this.casillas[i][j] = panelConCelda;
                this.casillas[i][j].setBorder(new BevelBorder(BevelBorder.RAISED));
                panelConCelda.addMouseListener(this);
                this.centerPanel.add(panelConCelda);
            }

        }
        this.setBounds(100, 100, this.topPanel.getWidth() + 52 * ancho, 52 * alto + 125);

    }

    @Override
    public void dibujar(IMemoTest tablero)
    {
        for (int i = 0; i < tablero.getAlto(); i++)
        {
            for (int j = 0; j < tablero.getAncho(); j++)
            {
                if (tablero.isDadoVuelta(i, j))
                {
                    this.casillas[i][j].setBorder(new BevelBorder(BevelBorder.LOWERED));
                    ImageIcon imageIcon = this.recursos.getImagen(i, j);
                    this.casillas[i][j].setImageIcon(imageIcon);

                } else
                {
                    this.casillas[i][j].setBorder(new BevelBorder(BevelBorder.RAISED));
                    this.casillas[i][j].setImageIcon(null);
                }
            }
        }
        this.repaint();
    }

    @Override
    public void keyTyped(KeyEvent e)
    {

    }

    @Override
    public void keyPressed(KeyEvent e)
    {

    }

    @Override
    public void keyReleased(KeyEvent e)
    {
        int ancho = 0;
        int alto = 0;
        try
        {
            ancho = Integer.parseInt(this.campoAncho.getText());
            alto = Integer.parseInt(this.campoAlto.getText());
        } catch (NumberFormatException ex)
        {
            System.out.println(ex.getMessage());
        }
        boolean condicion = ancho > 0 && alto > 0;
        this.botonAceptarSize.setEnabled(condicion);
    }

    @Override
    public void mouseClicked(MouseEvent e)
    {

    }

    @Override
    public void mousePressed(MouseEvent e)
    {
        ActionEvent event;
        String command = "";
        ICelda celda = (ICelda) e.getSource();
        if (e.getButton() == MouseEvent.BUTTON1)
        {
            command = "DESCUBRIR_" + celda.getI() + "_" + celda.getJ();
        }
        event = new ActionEvent(celda, 0, command);
        this.actionListener.actionPerformed(event);
    }

    @Override
    public void mouseReleased(MouseEvent e)
    {

    }

    @Override
    public void mouseEntered(MouseEvent e)
    {

    }

    @Override
    public void mouseExited(MouseEvent e)
    {

    }
}

