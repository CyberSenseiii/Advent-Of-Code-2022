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


with open("input.txt", "r") as file:
    for f in file: 
        split = f.split() 
        

        #Match statement to compare all cases/combinations of the game. 
        #Replace function to access individual characters and replacing them for the desired outcome. 
        match split: 
            case ["A", "Z"]:
                f.replace(f[2], "Y")
                total = win + paper

            case ["A", "X"]:
                f.replace(f[2], "Z")
                total = lose + scissors

            case ["A", "Y"]:
                f.replace(f[2], "X")
                total = draw + rock

            case ["B", "X"]:
                total = lose + rock

            case ["B", "Y"]:
                total = draw + paper

            case ["B", "Z"]:
                total = win + scissors

            case ["C", "Y"]:
                f.replace(f[2], "Z")
                total = draw + scissors

            case ["C", "Z"]:
                f.replace(f[2], "X")
                total = win + rock

            case ["C", "X"]:
                f.replace(f[2], "Y")
                total = lose + paper
        
        #Appending the output of total to points.
        points.append(total)
       


#Getting the sum of a list of integers.
print(sum(points))

