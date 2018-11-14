# clear old results
> results.txt

# print new results

python3 -m BackTracking.Driver 5x5maze.txt None False
python3 -m BackTracking.Driver 5x5maze.txt None True
python3 -m BackTracking.Driver 5x5maze.txt Constrained False
python3 -m BackTracking.Driver 5x5maze.txt Constrained True
python3 -m BackTracking.Driver 5x5maze.txt Adjacent False
python3 -m BackTracking.Driver 5x5maze.txt Adjacent True
printf "\n***********************************\n" >> results.txt

python3 -m BackTracking.Driver 7x7maze.txt None False
python3 -m BackTracking.Driver 7x7maze.txt None True
python3 -m BackTracking.Driver 7x7maze.txt Constrained False
python3 -m BackTracking.Driver 7x7maze.txt Constrained True
python3 -m BackTracking.Driver 7x7maze.txt Adjacent False
python3 -m BackTracking.Driver 7x7maze.txt Adjacent True
printf "\n***********************************\n" >> results.txt

python3 -m BackTracking.Driver 8x8maze.txt None False
python3 -m BackTracking.Driver 8x8maze.txt None True
python3 -m BackTracking.Driver 8x8maze.txt Constrained False
python3 -m BackTracking.Driver 8x8maze.txt Constrained True
python3 -m BackTracking.Driver 8x8maze.txt Adjacent False
python3 -m BackTracking.Driver 8x8maze.txt Adjacent True
printf "\n***********************************\n" >> results.txt


#python3 -m BackTracking.Driver 9x9maze.txt None False
#python3 -m BackTracking.Driver 9x9maze.txt None True
python3 -m BackTracking.Driver 9x9maze.txt Constrained False
python3 -m BackTracking.Driver 9x9maze.txt Constrained True
#python3 -m BackTracking.Driver 9x9maze.txt Adjacent False
#python3 -m BackTracking.Driver 9x9maze.txt Adjacent True
printf "\n***********************************\n" >> results.txt

# python -m BackTracking.Driver 10x10maze.txt None False
# python -m BackTracking.Driver 10x10maze.txt None True
# python -m BackTracking.Driver 10x10maze.txt Constrained False
# python -m BackTracking.Driver 10x10maze.txt Constrained True
# python -m BackTracking.Driver 10x10maze.txt Adjacent False
python3 -m BackTracking.Driver 10x10maze.txt Adjacent True
printf "\n***********************************\n" >> results.txt
