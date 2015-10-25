#!/bin/bash

watchify -t babelify YmirCharacterEdit.js -o dist/YmirCharacterEdit.js &
watchify -t babelify YmirCharacter.js -o dist/YmirCharacter.js &
watchify -t babelify YmirOverview.js -o dist/YmirOverview.js &
watchify -t babelify YmirSearch.js -o dist/YmirSearch.js &
watchify -t babelify YmirWorldList.js -o dist/YmirWorldList.js &
