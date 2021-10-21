def classPhotos(redShirtHeights, blueShirtHeights):
    """
    You're given two input arrays: one containing the heights of all the students with red shirts
    and another one containing the heights of all the students with blue shirts.
    These arrays will always have the same length, and each height will be a positive integer.
    Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.
    Note: you can assume that each class has at least 2 students.
    """
    # O(N) time, where n is total number of shirts
    # O(1) space,
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    first_row_color = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]
        if first_row_color == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True

