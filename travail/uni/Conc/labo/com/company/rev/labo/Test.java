package com.company.rev.labo.source;

import com.company.rev.labo.source.Attempt1;
import com.company.rev.labo.source.Lock;
import com.company.rev.labo.source.MyThread;

public class Test{
    public static void main(String [] args) throws Exception {
	MyThread t[];
	int N = 2;
	Lock lock = new Attempt2(); //compléter avec un algorithme mutex
	t = new MyThread[N];
	for(int i=0; i<N; i++){
	    t[i] = new MyThread(i, lock);
	    t[i].start();
	}
    }
}
