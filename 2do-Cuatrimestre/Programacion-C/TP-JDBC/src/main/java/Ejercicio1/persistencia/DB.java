package Ejercicio1.persistencia;

import Ejercicio1.modelo.Cliente;
import Ejercicio1.modelo.Mascota;

import java.sql.*;
import java.util.ArrayList;

public class DB implements IPersistencia
{
    Connection conexion;
    Statement sentencia;
    ResultSet resultado;

    public  DB() throws SQLException
    {

        conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/veterinaria","root","");
        sentencia = conexion.createStatement();
    }

    public ResultSet consulta(String sql) throws SQLException
    {
        this.resultado = this.sentencia.executeQuery(sql);
        return this.resultado;
    }


    @Override
    public ArrayList<ClienteDTO> getClientes()
    {
        ArrayList<ClienteDTO> clientes = new ArrayList<>();
        try{
            this.resultado = this.sentencia.executeQuery("SELECT * FROM clientes");
            while(this.resultado.next()){
                ClienteDTO c = new ClienteDTO();
                c.setId(this.resultado.getInt("cliente_id"));
                c.setNombre(this.resultado.getString("nombre"));
                c.setDireccion(this.resultado.getString("direccion"));
                c.setTelefono(this.resultado.getString("telefono"));
                clientes.add(c);
            }
        }catch (SQLException e){
            e.printStackTrace();
        }
        return clientes;
    }

    @Override
    public void insertarMascota()
    {

    }

    @Override
    public void insertarCliente()
    {

    }

    @Override
    public void insertarPracticaVeterinaria()
    {

    }

    @Override
    public ArrayList<MascotaDTO> getMascotasCliente(ClienteDTO c)
    {
        ArrayList<MascotaDTO> mascotas = new ArrayList<>();
        PreparedStatement sentencia = null;
        System.out.println("ID CLIENTE: " + c.getId());
        try{
            sentencia = conexion.prepareStatement("SELECT * FROM mascotas WHERE cliente_id = ?");
            sentencia.setInt(1, c.getId());
            ResultSet res= sentencia.executeQuery();
            while(res.next()){
                MascotaDTO m = new MascotaDTO();
                m.setId(res.getInt("mascota_id"));
                m.setFechaNacimiento(res.getDate("fechaNacimiento"));
                m.setHistoriaClinica(res.getString("historiaClinica"));
                m.setNombre(res.getString("nombre"));
                m.setAnimal(res.getString("animal"));
                m.setIdCliente(res.getInt("cliente_id"));

                mascotas.add(m);
            }
        }catch (Exception e){

        }
        return mascotas;
    }

    @Override
    public void getPracticasVeterinarias(MascotaDTO m)
    {

    }

    @Override
    public void getMascotasPorTipo(String tipo)
    {

    }

    @Override
    public void getMascota(String historiaClinica)
    {

    }
}
