public class Compteurb {
 private volatile int counter;

 public Compteurb(){
   this.counter=0;
 }

 public int getValue(){
   return counter;
 }

 public void increment(){
	int inter;
	inter = counter;
	try{
		Thread.sleep(1000);
	}catch(InterruptedException e){}
	counter = inter +1;
 }
}
