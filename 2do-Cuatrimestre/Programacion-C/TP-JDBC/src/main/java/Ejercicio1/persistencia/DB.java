package Ejercicio1.persistencia;

import java.sql.*;

public class DB implements IPersistencia
{
    Connection conexion;
    Statement sentencia;
    ResultSet resultado;

    public DB() throws SQLException
    {

        conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/prueba1");
        sentencia = conexion.createStatement();
    }

    public ResultSet consulta(String sql) throws SQLException
    {
        resultado = sentencia.executeQuery(sql);
        return resultado;
    }

    @Override
    public void persistir()
    {

    }

    @Override
    public void insertar()
    {

    }

    @Override
    public void recuperar()
    {

    }
}
