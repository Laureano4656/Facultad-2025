package ejercicio3.vista;

import ejercicio3.ParametrosInvalidosExcpetion;
import ejercicio3.modelo.ICelda;
import ejercicio3.modelo.IMemoTest;

import javax.swing.*;
import javax.swing.border.BevelBorder;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.*;


public class Ventana extends JFrame implements KeyListener, MouseListener
{
    private int ancho;
    private int alto;

    private JPanel contentPanel;
    private JPanel topPanel;
    private JPanel topLeftPanel;
    private JPanel topRightPanel;
    private JPanel centerPanel;

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

    public Ventana(int ancho, int alto) throws ParametrosInvalidosExcpetion
    {
        if (ancho <= 0 || alto <= 0)
        {
            throw new ParametrosInvalidosExcpetion("Los parametros deben ser mayores a 0");
        }
        if (ancho % 2 != 0 || alto % 2 != 0)
        {
            throw new ParametrosInvalidosExcpetion("Los parametros deben ser pares");
        }
        this.alto = alto;
        this.ancho = ancho;

        this.contentPanel = new JPanel();
        this.contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
        this.contentPanel.setLayout(new BorderLayout(0, 0));
        this.setContentPane(this.contentPanel);

        this.topPanel = new JPanel();
        this.contentPanel.add(this.topPanel, BorderLayout.NORTH);
        this.topPanel.setLayout(new BorderLayout(0, 0));
        this.topLeftPanel = new JPanel();
        this.topLeftPanel.setLayout(new FlowLayout());
        this.topLeftLeftPanel = new JPanel();
        this.topLeftLeftPanel.setLayout(new FlowLayout());
        this.topLeftLeftTopPanel = new JPanel();
        this.topLeftLeftTopPanel.setLayout(new FlowLayout());
        this.anchoLabel = new JLabel("Ancho:");
        this.campoAncho = new TextField(5);
        this.campoAncho.addKeyListener(this);
        this.topLeftLeftTopPanel.add(this.anchoLabel);
        this.topLeftLeftTopPanel.add(this.campoAncho);
        this.topLeftLeftPanel.add(this.topLeftLeftTopPanel);

        this.topLeftLeftBottomPanel = new JPanel();
        this.topLeftLeftBottomPanel.setLayout(new FlowLayout());
        this.altoLabel = new JLabel("Alto:");
        this.campoAlto = new TextField(5);
        this.campoAlto.addKeyListener(this);
        this.topLeftLeftBottomPanel.add(this.altoLabel);
        this.topLeftLeftBottomPanel.add(this.campoAlto);
        this.topLeftLeftPanel.add(this.topLeftLeftBottomPanel);
        this.topLeftPanel.add(this.topLeftLeftPanel);

        this.topLeftRightPanel = new JPanel();
        this.botonAceptarSize = new JButton("Aceptar");
        this.topLeftRightPanel.add(this.botonAceptarSize);


        this.topPanel.add(this.topLeftPanel, BorderLayout.WEST);


        this.topRightPanel = new JPanel();
        this.topRightPanel.setLayout(new FlowLayout());


        this.topPanel.add(this.topRightPanel, BorderLayout.EAST);

    }

    public void setActionListener(ActionListener actionListener)
    {
        this.botonAceptarSize.addActionListener(actionListener);
        this.actionListener = actionListener;
    }

    public void iniciarJuego(int alto, int ancho)
    {
        this.campoAncho.setEnabled(false);
        this.campoAlto.setEnabled(false);
        this.botonAceptarSize.setEnabled(false);
        this.anchoLabel.setEnabled(false);
        this.altoLabel.setEnabled(false);

        this.centerPanel = new JPanel();
        this.centerPanel.setLayout(new GridLayout(0, ancho));
        this.contentPanel.add(this.centerPanel, BorderLayout.CENTER);
        this.casillas = new PanelConCelda[alto][ancho];
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
                    this.casillas[i][j].repaint();
                }
                else
                {
                    this.casillas[i][j].setBorder(new EmptyBorder(5, 5, 5, 5));
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
        String command= "";
        ICelda celda = (ICelda) e.getSource();
        if (e.getButton() == MouseEvent.BUTTON1){
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

