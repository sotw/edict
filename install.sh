INSFOLDER=~/.edict
FULL_INSTALL=false

while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--full)
            FULL_INSTALL=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

if [ "$FULL_INSTALL" = true ]; then
    echo "Full installation (including database)..."
    rm -Rf $INSFOLDER
else
    echo "Updating code files only (database preserved)..."
fi

mkdir -p ~/bin/sh
mkdir -p $INSFOLDER

cp -vf *.py $INSFOLDER
cp -vf edict ~/bin/sh

if [ "$FULL_INSTALL" = true ]; then
    cp -vf *.db $INSFOLDER
fi

chmod -R 755 $INSFOLDER
chmod -R 755 ~/bin/sh

if [ ! -d "$INSFOLDER/venv" ]; then
    python3 -m venv "$INSFOLDER/venv"
    source "$INSFOLDER/venv/bin/activate"
    pip install beautifulsoup4 openai
fi

echo "Done!"
