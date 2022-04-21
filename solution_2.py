def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move() 

while not at_goal(): 
  if wall_on_right():
    if wall_in_front():
      turn_left()
      if wall_in_front():
        turn_left()
      move()
    else:
      move()
  else:
    if wall_in_front():
      turn_right()
    else:
      move()
       
