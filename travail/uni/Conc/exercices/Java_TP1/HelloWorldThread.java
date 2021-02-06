public class HelloWorldThread extends Thread {
	public void run() {
		System.out.println("Hello, world "+Thread.currentThread().getName());
	}
	
	public static void main(String[] args) {
		HelloWorldThread t = new HelloWorldThread();
		t.start();
		System.out.println("Hello, world "+Thread.currentThread().getName());
		
	}
}
