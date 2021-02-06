public class compteurStatic extends Thread{
	static volatile int val=0;

	public void run(){
		while(true){
			incremente();
			System.out.println("Thread "+Thread.currentThread().getName()+"  "+getValue());
		}
	}
	 void incremente() {
	int inter = val;
	try{
		Thread.sleep(1000);
	}catch(InterruptedException e){}
	val=inter+1;
}
 	int getValue() {
	return val;
}
}
