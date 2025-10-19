package vista;

import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

import controlador.IVista;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;

public class Ventana extends JFrame implements IVista, KeyListener
{

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField textField;
	private JPanel panel;
	private JButton buttonIncrementa;
	private JPanel panel_1;
	private JPanel panel_2;
	private JButton buttonDecrementa;
	private JPanel panel_3;
	private JLabel lblNewLabel;

	/**
	 * Create the frame.
	 */
	public Ventana()
	{
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		this.contentPane = new JPanel();
		this.contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(this.contentPane);
		this.contentPane.setLayout(new GridLayout(0, 1, 0, 0));

		this.panel = new JPanel();
		this.contentPane.add(this.panel);

		this.textField = new JTextField();
		this.textField.addKeyListener(this);
		this.panel.add(this.textField);
		this.textField.setColumns(10);

		this.panel_1 = new JPanel();
		this.contentPane.add(this.panel_1);

		this.buttonIncrementa = new JButton("Incrementa");
		this.buttonIncrementa.setEnabled(false);
		this.panel_1.add(this.buttonIncrementa);

		this.panel_2 = new JPanel();
		this.contentPane.add(this.panel_2);

		this.buttonDecrementa = new JButton("Decrementa");
		this.buttonDecrementa.setEnabled(false);

		this.panel_2.add(this.buttonDecrementa);

		this.panel_3 = new JPanel();
		this.contentPane.add(this.panel_3);

		this.lblNewLabel = new JLabel("");
		this.panel_3.add(this.lblNewLabel);
		this.setVisible(true);

		
	}

	@Override
	public int getCantidad()
	{
		int cantidad = Integer.parseInt(this.textField.getText());
		return cantidad;
	}

	@Override
	public void actualizaValor(int valor)
	{
		this.lblNewLabel.setText(String.valueOf(valor));

	}

	@Override
	public void addActionListener(ActionListener actionListener)
	{
		this.buttonDecrementa.addActionListener(actionListener);
		this.buttonIncrementa.addActionListener(actionListener);

	}

	public void keyPressed(KeyEvent e)
	{
	}

	public void keyReleased(KeyEvent e)
	{
		try
		{
			int h = Integer.parseInt(this.textField.getText());
			this.buttonDecrementa.setEnabled(true);
			this.buttonIncrementa.setEnabled(true);
		} catch (NumberFormatException exception)
		{
			this.buttonDecrementa.setEnabled(false);
			this.buttonIncrementa.setEnabled(false);

		}
	}

	public void keyTyped(KeyEvent e)
	{
	}

}
