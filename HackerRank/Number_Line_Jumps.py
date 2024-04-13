def kangaroo(x1, v1, x2, v2):
    # If both kangaroos start at the same position with the same speed, they will meet
    if x1 == x2 and v1 == v2:
        return "YES"
    # If both kangaroos have the same speed but different starting positions, they will never meet
    elif v1 == v2:
        return "NO"
    else:
        # If one kangaroo starts ahead of the other and has a greater speed, they will never meet
        if (x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2):
            return "NO"
        else:
            # Check if the kangaroos will meet after a finite number of jumps
            while True:
                # Update the positions of both kangaroos after one jump
                x1 += v1
                x2 += v2
                # If they meet at the same position, return "YES"
                if x1 == x2:
                    return "YES"
                # If one kangaroo passes the other without meeting, return "NO"
                elif (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1):
                    return "NO"
