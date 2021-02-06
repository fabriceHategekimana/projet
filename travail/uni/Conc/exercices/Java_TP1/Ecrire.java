import java.lang.Thread;
import java.util.Random;

// Threads with random sleep
public class Ecrire extends Thread{
  private String text;
  private int nb;

  public Ecrire(String text, int nb){ // constructeur
    this.text=text;
    this.nb=nb;
  }

  public void run(){
    Random r=new Random();

    try{
      for(int i=0; i < nb; i++){
        print(text);
        //System.out.print(text);
        sleep(r.nextInt(10));
        /*
        The nextInt(int n) method is used to get a pseudorandom,
        uniformly distributed int value between 0 (inclusive)
        and the specified value (exclusive), drawn from this random
        number generator's sequence.
        */
      }
    }
    catch (InterruptedException e) {}
  }

  public void print(String text){
    for(int j=0; j < text.length() ;j++){
      System.out.print(text.charAt(j));
    }

  }

}
/*
bo
 bonjnsoir our
 bonjour bonjour bonjour bonsoir bonsoir
 bonjour bonsoir bonsoir bonjour bonsoi
 r
 bonjour bonsoir bonjour bonsoir bonjour bonsoir bonjour bonsoir bonsoir bonsoir


*/
