def is_inside(event, coordinates):
    return (coordinates[0] <= event.x <= coordinates[2]) and (coordinates[1] <= event.y <= coordinates[3])
