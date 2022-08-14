from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Slot(Widget):
    pass


class HockeyPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1.1 * vx, vy)
            vel = bounced*2
            ball.velocity = vel.x, vel.y + offset
            if vx < -20 or vx > 20  :
                bounced = bounced
                vel = bounced * 0.9
                ball.velocity = vel.x, vel.y + offset
            print(vy)

class HockeyBall(Widget):
    
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        

class HockeyGame(Widget):
    ball = ObjectProperty(None)

    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self,vel=(6, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        
    
    def update(self, dt):
        # call ball.move and other stuff
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if ((self.ball.x < self.x) and (self.ball.y < 190 or self.ball.y > 330)) or (self.ball.right> self.width and (self.ball.y < 190 or self.ball.y > 330)):
            self.ball.velocity_x *= -1

        

        # went of to a slot to score point?
        if ((self.ball.x < self.x -75) and (self.ball.y > 190 and self.ball.y < 330)):
            self.player2.score += 1
            self.serve_ball(vel=(6, 0))
        if (self.ball.right> self.width + 75 and (self.ball.y > 190 or self.ball.y < 330)):
            self.player1.score += 1
            self.serve_ball(vel=(-6, 0))
        print(self.ball.y)

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y 
            self.player1.center_x = touch.x 
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
        



class HockeyApp(App):
    def build(self):
        game = HockeyGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__=="__main__":
    HockeyApp().run()