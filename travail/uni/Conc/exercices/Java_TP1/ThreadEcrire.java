
public class ThreadEcrire{
  public static void main(String[] args) {
    Ecrire e1=new Ecrire("bonjour ",10);
    Ecrire e2=new Ecrire("bonsoir ",12);
    Ecrire e3=new Ecrire("\n ",5);

    e1.start();
    e2.start();
    e3.start();
    // c est pas dans l ordre ?! a part grand nb..
  }
}
