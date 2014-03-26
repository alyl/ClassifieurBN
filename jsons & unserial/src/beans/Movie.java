package beans;

import java.util.ArrayList;
import java.util.Map;

public class Movie {

    private int                id;
    private int                timestamp;
    private ArrayList<Integer> style;    // tableau de 0 et de 1 identifiant le
                                          // style
    Map<Integer, Integer>      ratings;  // clé : id de l'utilisateur qui a
                                          // attribué la note, valeur : valeur
                                          // de la note

    /* Printer */
    public void print() {
        System.out.println( "MoviePrint : " );
        System.out.println( "id = " + this.id );
        System.out.println( "timestamp = " + this.timestamp );
        System.out.println( "style = " + this.style );
        System.out.print( "ratings = { \n" );
        for ( Integer key : ratings.keySet() )
        {
            System.out.print( "key = " + key + ", " + "value = " + ratings.get(
                    key ) + "\n" );
        }
        System.out.println( "}" );
    }

    /* Getters & setters */

    public int getId() {
        return id;
    }

    public void setId( int id ) {
        this.id = id;
    }

    public int getTimestamp() {
        return timestamp;
    }

    public void setTimestamp( int timestamp ) {
        this.timestamp = timestamp;
    }

    public ArrayList<Integer> getStyle() {
        return style;
    }

    public void setStyle( ArrayList<Integer> style ) {
        this.style = style;
    }

    public Map<Integer, Integer> getRatings() {
        return ratings;
    }

    public void setRatings( Map<Integer, Integer> ratings ) {
        this.ratings = ratings;
    }

}