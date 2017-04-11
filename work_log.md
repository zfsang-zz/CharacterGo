# Work Log

## Day 3

With Ivan's help, my solution to solve the coreference of character name is much faster.  Particularly, the replacing pronoun by real 
Get the first unsupervised model going.

## Day 4

unicode normalizer on accent 
add support for 'veryPostive' 'veryNegative'
tmux is working

## Day 5
figure out pipeline to process all the data (using shell script, cd )

## Day 6
Did not do much work today

## Day 7
Parse all summary docs through pipeline

## Day 8
try to install textacy with no luck on AWS (painful process to configure gcc,other dependency)
manually clean up the label data I got

## Day 9
Match label with the text
Get the first supervised model running: LinearSVC
Work on the full text, get a lot of false positive NER

### Questiones



### Notes

tmux

tmux detach (or ctrl + b then d)  tmux ls
tmux list-sessions


tmux attach
tmux attach -t 0
tmux kill-session -t 0


http://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session