
while [ 1 ]
do
    sleep 2
    clear
    cowsay -W 60 Bienvenue à la conférence Vi/Vim!
    sleep 2
    clear
    dans=$(task calc now - 2021-02-18T18:00:00  | sed -e "s/M-/ Minutes et /" | sed -e "s/H-/ Heures et /" | sed -e "s/S/ Secondes/" | sed -e "s/PT-//")
    cowsay -W 60 La conférence commence dans $dans
    sleep 3
    clear
    cowsay -W 60 Un peu de patience
done

