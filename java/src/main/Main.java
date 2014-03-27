package main;

import weka.Bayes_test;
import weka.Cluster_test;

public class Main {

    public static void main( String[] args ) {
        // TODO Auto-generated method stub

        /*
         * Exemple de deserialisation // Déserialisation des users depuis
         * users.csv Users_handling users_handling = new Users_handling(
         * "C:\\eclipse\\workspace\\datamining_TD\\lib\\users.csv" );
         * ArrayList<User> users = users_handling.giveUsers();
         * 
         * // Print des users System.out.println(
         * " ############### Unserialized users ###############" ); for ( User
         * user : users ) { user.print(); System.out.print( "\n" ); }
         * System.out.println(
         * " ################################################" );
         * 
         * // Déserialisation des movies depuis movies.csv Movies_handling
         * movies_handling = new Movies_handling(
         * "C:\\eclipse\\workspace\\datamining_TD\\lib\\movies.csv" );
         * ArrayList<Movie> movies = movies_handling.giveMovies();
         * 
         * // Print des movies System.out.println(
         * " ############### Unserialized movies ###############" ); for ( Movie
         * movie : movies ) { movie.print(); System.out.print( "\n" ); }
         * System.out.println(
         * " ################################################" );
         */

        /* Test exemple de Yanlin */
        System.out.println( "Test de clustering des iris \n" );
        Cluster_test myTest = new Cluster_test();
        myTest.test();

        System.out.println( "Test de classification de Bayes des matches de foot \n" );
        Bayes_test mySecondTest = new Bayes_test();
        mySecondTest.test( "C:\\eclipse\\workspace\\datamining_TD\\lib\\weather.nominal.arff" );

        System.out.println( "Test de classification de Bayes des notes de films \n" );
        Bayes_test myThirdTest = new Bayes_test();
        mySecondTest.test( "C:\\eclipse\\workspace\\datamining_TD\\lib\\ratings.arff" );

    }

}
