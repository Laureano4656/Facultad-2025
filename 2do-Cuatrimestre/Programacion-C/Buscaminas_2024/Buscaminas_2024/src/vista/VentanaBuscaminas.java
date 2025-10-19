package vista;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.BevelBorder;
import javax.swing.border.EmptyBorder;

import modelo.IBuscaminas;
import modelo.ICelda;

public class VentanaBuscaminas extends JFrame implements KeyListener, IVista, MouseListener
{

    private JPanel contentPane;
    private JPanel panelOeste;
    private JPanel panelCentral;
    private JLabel lbl_Alto;
    private JTextField textField_Alto;
    private JPanel panel;
    private JPanel panel_1;
    private JPanel panel_2;
    private JLabel lbl_Ancho;
    private JPanel panel_3;
    private JTextField textField_Ancho;
    private JPanel panel_4;
    private JLabel lbl_Cantidad;
    private JPanel panel_5;
    private JTextField textField_Cantidad;
    private JPanel panel_6;
    private JPanel panel_7;
    private JButton btnIniciar;
    private ActionListener actionListener;
    private PanelConCelda[][] casilleros;
    private static Recursos recursos = new Recursos();

  
    public VentanaBuscaminas()
    {
	setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	setBounds(100, 100, 450, 300);
	this.contentPane = new JPanel();
	this.contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
	this.contentPane.setLayout(new BorderLayout(0, 0));
	setContentPane(this.contentPane);

	this.panelOeste = new JPanel();
	this.contentPane.add(this.panelOeste, BorderLayout.WEST);
	this.panelOeste.setLayout(new GridLayout(0, 2, 0, 0));

	this.panel = new JPanel();
	this.panelOeste.add(this.panel);

	this.lbl_Alto = new JLabel("Alto:");
	this.panel.add(this.lbl_Alto);

	this.panel_1 = new JPanel();
	this.panelOeste.add(this.panel_1);

	this.textField_Alto = new JTextField();
	this.textField_Alto.addKeyListener(this);
	this.panel_1.add(this.textField_Alto);
	this.textField_Alto.setColumns(10);

	this.panel_2 = new JPanel();
	this.panelOeste.add(this.panel_2);

	this.lbl_Ancho = new JLabel("Ancho:");
	this.panel_2.add(this.lbl_Ancho);
	this.panel_3 = new JPanel();
	this.panelOeste.add(this.panel_3);

	this.textField_Ancho = new JTextField();
	this.textField_Ancho.setColumns(10);
	this.panel_3.add(this.textField_Ancho);
	this.textField_Ancho.addKeyListener(this);
	this.panel_4 = new JPanel();
	this.panelOeste.add(this.panel_4);

	this.lbl_Cantidad = new JLabel("Cantidad de Minas:");
	this.panel_4.add(this.lbl_Cantidad);

	this.panel_5 = new JPanel();
	this.panelOeste.add(this.panel_5);

	this.textField_Cantidad = new JTextField();
	this.textField_Cantidad.setColumns(10);
	this.textField_Cantidad.addKeyListener(this);
	this.panel_5.add(this.textField_Cantidad);

	this.panel_6 = new JPanel();
	this.panelOeste.add(this.panel_6);

	this.panel_7 = new JPanel();
	this.panelOeste.add(this.panel_7);

	this.btnIniciar = new JButton("Iniciar");
	this.btnIniciar.setActionCommand("INICIAR");
	this.btnIniciar.setEnabled(false);
	this.panel_7.add(this.btnIniciar);

	this.panelCentral = new JPanel();
	this.contentPane.add(this.panelCentral, BorderLayout.CENTER);
	this.setVisible(true);
    }

    public void keyPressed(KeyEvent arg0)
    {
    }

    public void keyReleased(KeyEvent arg0)
    {
	int ancho = 0;
	int alto = 0;
	int cantidad = 0;
	try
	{
	    ancho = Integer.parseInt(this.textField_Ancho.getText());
	    alto = Integer.parseInt(this.textField_Alto.getText());
	    cantidad = Integer.parseInt(this.textField_Cantidad.getText());
	} catch (NumberFormatException e)
	{
	}

	boolean condicion = ancho > 0 && alto > 0 && cantidad > 0 && cantidad < ancho * alto;
	this.btnIniciar.setEnabled(condicion);

    }

    public void keyTyped(KeyEvent arg0)
    {
    }

    @Override
    public int getAncho()
    {
	return Integer.parseInt(this.textField_Ancho.getText());
    }

    @Override
    public int getAlto()
    {
	return Integer.parseInt(this.textField_Alto.getText());
    }

    @Override
    public int getCantidad()
    {
	return Integer.parseInt(this.textField_Cantidad.getText());
    }

    @Override
    public void setActionListener(ActionListener actionListener)
    {
	this.btnIniciar.addActionListener(actionListener);
	this.actionListener = actionListener;
    }

    @Override
    public void iniciarJuego(int alto, int ancho)
    {
	this.textField_Alto.setEnabled(false);
	this.textField_Ancho.setEnabled(false);
	this.textField_Cantidad.setEnabled(false);
	this.lbl_Alto.setEnabled(false);
	this.lbl_Ancho.setEnabled(false);
	this.lbl_Cantidad.setEnabled(false);
	this.btnIniciar.setEnabled(false);
	this.panelCentral.setLayout(new GridLayout(0, ancho));
	this.casilleros = new PanelConCelda[alto][ancho];
	for (int i = 0; i < alto; i++)
	    for (int j = 0; j < ancho; j++)
	    {
		this.casilleros[i][j] = new PanelConCelda(i, j);
		this.casilleros[i][j].setBorder(new BevelBorder(BevelBorder.RAISED));
		this.panelCentral.add(this.casilleros[i][j]);
		this.casilleros[i][j].addMouseListener(this);
	    }
	this.setBounds(100, 100, this.panelOeste.getWidth() + 52 * ancho, 52 * alto + 25);
    }

    public void dibujar(IBuscaminas tablero)
    {
	for (int i = 0; i < tablero.getAlto(); i++)
	    for (int j = 0; j < tablero.getAncho(); j++)
	    {
		if (tablero.isPisado(i, j))
		{
		    this.casilleros[i][j].setBorder(new BevelBorder(BevelBorder.LOWERED));
		    if (tablero.isMina(i, j))
		    {
			this.casilleros[i][j].setImageIcon(recursos.getExplosion());
		    } else
		    {
			if (tablero.getEntorno(i, j) > 0)
			    this.casilleros[i][j].setImageIcon(recursos.getNumero(tablero.getEntorno(i, j)));
		    }

		} else
		{
		    if (tablero.isMarcado(i, j))
			this.casilleros[i][j].setImageIcon(recursos.getBandera());
		    else
			this.casilleros[i][j].setImageIcon(null);
		}
	    }
	this.repaint();
    }

    public void dibujarFinal(IBuscaminas tablero)
    {
	for (int i = 0; i < tablero.getAlto(); i++)
	    for (int j = 0; j < tablero.getAncho(); j++)
	    {
		if (tablero.isMina(i, j))
		{
		    if (tablero.isPisado(i, j))
			this.casilleros[i][j].setImageIcon(recursos.getExplosion());
		    else
			this.casilleros[i][j].setImageIcon(recursos.getMina());
		}
	    }
	this.repaint();
    }

    @Override
    public void perder()
    {
    	
	JOptionPane.showMessageDialog(this, "Has Perdido, Juego Terminado");
	this.dispose();
    }

    @Override
    public void ganar()
    {
	JOptionPane.showMessageDialog(this, "Felicitaciones, Has Ganado, Juego Terminado");
	this.dispose();
    }

    @Override
    public void mouseClicked(MouseEvent arg0)
    {
	
    }

    @Override
    public void mouseEntered(MouseEvent arg0)
    {
	
    }

    @Override
    public void mouseExited(MouseEvent arg0)
    {
	

    }

    @Override
    public void mousePressed(MouseEvent arg0)
    {
	ActionEvent event;
	String command;
	ICelda celda = (ICelda) arg0.getSource();
	if (arg0.getButton() != 1)
	    command = "MARCAR";
	else
	    command = "PISAR";
	event = new ActionEvent(celda, 0, command);
	this.actionListener.actionPerformed(event);
    }

    @Override
    public void mouseReleased(MouseEvent arg0)
    {
	

    }
}
