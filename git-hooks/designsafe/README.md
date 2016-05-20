# Git hooks for designsafe

## Installation

Move files into `$PORTAL_PROJECT_PATH/.git/hooks`

## pre-commit

Will fire up every time you commit some files i.e. `git commit -m "Some commit message"`

Checks `.py` and `.js` files that are being committed for `ipdb.set_trace`, `console.log` and `<<<<<<<`.
If any of these strings are in the files then it does not commit anything an exits with a `1`.


## pre-push

Will fire up every time you push something to **any** branch i.e. `git push`

Run necessary tests, if not all the tests are passed then it does not push anything.

To property confgiure change the first line from `eval "$(docker-machine env dev)"`
to your docker-machine name and change the value of `TEST_CMD` if necessary.
