# PolygonFactory
<h2> Description </h2>
Using the turtle module on python, the aim of this program is to give users the ability to create their own shape with the click of a mouse, choose their own transformations (translate, rotate, scale, shear, reflect) and create a pattern (choose one out of three pre-coded patterns). At the end of the program, a text file will be created, which will save the drawing instructions of the polygon, the transformations chosen as well as the pattern number. Users will be able to load their saved data into the program to see their pattern being drawn out whenever they want, they are also able to create a pattern being drawn out by creating a text file and following the format, create their own polygon, transformations and pattern by manually typing in the drawing instructions using coordinates etc. 

<h2> Features </h2>

<h3> Creating the environment </h3>
At the start of every screen that is loaded, turtle will freeze the drawing animations until the screen is fully drawn, then it will show the full screen. The buttons seen on the screen are actually drawn by the turtle using coordinates that I figured out on my own, trying to scale it according to the window size I set for my program (1000 x pixels by 800 y pixels). The buttons are triggered when the user left clicks on an area that is marked out using a function named "within_...". This helps the program detect the user's intentions

<h3> Drawing with a mouse (Create polygon) </h3>

<h4> Left Click </h4>
<h5> Before anything is drawn </h5>
The first left click will be used to indicate the start point of the drawing, meaning the pen will go to the coordinate from the origin (0,0) without putting its pen down. The program will save the instructions into a dictionary called polygon, using key "Drawing Instructions" and appending the mouse option and the chosen coordinates into the value which is an empty list  e.g [] -> [ ["S", (100.0,90.0)] ] 

<h5> After the start point is chosen </h5>
Subsequent left clicks will be the destination for the pen to go to, leaving a straight line drawn from its starting position to the position chosen by the left click. The program will save the instructions and append the mouse option and chosen coordinates into the list mentioned above. The result will be e.g [ ["S", (100.0,90.0)] ] -> [ ["S", (100.0,90.0)], ["L", (80.3, 60.2)] ] 

<h4> Right Click </h4>

<h5> Utilising the bezier curve </h5>
Curves can be made by making three right clicks. The bezier curve function will use 4 points to make the curve, the current coordinates of the turtle together with the coordinates of the three right clicks made. The instructions will be saved and the result will be e.g [ ["S", (100.0,90.0)], ["L", (80.3, 60.2)] ] -> [ ["S", (100.0,90.0)], ["L", <b>(80.3, 60.2)</b>], ["R", [<b>(80.3,60.2)</b>, (90.5,70.4), (100.0, 69.4), (105.2, 64.2)]] ] 

<h4> Middle Click </h4>

Acts as an undo function, where it will remove the last drawing instruction from the polygon dictionary as well as make the turtle go back to its previously recorded coordinates.

<h4> Pen Up </h4>

Clicking on the pen up button allows users to manually move the pen up, giving them the option of making holes in their polygon. E.g Users now have the ability to create the polygon "B"

<h3> Selecting the transformation </h3>

<h5> Utilising matrice mulitplication </h5>
Matrice multiplication makes it a lot easier to transform the coordinates of the polygon as required by the user

<h4> Translate </h4>

Users can choose to translate their polygon to the left (using -x) or to the right (using +x) or down (using -y) or up (using +y) in the input box provided

<h4> Rotate </h4> 

Users can choose to rotate their polygon to any degree that they would like

<h4> Scale </h4>

Users can scale their polygon along the x-axis and y-axis. The range is limited from 0.1 to 2.0 though as increasing the upper limit would most likely lead to the polygon going beyond the limits of the window created

<h4> Shear </h4>

Users can shear their polygon along the x-axis and y-axis. The range is also limited to 0.0 to 2.0 for the same reasons.

<h4> Reflect </h4>

Users can reflect their polygon about the x-axis and y-axis. Just need to input "y" or "n" to the input prompts provided

<h3> Selecting the pattern </h3>

Users can choose from one of three patterns to see their transformed polygon being used to create a pattern on the screen

<h4> Limitations </h4>

Currently the program does not support the ability for users to customise and create their own patterns though given the current structure of the code, it is quite possible to achieve this feature in a short amount of time. I am just too lazy rn. Maybe in the future

<h3> Load file </h3>

At the end of the "Create polygon" feature, the program will save a text file, that is readable for both humans and python, which hence allows users to be able to either (1) Use the text file created to view their creation again or (2) Modify it on the text file itself to create a different looking pattern. Similarly, users can just skip the "Create polygon" step and create their own pattern using a text file which follows the template. But where's the fun in that?
