INSFOLDER=~/.edict
echo "If you are mac user, please use mac port"
echo "http://www.macports.org/"
echo "And download both python and pip"
echo "And don't forget set PATH for ~/bin/sh all wrapped bash script is there"

rm -Rf $INSFOLDER
rm -f ~/bin/sh/edict
mkdir -p ~/bin/sh
mkdir -p $INSFOLDER
cp *.py $INSFOLDER
cp edict ~/bin/sh
cp *.db $INSFOLDER

chmod -R 755 $INSFOLDER
chmod -R 755 ~/bin/sh