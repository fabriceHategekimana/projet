package com.company.rev.philosophes;

public class Philosopher implements Runnable{
    	int id = 0;
	Ressource r = null;

	public Philosopher(int initId, Resource initr){
	    id = initId;
	    r = initr;
	}	

	public void run() {
	    while(true) {
		try {
		    System.out.println(“ Philosophe “ + id + “ pense”);
		    Thread.sleep(30);
		    System.out.println(“ Philosophe “ + id + “ a faim”);
		    r.acquire(id); // acquisition des resources critiques
		    System.out.println(“ Philosophe “ + id + “ mange”);
		    Thread.sleep(40);
		    r.release(id); // libère les resources
		} catch (InterruptedException e) { return;}
	    }
	}
}

}
