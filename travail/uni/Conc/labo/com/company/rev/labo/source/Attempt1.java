package com.company.rev.labo.source;

import java.util.concurrent.TimeUnit;

public class Attempt1 implements Lock {
    private boolean openDoor = true;

    public Attempt1() {
    }

    public void requestCS(int i) {
	while (!openDoor) ; // attente active
	openDoor = false; // verouille l’accès à la SC
    }

    public void releaseCS(int i) {
	openDoor = true; // libère l’accès à la SC
    }


}
