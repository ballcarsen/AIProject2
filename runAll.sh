# clear old results
> results.txt

# print new results

python -m BackTracking.Driver 5x5maze.txt False False
python -m BackTracking.Driver 5x5maze.txt False True
python -m BackTracking.Driver 5x5maze.txt True False
python -m BackTracking.Driver 5x5maze.txt True True
printf "\n***********************************\n" >> results.txt

python -m BackTracking.Driver 7x7maze.txt False False
python -m BackTracking.Driver 7x7maze.txt False True
python -m BackTracking.Driver 7x7maze.txt True False
python -m BackTracking.Driver 7x7maze.txt True True
printf "\n***********************************\n" >> results.txt

python -m BackTracking.Driver 8x8maze.txt False False
python -m BackTracking.Driver 8x8maze.txt False True
python -m BackTracking.Driver 8x8maze.txt True False
python -m BackTracking.Driver 8x8maze.txt True True
printf "\n***********************************\n" >> results.txt

python -m BackTracking.Driver 9x9maze.txt False False
python -m BackTracking.Driver 9x9maze.txt False True
python -m BackTracking.Driver 9x9maze.txt True True
printf "\n***********************************\n" >> results.txt
