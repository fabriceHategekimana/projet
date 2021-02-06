package com.company.rev.labo.source;

public interface Lock
// voir l’interface Runnable pour l’utilisation
{
    public void requestCS(int pid); // requête pour entrer en SC
    public void releaseCS(int pid); // indique que le thread quitte la SC
}
