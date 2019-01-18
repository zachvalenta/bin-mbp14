# OVERVIEW

a congeries of Bash utils

# USEFUL TO YOU (MAYBE)

* `fne` ('file name editor'): CLI for file edits using argparse ✂️
* `qing` ('清'): wrapper around `send2trash` ♻️

# USEFUL TO ME (ONLY)

__daily workflow__

* `shui` (水): start the day
* `jb` (进步): `git s` on `notes` dir
* `jz` (节奏): checkpoint to keep myself on track
* `js` (结束): end the day

__projects__

* `flash`: setup - project on Flash Boys 🏦
* `suan` ('算'): setup - 'Grokking Algorithms'

__hobbies__

* `dance`: setup - dance 💃🏼
* `music`: setup - dance 🎹
* `viz`: setup - visual art ✒️

__misc__

* `kcm` ('kill cmus'): cmus doesn't play well with Bluetooth and I frequently need to kill the process 😑
* `yoga`: setup - yoga

# TODO

* _monthly_: script to tally + charts w/ [dataset](https://dataset.readthedocs.io/en/latest/index.html) and [termgraph](https://github.com/mkaz/termgraph)
* `qiu`: fix bug w/ `argparse`; can only do `?k1=v1`, not `?k1=v1&k2=v2`
* `jb`: fix overlap btw 'deleted' and 'added'
* `bash_profile.pysave`?
* clean `.bash_profile`

## ding

- [ ] bug - normal Bash navigational shortcuts fail during commit msg input
- [ ] move to `printf`
- [ ] new line after each
- [ ] `-h` (like argparse)
- [ ] fix input glitch (cannot backspace, use normal Bash shortcuts)
- [ ] move to own repo, [laziestgit](https://github.com/jesseduffield/lazygit) --> "n.b.: This is a work in-progress. When you break it, let me know!"

## fne

- [ ] actually allow re-doing args
- [ ] file extension - if no flag, assume `.mp3`, optional args for `.mp4` and `.pdf` (for language-learning audio files)
- [ ] Pathlib's `.extension()` http://blog.danwin.com/using-python-3-pathlib-for-managing-filenames-and-directories/
- [ ] regex - lowercase
- [ ] regex - kebab case

## jb

- [ ] filter out anything that hasn't changed by more than 50 lines

## za

- [ ] script for month end tally
- [ ] `mkd` but for cd into repo immediately after `git clone`
- [ ] `qiu`: defaults for port/path
- [ ] `kcm`: `psutil`?
- [ ] dictionary pronunciation CLI https://dictionaryapi.com/info/faq-audio-image#collegiate
- [ ] `py-wiki`: Py version of [wikit](https://www.npmjs.com/package/wikit)
