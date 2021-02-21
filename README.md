# Classic Brick Breaker

This is a terminal based python brick breaker game, without the usage of any curses libraries. 

Controls
----------
> **j**: move paddle to left

> **l**: move paddle to right

> **spacebar**: to release the ball

> **q**: to quit the game
----------
About the features of this game:
------

It as usual starts with a paddle and a ball on it, whcih gets released according to the input.
The collisions of ball with bricks and wall is pretty much reflectional except the case with paddle. 
- The velocity of the ball gets affected according to the part of paddle it hits.
In simple words, the paddle is segregated into 5 parts. The y velocity is normally revrsed, only x velocity is affected
- If it hits centre portion, no change in x velocity
- If it hits leftmost part, then 2 units of velocity is imparted to left, similarly for right. 
- If it hits the other two part, 1 unit of velocity is imparted accordingly

Note: When the ball collides with the corner of the bricks, it is simply reversed, that is, both x and y velocity are reversed.
Similarly for paddle, if ball is going right and it just touches the left corner of paddle(left of last point of paddle), it is still rebounded, and vice versa.

Types of Bricks
----
- Cyan brick: This bricks gets demolished on hitting just once, that is, strength is 1 units. It is worth 10 points
- Blue bricks: This bricks gets demolished on hitting it twice, that is, strength is 2 units. It is worth 20 points. On being hit the first time, it then becomes a cyan brick of strength 1, and the 20 points gets added when it is totally finished
- Red bricks: This bricks gets demolished on hitting it thrice, that is, strength is 3 units. To do this, first it changes to blue and then cyan on being hit. It is worth 10 points, and it gets added only when that brick is completely finished.
- White bricks: These are unbreakable bricks, which get demolished only if an explosive brick explodes near them.
Yellow bricks(dented as "[!! ]"): It explodes all the nearby bricks(which is in touch with it). To implement the case where multiple explosive bricks are adjacent to each other, i was first using recursion, which was giving some error, hence i did this using dfs.

Requirements:
---



To start:
----
Run the follwing code to start the game:
```
python3 main.py
```


