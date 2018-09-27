#!/usr/bin/env bash

# TODO: move to `printf`
# TODO: add `diff`

echo -en "$(tput setaf 5)STATUS$(tput sgr0)\n"
git add -A
git status -s >&2

echo -en "$(tput setaf 5)LOG$(tput sgr0)\n"
git log --graph -n 3 --oneline --all --decorate >&2

echo -en "$(tput setaf 5)MSG$(tput sgr0)\n --> "
read msg
commit="$(git commit -m "$msg")"

echo -en "$(tput setaf 5)COMMIT$(tput sgr0)\n"
echo "${commit}"
git push
