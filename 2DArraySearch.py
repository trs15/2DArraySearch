#params: board: a 2d array representation of the game board, boardSize: integer size of the board, light, dark, blank: integer representation of pieces
#returns: dict with keys of light and dark with boolean values of their playable status
def _search(board, boardSize, light, dark, blank):
    darkPlayable = False
    lightPlayable = False

    for y in range(0, boardSize-1):
        for x in range(0, boardSize-1):
            position = int(board[y][x])
            if((position == light and lightPlayable is False) or (position == dark and darkPlayable is False)):
                if(y == 0):
                    if(x == 0):
                        if(searchSouth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                    elif(x == boardSize-1):
                        if(searchSouth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                    else:
                        if(searchEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                    
                elif(y == boardSize-1):
                    if(x == 0):
                        if(searchSouth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                    elif(x == boardSize-1):
                        if(searchNorth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchNorthWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                    else:
                        if(searchNorth(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchNorthEast(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue
                        if(searchNorthWest(board, boardSize, blank, x, y) > 0):
                            if(position == light):
                                lightPlayable = True
                            if(position == dark):
                                darkPlayable = True
                            continue

                    if(searchNorth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
            
                elif(x == 0):
                    if(searchNorth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    
                elif(x == boardSize-1):
                    if(searchSouth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouthWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                
                else:
                    if(searchNorth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouth(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchNorthWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouthEast(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue
                    if(searchSouthWest(board, boardSize, blank, x, y) > 0):
                        if(position == light):
                            lightPlayable = True
                        if(position == dark):
                            darkPlayable = True
                        continue

    return {"light":lightPlayable, "dark":darkPlayable}            
                    
def searchNorth(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y > 0):
        distance = distance + 1
        y = y - 1
        current = board[y][x]
        if(current == piece):
            return 0
    
    if(distance == 1 or (y == 0 and current != blank)):
        return 0

    return distance
        
def searchSouth(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y <= size-2):
        distance = distance + 1
        y = y + 1
        current = board[y][x]
        if(current == piece):
            return 0
    
    if(distance == 1 or (y == size-1 and current != blank)):
        return 0
    
    return distance

def searchEast(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and x <= size-2):
        distance = distance + 1
        x = x + 1
        current = board[y][x]
        if(current == piece):
            return 0

    if(distance == 1 or (x == size-1 and current != blank)):
        return 0
        
    return distance

def searchWest(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and x > 0):
        distance = distance + 1
        x = x - 1
        current = board[y][x]
        if(current == piece):
            return 0

    if(distance == 1 or (x == 0 and current != blank)):
        return 0
        
    return distance

def searchNorthEast(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y > 0 and x <= size-2):
        distance = distance + 1
        y = y - 1
        x = x + 1
        current = board[y][x]
        if(current == piece):
            return 0
    
    if(distance == 1 or ((y == 0 or x == size-1) and current != blank)):
        return 0

    return distance

def searchNorthWest(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y > 0 and x > 0):
        distance = distance + 1
        y = y - 1
        x = x - 1
        current = board[y][x]
        if(current == piece):
            return 0
    
    if(distance == 1 or ((y == 0 or x == 0) and current != blank)):
        return 0
        
    return distance

def searchSouthEast(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y <= size-2 and x <= size-2):
        distance = distance + 1
        y = y + 1
        x = x + 1
        current = board[y][x]
        if(current == piece):
            return 0
    
    if(distance == 1 or ((y == size-1 or x == size-1) and current != blank)):
        return 0
        
    return distance
        
def searchSouthWest(board, size, blank, x, y):
    current = board[y][x]
    piece = board[y][x]
    distance = 0
    while(current != blank and y <= size-2 and x > 0):
        distance = distance + 1
        y = y + 1
        x = x - 1
        current = board[y][x]
        if(current == piece):
            return 0

    if(distance == 1 or ((y == size-1 or x == 0) and current != blank)):
        return 0
        
    return distance