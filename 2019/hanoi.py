## Towers of Hanoi. 3 Towers, A, B, C. We're going to move it from A -> B

def hanoi(source, dest, aux, height): ## 1 = top. Counting down
    if(height >= 1):
        hanoi(source, aux, dest, height -1)
        print("MOVE {} FROM {} TO {}".format('*'*height,source, dest))
        hanoi(aux, dest, source, height -1)

hanoi('A', 'B', 'C', 3)