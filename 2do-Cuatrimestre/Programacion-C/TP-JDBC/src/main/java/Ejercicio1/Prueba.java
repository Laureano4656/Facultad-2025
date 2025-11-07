package Ejercicio1;

import Ejercicio1.persistencia.DB;

public class Prueba
{
    public static void main(String[] args)
    {
        try{
            Class.forName("java.sql.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        try{
        DB db = new DB();

        }catch(Exception e){
            System.out.println(e);
            System.exit(0);
        }
    }
}
