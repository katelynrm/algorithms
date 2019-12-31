

def intersection_area(rect1, rect2):
    rect1_x, rect1_y = [tup[0] for tup in rect1], [tup[1] for tup in rect1]
    rect2_x, rect2_y = [tup[0] for tup in rect2], [tup[1] for tup in rect2]
    
    rect1_xs = (min(rect1_x), max(rect1_x))
    rect1_ys = (min(rect1_y), max(rect1_y))
    rect2_xs = (min(rect2_x), max(rect2_x))
    rect2_ys = (min(rect2_y), max(rect2_y))

    if rect1_xs[0] >= rect2_xs[0] and rect1_xs[0] <=rect2_xs[1]:
        width = rect2_xs[1] - rect1_xs[0]
    else:
        width = rect1_xs[1] - rect2_xs[0]

    if rect1_ys[1] >= rect2_ys[0] and rect1_ys[1] <=rect2_ys[1]:
        length = rect1_ys[1] - rect2_ys[0]
    else:
        length = rect2_ys[1] - rect1_ys[0]
    return width * length 


rec1 = [(3,3),(3,1),(6,1),(6,3)]

rec2 = [(1,4),(1,1),(4,1),(4,4)]

print(intersection_area(rec1, rec2))

