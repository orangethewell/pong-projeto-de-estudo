from pyray import *
import random

init_window(800, 450, "Pong")

player_speed = 5

p1_pos_x = 10
p1_pos_y = 225 - 20

p2_pos_x = 780
p2_pos_y = 225 - 20

p1_score = 0
p2_score = 0

ball_pos_x = 400
ball_pos_y = 225
ball_radius = 10
ball_speed = random.randrange(5, 10)

ball_dir_x = random.uniform(-1, 1)
ball_dir_y = random.uniform(-1, 1)

set_target_fps(60)

while not window_should_close():
    if is_key_down(KeyboardKey.KEY_S):
        p1_pos_y += player_speed
    elif is_key_down(KeyboardKey.KEY_W):
        p1_pos_y -= player_speed

    if is_key_down(KeyboardKey.KEY_DOWN):
        p2_pos_y += player_speed
    elif is_key_down(KeyboardKey.KEY_UP):
        p2_pos_y -= player_speed

    if ball_pos_y >= 450 or ball_pos_y <= 0:
        ball_dir_y = -ball_dir_y
    
    if check_collision_recs(
        Rectangle(ball_pos_x, ball_pos_y, ball_radius, ball_radius),
        Rectangle(p1_pos_x, p1_pos_y, 10, 40),
    ) or check_collision_recs(
        Rectangle(ball_pos_x, ball_pos_y, ball_radius, ball_radius),
        Rectangle(p2_pos_x, p2_pos_y, 10, 40),
    ):
        ball_dir_x = -ball_dir_x
        ball_dir_y = random.uniform(-1, 1)
        ball_speed = random.randrange(5, 10)

    ball_pos_x += int(ball_dir_x * ball_speed)
    ball_pos_y += int(ball_dir_y * ball_speed)

    if ball_pos_x > 820:
        p1_score += 1
        
        ball_pos_x = 400
        ball_pos_y = 225

        ball_speed = random.randrange(5, 10)

        ball_dir_x = random.uniform(-1, 1)
        ball_dir_y = random.uniform(-1, 1)

    elif ball_pos_x < -10:
        p2_score += 1

        ball_pos_x = 400
        ball_pos_y = 225

        ball_speed = random.randrange(5, 10)

        ball_dir_x = random.uniform(-1, 1)
        ball_dir_y = random.uniform(-1, 1)

    begin_drawing()
    clear_background(BLACK)
    draw_rectangle(
        p1_pos_x,
        p1_pos_y,
        10,
        40,
        WHITE
    )
    draw_rectangle(
        p2_pos_x,
        p2_pos_y,
        10,
        40,
        WHITE
    )
    draw_rectangle(
        ball_pos_x,
        ball_pos_y,
        ball_radius,
        ball_radius,
        WHITE
    )
    draw_text(f"{p1_score}", 340, 10, 40, WHITE)
    draw_text(f"{p2_score}", 440, 10, 40, WHITE)
    end_drawing()
close_window()
