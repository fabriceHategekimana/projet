package com.company.rev.labo.source;

import java.util.Random;

public class MyThread extends Thread {
    int myId; Lock lock; Random r= new Random();
    public MyThread(int id, Lock lock) {
	myId = id;
	// chaque processus possède une identité propre
	this.lock = lock; // les processus utilisent le même verrou pour accéder la SC
    }
    void nonCriticalSection() {
	System.out.println(myId + " n’est pas en SC ");
	mySleep(r.nextInt(1000));
    }

    void CriticalSection() {
	System.out.println(myId + " est en SC ");
	mySleep(r.nextInt(1000));
    }

    public static void  mySleep(int time)
    { 
	try {
	    Thread.sleep( time );
	} catch (InterruptedException e) {} // le bloc try est imposé par sleep(t)
    }
}
