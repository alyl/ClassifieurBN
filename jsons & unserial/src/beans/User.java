package beans;

import java.util.Map;

public class User {

    private int           id;
    private int           age;
    private String        sex;
    private String        job;
    private int           zipcode; // une dizaine de zipcodes étaient des
                                   // String. Ils apparaissent comme 0 dans mes
                                   // csv.
    Map<Integer, Integer> ratings; // clé : id du film auquel la note a été
                                   // attribuée, valeur : valeur de la note

    /* Printer */
    public void print() {
        System.out.println( "UserPrint : " );
        System.out.println( "id = " + this.id );
        System.out.println( "age = " + this.age );
        System.out.println( "sex = " + this.sex );
        System.out.println( "job = " + this.job );
        System.out.println( "zipcode = " + this.zipcode );

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

    public int getAge() {
        return age;
    }

    public void setAge( int age ) {
        this.age = age;
    }

    public String getSex() {
        return sex;
    }

    public void setSex( String sex ) {
        this.sex = sex;
    }

    public String getJob() {
        return job;
    }

    public void setJob( String job ) {
        this.job = job;
    }

    public int getZipcode() {
        return zipcode;
    }

    public void setZipcode( int zipcode ) {
        this.zipcode = zipcode;
    }

    public void setRatings( Map<Integer, Integer> ratings ) {
        this.ratings = ratings;
    }

    public Map<Integer, Integer> getRatings() {
        return ratings;
    }
}