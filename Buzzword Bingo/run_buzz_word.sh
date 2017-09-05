export LD_LIBRARY_PATH=/usr/local/lib
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
pocketsphinx_continuous -inmic yes -kws ~/buzz_words.txt -logfn log.log | while read line
do
    echo $line
    sudo python usb_on.py
done

#grep buzzword |
