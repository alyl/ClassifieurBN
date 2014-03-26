package files_handling;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import beans.User;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

/* Classe de handlers de fichiers json au format de users.csv */
public class Users_handling {

    private String path;

    /* Constructeur mentionant le chemin vers le fichier Json à parser */
    public Users_handling( String path ) {
        this.path = path;
    }

    /* méthode renvoyant la liste des User correspondants au fichier Json */
    public ArrayList<User> giveUsers() {

        ArrayList<User> users = new ArrayList<User>();

        try {
            BufferedReader reader = new BufferedReader( new FileReader( new
                    File( this.path ) ) );
            System.out.println( "Source File opened successfully" );

            try {
                for ( String line = reader.readLine(); line != null; line = reader.readLine() ) {

                    Gson gson = new GsonBuilder().create();
                    User user = gson.fromJson( line, User.class );
                    users.add( user );
                }
                reader.close();

            } catch ( IOException e ) {
                System.out.println( "An error occured during the Json parsing : " );
                e.printStackTrace();
            }

        } catch ( FileNotFoundException e ) {
            e.printStackTrace();
        }
        return users;
    }
}
