package weka;

import java.io.BufferedReader;
import java.io.FileReader;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.core.Instances;

public class Bayes_test {

    public static void test( String path ) {
        try {
            // permet de charger un ensemble d?exemples
            BufferedReader reader = new BufferedReader( new FileReader( path ) );
            Instances data = new Instances( reader );
            data.setClassIndex( 0 );
            reader.close();

            Classifier cModel = (Classifier) new NaiveBayes();
            cModel.buildClassifier( data );

            // set the options
            // build the clusterer

            Evaluation eTest = new Evaluation( data );
            eTest.evaluateModel( cModel, data );

            String strSummary = eTest.toSummaryString();

            // Get the confusion matrix
            double[][] cmMatrix = eTest.confusionMatrix();

            System.out.println( " summary : " + strSummary );
            System.out.println( "\n confusion matrix : " + cmMatrix );

        }

        catch ( Exception e1 ) {
            System.out.println( e1.getMessage() );
        }
    }
}
