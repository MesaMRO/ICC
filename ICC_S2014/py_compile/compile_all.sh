for f in *.tex
do
    pdflatex -output-directory output $f
done

cd output
rm *.aux *.log
