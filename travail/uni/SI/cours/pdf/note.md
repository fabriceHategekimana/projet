# Les démons
Pour crééer un démon il faut
1. fork();
2. créer une nouvelle session et se déconnecter du terminal (setsid)
3. changer/sécuriser son répertoire de travail (chdir/chroot)
4. ajuster les droits d'utilisateur (setuid)
5. changer les droits de fichier (umask)

Session (SID= session ID)
processus maître de session (shell de login ou session graphique)

RUID, EUID

