INSFOLDER=~/.edict
echo "If you are mac user, please use mac port"
echo "http://www.macports.org/"
echo "And download both python and pip"
echo "And don't forget set PATH for ~/bin/sh all wrapped bash script is there"
rm -Rf $INSFOLDER
rm -f ~/bin/sh/edict
mkdir -p ~/bin/sh
mkdir -p $INSFOLDER
cp -vf *.py $INSFOLDER
cp -vf edict ~/bin/sh
cp -vf *.db $INSFOLDER


chmod -R 755 $INSFOLDER
chmod -R 755 ~/bin/sh

echo "Do you want to add PATH envirnment in .bashrc?(restart terminal will effect at once)"
select yn in "Yes" "No"; do
	case $yn in
		Yes ) echo "PATH=$PATH:~/bin/sh:~/bin" > ~/.bashrc; break;;
	    No ) google have a nice day; break;;
	esac
done
echo "This utility depends on beautifulsoup 4"
echo "in case you use ubuntu 20.04 LTS launch sodo apt install python3-bs4"
