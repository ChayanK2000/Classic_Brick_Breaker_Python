1. say vel_x increases to 6 units, and i am at 97th coord(99 is the end). so it shud then show up at 91 or 95? though this is not much detectable but these cases entangle more and are important ig when say wall/brick or brick/brick are very near to each other and collision is happening.
Update: Still left

2. thus just as we had extra (+1, -1) while collision with pad(but still i did not take into account vel here which i should. Thus now even if ball already goes on right comes to just right of paddle, it bounces(not expected), but a ball already going left comes just right of paddle it bounces(expected)), similar technique to apply in bricks. Need to consider the extreme + 1 points
Update: Paddle collision extreme handle succesfullly using separate if loops.
Update: hopefully this whole issue is solved.
Update issue solved.

3. initially sometimes have to keep spacebar pressed down to release ball(proabbly some tweaks in time/sigal) . I had not used the input py provided by TAs

4. I used txt for consistency so that if we want a bigger figure, we can simply draw it there. Initially i thought this might be better as we progress further in game, but actually it is not needed as far as i can understand as it is better if we keep all bricks uniform, thus no need to calculate height width explicilty by the generate() function. Time wasted! :)

5. !! at certain situation, probably due to timing of moving the paddle, the ball bounces but still live is lost. IDK how!!!(usually at corners and when i just try to insert paddle at last moment)
Probably because collision wall said it lost a life, but before being erased and new generated, collision of paddle is executed, and it still has the same ballobj and paddleobj. Hopefully tackled by clearing and generating new as soon as change lives is called.

or probably can also be tackled if collision handling with wall is did at last after paddle and bricks

Update: handled by the second sol. though thinking to inculcate the first method as it would be neater
but doing that has a problem that on the new life the ball never gets released. unable to figure out.

6. All have different generate function even though i can have one only in item is because everything has different colour. so anyways if i did thta i had to write lots of if else in it depending on which file is being read.

7. to see the hypo case where say first there is cyan then on same place i have unreak, then beacuse of order, unbreak is show, BUT on hitting it it gives 10 points(as it was also cyan), but the area became completely blank, though property of unbreak was stull reflected(the ball reflects from the blank area, as unbreak coord are still there) Writing this because this coincides with the concept of powerups inside bricks