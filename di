#!/usr/bin/env bash

# stage everything
echo -en "\n"
echo -en "$(tput setaf 5)🚚  - STAGED FILES$(tput sgr0)\n"
echo -en "\n"
git add -A
git status -s >&2

# show some recent commtis for context
echo -en "\n"
echo -en "$(tput setaf 5)📝  - RECENT COMMITS$(tput sgr0)\n"
echo -en "\n"
git log --graph -n 3 --oneline --all --decorate >&2

# take user input for commit msg
echo -en "\n"
echo -en "$(tput setaf 5)✏️  - COMMIT MSG$(tput sgr0)\n --> "
read msg
commit="$(git commit -m "$msg")"

# display commit
echo -en "\n"
echo -en "$(tput setaf 5)✅  - COMMIT SUCCESSFUL!$(tput sgr0)\n"
echo -en "\n"
echo "${commit}"
