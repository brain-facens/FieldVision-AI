#! /usr/bin/bash
IFS=' '
read -a strarr <<< "$@"
length=${#strarr[@]}

if !(( ${#strarr[@]} )); then
    echo Empty input...
    echo Leaving.
    exit
fi

phrases=""
for ((i=0; i<$length; i++))
do
    if [ $i -eq 0 ]; then
        phrases="${strarr[$i]}"

    else
        phrases="${phrases},${strarr[$i]}"

    fi
done

echo Filter words are: ${phrases[@]}

docker run -it --rm --name ocr-notas --privileged --net=host --env=NVIDIA_VISIBLE_DEVICES=all --env=NVIDIA_DRIVER_CAPABILITIES=all --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix -e PHRASES=$phrases brain20/ocr-notas:latest bash