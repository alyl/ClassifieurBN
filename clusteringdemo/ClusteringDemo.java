package clusteringdemo;

import weka.core.Instances;
import java.io.BufferedReader;
import java.io.FileReader;
import weka.clusterers.*;
import weka.clusterers.ClusterEvaluation;

public class ClusteringDemo{

    public static void main(String[] args){
		try{
			// permet de charger un ensemble d?exemples
			BufferedReader reader = new BufferedReader(new FileReader("./iris.arff"));
			Instances data = new Instances(reader);
			reader.close();

			String [] options = new String [2];
			options[0] = "-I"; // max. 
			options[1] = "100";
			EM clusterer = new EM(); // new instance of clusterer

			clusterer.setOptions(options);
			clusterer.buildClusterer(data);
			// set the options
			// build the clusterer

			ClusterEvaluation eval = new ClusterEvaluation ();
			eval.setClusterer(clusterer);
			eval.evaluateClusterer(data);

			System.out.println("# of clusters: " + eval.getNumClusters()); // output # of clusters 
		}

		catch(Exception e1){
			System.out.println(e1.getMessage());
		} 
	}
}

