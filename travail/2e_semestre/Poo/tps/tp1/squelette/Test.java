class Test{ 
	public static void main(String[] args){ 
		int n= args.length;
		double[] notes= TP1Utils.str2double(args, n);

		TP1Utils.dispArr(notes, n);

		System.out.println("");

		double[] noteTrie= TP1Utils.triBulle(notes, n);

		System.out.println("Notes triées: ");
		TP1Utils.dispArr(noteTrie, n);
		
		System.out.println("");
		double med= TP1Utils.mediane(notes, n);
		System.out.println("Médiane: ");
		System.out.println(med);
	}
}
