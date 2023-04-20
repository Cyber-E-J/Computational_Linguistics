for file in *.wav; do sox "$file" "48khz_$file" -r 48000; done

