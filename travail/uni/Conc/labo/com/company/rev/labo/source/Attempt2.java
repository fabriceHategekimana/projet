package com.company.rev.labo.source;

public class Attempt2 implements Lock {
    private boolean wantCS[] = {false, false};

    public void requestCS(int i) {
	wantCS[i] = true;
	// resèrve l’accès à la SC
	while (wantCS[1-i]); // attente active si le second processus en SC
    }

    public void releaseCS(int i) {
	wantCS[i] = false;
    }
}
