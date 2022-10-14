import arcade


arcade.open_window(1000,800,"Graph paper")
arcade.set_background_color(arcade.color.AMAZON)

arcade.start_render()
arcade.draw_circle_filled(400,400,300,arcade.color.GREEN)
arcade.draw_arc_outline(400, 300, 400, 100, arcade.color.LION, -180,0,0)
arcade.draw_arc_filled(300,450,100,200, arcade.color.BLACK, 0, 180)
#arcade.draw_arc_filled(500,450,100, arcade.color.BLACK, 0, 200)
arcade.draw_line(660, 550, 100, 400, arcade.color.BLACK)
arcade.draw_arc_filled(450, 450, 100, 100, arcade.color.BLACK, 0, 280)

arcade.draw_triangle_filled(400, 300, 450, 200, 250, 300, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(300,500,1000,650, arcade.color.BLACK)
signature = arcade.Text("Pumpkin by/nComp151-804", 10, 800, arcade.color.ARSENIC, 20)
signature.draw()
arcade.finish_render()

arcade.run()