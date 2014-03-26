package main;

import java.util.ArrayList;

import beans.Movie;
import beans.User;
import files_handling.Movies_handling;
import files_handling.Users_handling;

public class Main {

    public static void main( String[] args ) {
        // TODO Auto-generated method stub

        // Déserialisation des users depuis users.csv
        Users_handling users_handling = new Users_handling( "C:\\eclipse\\workspace\\datamining_TD\\lib\\users.csv" );
        ArrayList<User> users = users_handling.giveUsers();

        // Print des users
        System.out.println( " ############### Unserialized users ###############" );
        for ( User user : users ) {
            user.print();
            System.out.print( "\n" );
        }
        System.out.println( " ################################################" );

        // Déserialisation des movies depuis movies.csv
        Movies_handling movies_handling = new Movies_handling( "C:\\eclipse\\workspace\\datamining_TD\\lib\\movies.csv" );
        ArrayList<Movie> movies = movies_handling.giveMovies();

        // Print des movies
        System.out.println( " ############### Unserialized movies ###############" );
        for ( Movie movie : movies ) {
            movie.print();
            System.out.print( "\n" );
        }
        System.out.println( " ################################################" );
    }

}
