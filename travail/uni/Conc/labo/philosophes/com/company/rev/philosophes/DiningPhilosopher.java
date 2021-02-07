class DiningPhilosopher implements Ressource {
    int n = 0;
    BinarySemaphore[] fork = null;
    public DiningPhilosopher(int initN) {
	n = initN; // nombre de philosophes
	fork = new BinarySemaphore[n];
	for (int i = 0; i < n; i++) {
	    fork[i] = new BinarySemaphore(true); // les ressources sont
	    // initialement accessibles
	}
    }
}
