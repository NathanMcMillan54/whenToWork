#!/usr/bin/env bash

echo "Moving bin/whenToWork.sh..."
mv bin/whenToWork ../

# this should make ../../whenToWork_app.sh run when you just click on it
chmod u+x ../../whenToWork_app.sh
