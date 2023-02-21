#Points from the question.
win = 6
lose = 0
draw = 3

rock = 1
paper = 2
scissors = 3

#column1 a= rock, b= paper, c= scissors
#column2 x = rock, y= paper, z= scissors
total = 0
points = []

#Using with statement to open the file and loop over it.
with open("input.txt", "r") as file:
    for f in file: 
        split = f.split() 
        

        #Using match statement to compare all cases/combinations of the game. 
        match split: 
            case ["A", "Z"]:
                total = lose + scissors

            case ["A", "X"]:
                total = draw + rock

            case ["A", "Y"]:
                total = win + paper

            case ["B", "X"]:
                total = lose + rock

            case ["B", "Y"]:
                total = draw + paper

            case ["B", "Z"]:
                total = win + scissors

            case ["C", "Y"]:
                total = lose + paper

            case ["C", "Z"]:
                total = draw + scissors

            case ["C", "X"]:
                total = win + rock
        
        #Appending the output of total to points.
        points.append(total)


#Getting the sum of a list of integers.
print(sum(points))

       


