public class Compteur {
 private volatile int counter;

 public Compteur(){
   this.counter=0;
 }

 public int getValue(){
   return counter;
 }

 public void increment(){
   counter= counter + 1;
 }
}
