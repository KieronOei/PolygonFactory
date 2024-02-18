import turtle as t
import math

def create_button(x,y,label): #Get initial x and y of button turtle
    button_builder = t.Turtle()
    button_builder.shape("blank") #Make the turtle invisible
    button_builder.penup() #allow the button to be positioned
    button_builder.setpos(x,y)
    button_builder.pendown()
    for i in range(2): 
        button_builder.right(90) #Make a rectangle of length 150 and height 75
        button_builder.forward(200)
        button_builder.right(90)
        button_builder.forward(150)
    button_builder.penup()
    button_builder.goto(x+100,y-90) #Go to centre of the button
    button_builder.write(label,align="center",font=("Comic Sans",16,"bold")) #Create text message inside the button

def create_transformation_button(x,y,label): 
    button_builder = t.Turtle()
    button_builder.shape("blank") #Make the turtle invisible
    button_builder.penup() #allow the button to be positioned
    button_builder.setpos(x,y)
    button_builder.pendown()
    for i in range(2): 
        button_builder.right(90) #Make a rectangle of length 150 and height 75
        button_builder.forward(200)
        button_builder.right(90)
        button_builder.forward(50)
    button_builder.penup()
    button_builder.goto(x+100,y-40) #Go to centre of the button
    button_builder.write(label,align="center",font=("Comic Sans",16,"bold")) #Create text message inside the button

def create_pattern_button(x,y,label,description1,description2): 
    button_builder = t.Turtle()
    button_builder.shape("blank") #Make the turtle invisible
    button_builder.penup() #allow the button to be positioned
    button_builder.setpos(x,y)
    button_builder.pendown()
    for i in range(2): 
        button_builder.right(90) #Make a rectangle of length 300 and height 200
        button_builder.forward(350)
        button_builder.right(90)
        button_builder.forward(100)
    button_builder.penup()
    button_builder.goto(x+175,y-50) #Go to centre of the button
    button_builder.write(label,align="center",font=("Comic Sans",16,"bold")) #Create text message inside the button
    button_builder.penup()
    button_builder.goto(x+175,y-60) #Go to centre of the button
    button_builder.write(description1,align="center",font=("Comic Sans",11,"normal")) #Create first line of description inside the button
    button_builder.penup()
    button_builder.goto(x+175,y-80) #Go to centre of the button
    button_builder.write(description2,align="center",font=("Comic Sans",11,"normal")) #Create first line of description inside the button
    
def create_working_area(x,y):
    working_area_builder = t.Turtle()
    working_area_builder.shape("blank")
    working_area_builder.penup()
    working_area_builder.setpos(x,y)
    working_area_builder.pendown()
    for i in range(2):
        working_area_builder.right(90) #Make a rectangle of length 1200 and height 900
        working_area_builder.forward(400)
        working_area_builder.right(90) 
        working_area_builder.forward(300)

def within_start_point(x,y):
    global start_x
    global start_y
    if (x <= start_x + 10 and x >= start_x - 10)  and (y <= start_y + 10 and y >= start_y - 10):
        return True
    else:
        return False

def within_working_area(x,y): #Determine if user is clicking within the working area
    if (x < 201 and x > -201) and (y < 151 and y > -151):
        return True
    else:
        return False

def within_penup_button(x,y): #Determine if the pen up button is clicked
    if (x < 471 and x > 269) and (y < 151 and y > -1): #if pen up button is clicked
        return True
    else:
        return False

def within_done_button(x,y): #Determine if the pen up button is clicked
    if (x < 471 and x > 269) and (y < -9 and y > -311): #if pen up button is clicked
        return True
    else:
        return False

def within_translate_button(x,y):
    if (x < 471 and x > 269) and (y < 201 and y > 149):
        return True
    else:
        return False

def within_rotate_button(x,y):
    if (x < 471 and x > 269) and (y < 141 and y > 89): 
        return True
    else:
        return False

def within_scale_button(x,y):
    if (x < 471 and x > 269) and (y < 81 and y > 29): 
        return True
    else:
        return False

def within_shear_button(x,y):
    if (x < 471 and x > 269) and (y < 21 and y > -49): 
        return True
    else:
        return False

def within_reflect_button(x,y):
    if (x < 471 and x > 269) and (y < -41 and y > -109): 
        return True
    else:
        return False

def within_done_transforming_button(x,y):
    if (x < 471 and x > 269) and (y < -101 and y > -169): 
        return True
    else:
        return False

def within_pattern1_button(x,y):
    if (x < -251 and x > -601) and (y < -161 and y > -261): 
        return True
    else:
        return False

def within_pattern2_button(x,y):
    if (x < 151 and x > -201) and (y < -161 and y > -261): 
        return True
    else:
        return False

def within_pattern3_button(x,y):
    if (x < 551 and x > 199) and (y < -161 and y > -261): 
        return True
    else:
        return False
    
def detect_start_screen_click(x,y):
    if (x > -251 and x < -49) and (y > -76 and y < 76): #if create poly is clicked
        draw_create_screen()
    elif (x > 49 and x < 251) and (y > -76 and y < 76): #if load poly is clicked
        draw_load_screen()

def draw_start_screen(): #Screen No.1
    s.tracer(0) #To stop screen updates
    create_button(-250,75,"Create Poly") #create a create polygon button
    create_button(50,75,"Load File") # create a view created polygons button
    s.update()
    s.onclick(detect_start_screen_click,1)
    s.listen()

def draw_create_screen(): #Screen No. 2
    global pen
    global polygon
    global bezier_P
    global right_click_count
    global click_list
    
    s.clear()
    s.tracer(0)
    create_working_area(-200,150)
    create_button(270, 150, "Pen Up")
    create_button(270, -10, "Done")
    s.update()
    s.tracer(1) #allow for the user to see their drawing happen in real time
    
    ### initialize variables for drawing
    pen = t.Turtle()
    polygon = {} #Track vertices of polygon using a dictionary
    bezier_P = [] #P is a list of tuples containing x and y coordinates for the bezier curve
    right_click_count = 0 #counts how many times right click has been clicked
    click_list = [] #a list that keeps track of the actions taken by the mouse. S: Start point of polygon L: straight edge, R: curved edge
    polygon["Name"] = s.textinput("Name of polygon", "What is the name of your polygon?")
    polygon["Drawing Instructions"] = []#Initialise an empty list
    
    s.onclick(onleftclick,1)
    s.onclick(onrightclick,3)
    s.onclick(onmiddleclick,2)
    s.listen()


def draw_load_screen(): #Screen No. 2
    global pen
    global bezier_P
    global right_click_count
    global click_list
    global polygon
    global transformation_list
    global transformed
    global pattern
    
    s.clear()
    #initialize variables for drawing
    pen = t.Turtle()
    bezier_P = [] #P is a list of tuples containing x and y coordinates for the bezier curve
    right_click_count = 0 #counts how many times right click has been clicked
    click_list = []
    transformation_list = []
    polygon = {"Drawing Instructions": []}
    transformed = False
    transformation_list = []
    pattern = "" 

    input_file = s.textinput("Load File", "Enter file name in this format: '<file_name>.txt': ")
    file = open(input_file)
    for line in file:
        line = line.strip("\n")
        line = line.split(":")
        #print("line v1",line)
        if line[0] == "Name":
            polygon["Name"] = line[1]
        elif line[0] == "Instruction":
            temp_lst = []
            line = line[1][1:-1] #Remove '[' and ']'
            #print("line v2",line)
            temp_lst.append(line[1]) #add the action letter in
            #print("temp_lst",temp_lst)
            if not line[1] == "R": #if action letter is 'L' or 'S'
                line = line[6:-1].split(", ") #Separate the x and y coordinates
                #print("line v3",line)
                temp_tuple = (float(line[0]),float(line[1]))
                #print("temp_tuple", temp_tuple)
                temp_lst.append(temp_tuple) #Make it e.g ["S", (-76.0, 52.0)]
                #print("temp_lst", temp_lst)
                polygon["Drawing Instructions"].append(temp_lst)
            else:
                line = line[6:-1].split("), ")#Leave only the tuple coordinates
                temp_tuple = ()
                temp_lst_2 = [] #to contain the 4 coordinates
                for item in line:
                    #print("item",item)
                    if "(" in item:
                        item = item[1:] #remove '('
                    if ")" in item:
                        item = item[:-1] #remove ')'
                    item = item.split(", ")    
                    temp_tuple = (float(item[0]), float(item[1]))
                    temp_lst_2.append(temp_tuple)
                    #print("temp_tuple", temp_tuple)
                temp_lst.append(temp_lst_2)
                #print("temp_lst_2", temp_lst_2)
                #print("temp_lst", temp_lst)
                polygon["Drawing Instructions"].append(temp_lst)
                              
        elif line[0] == "Transformations":
            line = line[1][1:-1].split(", [") #remove '[' and ']' and remove front and trailing "'"
            line[0] = line[0].strip("'") #Get rid of the starting and trailing "'"
            #print("line",line)
            temp_list = []
            temp_mini_list = []
            #print("line[0]",line[0])
            temp_list.append(line[0]) #add the transformation name
            line[1] = line[1][:-1] #remove the trailing "]"
            if line[0] == "Rotate": #Accept only one value
                #print("Rotate line[1]", line[1])
                temp_mini_list = [float(line[1])]
            else:
                line[1] = line[1].split(", ")
                #print("Non rotate line[1]", line[1])
                temp_mini_list = [float(line[1][0]),float(line[1][1])]
            temp_list.append(temp_mini_list)
            transformation_list.append(temp_list)
        else:
            pattern = line[0]
            

    #print("polygon",polygon)
    #print("transformation list",transformation_list)
    #print("pattern",pattern)
    file.close()

    #Subsequently, draw the pattern in the file using the data from the file
    if pattern == "pattern1":
        draw_pattern1(polygon)
    elif pattern == "pattern2":
        draw_pattern2(polygon)
    elif pattern == "pattern3":
        draw_pattern3(polygon)

def draw_view_poly_screen(): # Screen No.3
    global transformed
    global transformation_list
    s.clear() #Start a new screen
    draw_polygon(polygon["Drawing Instructions"])
    s.tracer(0)
    create_transformation_button(270,200,"Translate")
    create_transformation_button(270,140,"Rotate")
    create_transformation_button(270,80,"Scale")
    create_transformation_button(270,20,"Shear")
    create_transformation_button(270,-40,"Reflect")
    create_transformation_button(270,-100,"Done") #Can choose to transform or not
    s.update()
    transformation_list = [] #initialize list that keeps track of transformations and their inputs
    transformed = False #initialize a boolean tracker that tells us if the polygon has been transformed
    s.onclick(onleftclick_transformation,1)
    s.listen()

def draw_view_transformed_poly_screen():# Screen No. 4
    global transformed_polygon
    global polygon
    global transformed

    s.clear()
    if transformed:
        draw_polygon(transformed_polygon["Drawing Instructions"])
    else:
        draw_polygon(polygon["Drawing Instructions"])
    s.tracer(0)
    create_pattern_button(-600,-160, "Pattern 1", "Polygon is drawn 10 times,increasing in size"," and shown in ascending order")
    create_pattern_button(-200,-160, "Pattern 2", "Polygon is drawn 10 times,increasing","in shear x-factor while rotating")
    create_pattern_button(200,-160, "Pattern 3", "Polygon is drawn 20 times, increasing ","in size and rotating")
    s.update()
    s.onclick(onleftclick_pattern,1)
    s.listen()

def square_matrix_multiplication(matrix1,matrix2): #matrix 1 and 2 is a tuple with 3 tuples that contain 3 items, the multiplication is done using dot product, result matrix will be [[r0c0,r0c1,r0c2],[r1c0,r1c1,r1c2],[r2c0,r2c1,r2c2]] given that indexes are from 0 to 2
    result = [] 
    for row in range(3): #utilize the no. of rows of matrix 1
        result.append([])
        for col in range(3): #utilize the no. of columns of matrix 2
            dot_product = matrix1[row][0] * matrix2[0][col] + matrix1[row][1] * matrix2[1][col] + matrix1[row][2] * matrix2[2][col]
            result[row].append(dot_product)
    return result

def rect_matrix_multiplication(matrix1,matrix2): # 3x3 multiplied by 3x1
    result = []
    for row in range(3):
        dot_product = 0
        for col in range(3): 
            dot_product += matrix1[row][col] * matrix2[col][0]
        result.append([dot_product])            
    return result

def drawBezierCurve(P): #P is a list containing P0,P1,P2,P3. The four control points
    global pen
    for i in range(101): #i will range from 0 to 100
        t = i/100 #let the progress of the curve be broken up into 100 parts
        x = P[0][0]*(1-t)**3 + 3*P[1][0]*t*(1-t)**2 + 3*P[2][0]*t*t*(1-t) + P[3][0]*t**3
        y = P[0][1]*(1-t)**3 + 3*P[1][1]*t*(1-t)**2 + 3*P[2][1]*t*t*(1-t) + P[3][1]*t**3
        pen.goto(x, y)

def convert_matrix(transformation,answers): #transformation is the name of the transformation, answers gives the values inputted by the user
    if transformation == "Translate":
        matrix = [[1,0,answers[0]],[0,1,answers[1]],[0,0,1]] #answers[0] is answer_x and answers[1] is answer_y
    elif transformation == "Rotate":
        matrix = [[math.cos(answers[0]),-math.sin(answers[0]),0],[math.sin(answers[0]),math.cos(answers[0]),0],[0,0,1]] #answers[0] is answer
    elif transformation == "Scale":
        matrix = [[answers[0],0,0],[0,answers[1],0],[0,0,1]]
    elif transformation == "Shear":
        matrix = [[1,answers[0],0],[answers[1],1,0],[0,0,1]]
    elif transformation == "Reflect":
        matrix = [[answers[0],0,0],[0,answers[1],0],[0,0,1]]

    return matrix

def onleftclick_pattern(x,y): #Screen No. 5, after choosing the pattern it will save the user's data into a file
    global polygon
    global pattern
    global transformed_polygon
    global transformed
    

    s.clear()
    if within_pattern1_button(x,y): #if user chooses pattern 1
        if transformed:
            draw_pattern1(transformed_polygon)
        else:
            draw_pattern1(polygon)
        pattern = "pattern1"

    elif within_pattern2_button(x,y): #if user chooses pattern 2
        if transformed:
            draw_pattern2(transformed_polygon)
        else:
            draw_pattern2(polygon)
        pattern = "pattern2"

    elif within_pattern3_button(x,y): #if user chooses pattern 2
        if transformed:
            draw_pattern3(transformed_polygon)
        else:
            draw_pattern3(polygon)

        pattern = "pattern3"

    save_file() #Finish off the code by saving a file with user's input
    

def onleftclick_transformation(x,y):
    global answer_x
    global answer_y
    global answer
    global polygon
    global transformed #determine if user transformed the polygon
    global transformed_polygon
    global transformation_matrix
    global transformation_list

    if within_translate_button(x,y) or within_rotate_button(x,y) or within_scale_button(x,y) or within_shear_button(x,y) or within_reflect_button(x,y):
        
        if within_translate_button(x,y): #if user wishes to translate
            answer_x = s.textinput("Translate", "Enter x-values in format -> '+/- x': \nIndicate '0' if there is no translation by that axis.") #User-friendly input box
            if "+" in answer_x:
                answer_x = int(answer_x[1:]) #remove '+'
            else:
                answer_x = int(answer_x)
            answer_y = s.textinput("Translate", "Enter y-values in format -> '+/- y': \nIndicate '0' if there is no translation by that axis.")
            if "+" in answer_y:
                answer_y = int(answer_y[1:]) #remove '+'
            else:
                answer_y = int(answer_y)

            transformation_list.append(["Translate",[answer_x,answer_y]])
            matrix = convert_matrix("Translate",[answer_x,answer_y]) #Change to matrix form
            

        elif within_rotate_button(x,y): #if user wishes to rotate
            answer = s.textinput("Rotate", "Enter angle in degrees: ") #User-friendly input box
            answer = math.radians(int(answer)) #Convert to radians for python's math processing

            transformation_list.append(["Rotate",[answer]])
            matrix = convert_matrix("Rotate",[answer]) #Change to matrix form
            
    
        elif within_scale_button(x,y): #if user wishes to scale
            answer_x = float(s.textinput("Scale", "Enter x-scale factor from 0.1 to 2.0: \nIndicate '1' if there is no scaling by that axis.")) #User-friendly input box
            answer_y = float(s.textinput("Scale", "Enter y-scale factor from 0.1 to 2.0: \nIndicate '1' if there is no scaling by that axis.")) #User-friendly input box

            transformation_list.append(["Scale",[answer_x,answer_y]])
            matrix = convert_matrix("Scale",[answer_x,answer_y])#Change to matrix form
                
        elif within_shear_button(x,y): #if user wishes to shear
            answer_x = float(s.textinput("Shear", "Enter x-shear factor from 0.0 to 2.0: \nIndicate '0' if there is no shearing by that axis.")) #User-friendly input box
            answer_y = float(s.textinput("Shear", "Enter y-shear factor from 0.0 to 2.0: \nIndicate '0' if there is no shearing by that axis.")) #User-friendly input box

            transformation_list.append(["Shear",[answer_x,answer_y]])
            matrix = convert_matrix("Shear",[answer_x,answer_y]) #Change to matrix form
                
        elif within_reflect_button(x,y): #if user wishes to shear
            answer_x = s.textinput("Reflect", "Do you wish to reflect by the x-axis? (y/n): ") #User-friendly input box
            if answer_x == "y":
                answer_x = -1
            elif answer_x == "n":
                answer_x = 1
            answer_y = s.textinput("Reflect", "Do you wish to reflect by the y-axis? (y/n): ") #User-friendly input box
            if answer_y == "y":
                answer_y = -1
            elif answer_y == "n":
                answer_y = 1

            transformation_list.append(["Reflect",[answer_x,answer_y]])
            matrix = convert_matrix("Reflect",[answer_x,answer_y]) #Change to matrix form

            
        if not transformed: #if transformation matrix has not been created
            transformation_matrix = matrix
        else: #multiply together all the transformation matrices first
            transformation_matrix = square_matrix_multiplication(transformation_matrix, matrix)
        transformed = True

    elif within_done_transforming_button(x,y):
        if transformed:
            transformed_polygon = {"Name": polygon["Name"],"Drawing Instructions": []}
            for action in polygon["Drawing Instructions"]: #Transform every coordinate
                if action[0] == "R": #Since "R" has 4 coordinates
                    transformed_curve_coordinates = []
                    for i in range(4): #Transform 4 coordinates 
                        matrix = [[action[1][i][0]], [action[1][i][1]], [1]] #action[0] is "R", action [i][1] is 4 of the curve (x,y)
                        result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                        transformed_curve_coordinates.append((result_matrix[0][0], result_matrix[1][0])) #Create the list of 4 coordinates
                    transformed_polygon["Drawing Instructions"].append([action[0], transformed_curve_coordinates])
                else: # if "L" or "S"
                    matrix = [[action[1][0]], [action[1][1]], [1]] #action[0] is "S"/"L", action [1] is (x,y)
                
                    result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                    transformed_polygon["Drawing Instructions"].append([action[0], (result_matrix[0][0], result_matrix[1][0])])
                    polygon = transformed_polygon #re-assign new transformed polygon dictionary to polygon
                    
        draw_view_transformed_poly_screen()
    
        

def onleftclick(x,y):
    global start_x #create global variables start x and start y which indicate start point of the polygon
    global start_y
    global click_list
    global pen
    global polygon

    if not within_working_area(x,y) and not within_penup_button(x,y) and not within_done_button: #Working area helps limit the size of the polygon drawn
        message.penup()
        message.goto(0,200)
        message.write("Please work within the working area!",align = "Center", font = ("Comic Sans", 16, "bold"))

    elif within_penup_button(x,y): #Allows users to pen up momentarily. The next click they select, the pen will automatically go down
        if pen.isdown():
            pen.penup()

    elif within_done_button(x,y): #Allows users to save their polygon and move on to transformations
        draw_view_poly_screen()
            
    else:
        message.clear()
        if pen.xcor() == 0.0 and pen.ycor() == 0.0: #if pen is still at home position, meaning user has not clicked on the screen to start drawing
            click_list.append("S")
            start_x = x
            start_y = y
            pen.penup()
            pen.goto(x,y)
            pen.pendown()
            polygon["Drawing Instructions"].append(("S",(x,y)))
            
        else:
            if within_start_point(x,y): # if user wishes to close the polygon, it will automatically close the polygon for them
                x = start_x
                y = start_y
                pen.goto(x,y)
                click_list.append("L")
                polygon["Drawing Instructions"].append(("L",(x,y)))

            else: #if drawing out the polygon with straight edges
                if not pen.isdown(): #if pen is up; assuming it's from clicking the pen up button
                    pen.goto(x,y)
                    start_x = x
                    start_y = y
                    pen.pendown() #automatic pen down
                    click_list.append("U") #Indicates pen up was used, meaning a start of a new hole
                    polygon["Drawing Instructions"].append(("U",(x,y)))
                else:
                    pen.goto(x,y)
                    click_list.append("L")
                    polygon["Drawing Instructions"].append(("L",(x,y)))

def onrightclick(x,y): #needs to register 3 right clicks in order to draw bezier curve
    global right_click_count
    global bezier_P
    global start_x
    global start_y
    global click_list
    global pen
    global polygon

    if not within_working_area(x,y):
        message.penup()
        message.goto(0,200)
        message.write("Please work within the working area!",align = "Center", font = ("Comic Sans", 16, "bold"))
    else:
        message.clear()
        right_click_count += 1
        
        if right_click_count == 1: #Put in current coordinates into the list of coordinates for the curve
            bezier_P.append((pen.xcor(),pen.ycor()))
            
        if right_click_count < 3: #if the middle 2 control points have not been inputted
            bezier_P.append((x,y))

        else: #when the final control point is inputted
            if within_start_point(x,y): # if user wishes to close the polygon it will automatically do so for them
                x = start_x
                y = start_y

            bezier_P.append((x,y))
            click_list.append("R")
            polygon["Drawing Instructions"].append(("R",bezier_P))
            drawBezierCurve(bezier_P)
            right_click_count = 0 #reset counter 
            bezier_P = [] #reset bezier list

def onmiddleclick(x,y):
    global click_list
    global bezier_P
    global right_click_count
    global pen
    global polygon

    if click_list[-1] == "L": #if last action taken was the start point or a straight edge
        pen.undo()

    elif click_list[-1] == "S": #if last action taken was the start point or a straight edge
        pen.up()
        pen.goto(0,0)
        pen.down()

    elif click_list[-1] == "U": #if last action taken placing the starting point of the hole
        for i in range(3):
            pen.undo()
    
    elif click_list[-1] == "R": #if last action taken was a curved edge
        for i in range(101): #undo the whole curve given that there are 101 pen commands in the bezier curve function
            pen.undo()

    polygon["Drawing Instructions"] = polygon["Drawing Instructions"][:-1] #Remove the last entry
    click_list = click_list[:-1]

def draw_polygon(instructions): #Input is the dictionary's drawing instructions
    global pen
    #print("instructions",instructions)
    for instruction in instructions:
        #print("instruction",instruction)
        if instruction[0] == "S" or instruction[0] == "U":
            pen.penup()
            pen.goto(instruction[1])
            pen.pendown()

        elif instruction[0] == "L":
            pen.goto(instruction[1])

        elif instruction[0] == "R":
            drawBezierCurve(instruction[1])

def draw_pattern1(polygon): #Draw a pattern that increases in size and translates 10 times
    
    translation_factor = 100
    scale_factor = 1.5
    draw_polygon(polygon["Drawing Instructions"])
    for i in range(9):
        transformed_polygon = {"Name": polygon["Name"] + " transformed", "Drawing Instructions": []}
        translate_matrix = convert_matrix("Translate", [translation_factor,0])
        scale_matrix = convert_matrix("Scale", [scale_factor,scale_factor])
        transformation_matrix = square_matrix_multiplication(translate_matrix,scale_matrix) #Combine the two changes first before applying to the coordinates
        for action in polygon["Drawing Instructions"]:

            if action[0] == "R": #Since "R" has 4 coordinates
                    transformed_curve_coordinates = []
                    for i in range(4): #Transform 4 coordinates 
                        matrix = [[action[1][i][0]], [action[1][i][1]], [1]] #action[0] is "R", action [i][1] is 4 of the curve (x,y)
                        result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                        transformed_curve_coordinates.append((result_matrix[0][0], result_matrix[1][0])) #Create the list of 4 coordinates
                    transformed_polygon["Drawing Instructions"].append([action[0], transformed_curve_coordinates])
            else: # if "L" or "S"
                matrix = [[action[1][0]], [action[1][1]], [1]] #action[0] is "S"/"L", action [1] is (x,y) 
                result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                transformed_polygon["Drawing Instructions"].append([action[0], (result_matrix[0][0], result_matrix[1][0])]) #Add new transformed coordinates into the list
                
        draw_polygon(transformed_polygon["Drawing Instructions"]) #Draw transformed polygon
        translation_factor += 100
        scale_factor += 0.5

def draw_pattern2(polygon): #Draw a pattern that shears the x-axis while rotating

    shear_factor = 1.0
    rotate_angle = 36
    draw_polygon(polygon["Drawing Instructions"])
    for i in range(9):
        transformed_polygon = {"Name": polygon["Name"] + " transformed", "Drawing Instructions": []}
        shear_matrix = convert_matrix("Shear",[shear_factor,0])
        rotate_matrix = convert_matrix("Rotate",[rotate_angle])
        transformation_matrix = square_matrix_multiplication(shear_matrix,rotate_matrix)

        for action in polygon["Drawing Instructions"]:

            if action[0] == "R": #Since "R" has 4 coordinates
                    transformed_curve_coordinates = []
                    for i in range(4): #Transform 4 coordinates 
                        matrix = [[action[1][i][0]], [action[1][i][1]], [1]] #action[0] is "R", action [i][1] is 4 of the curve (x,y)
                        result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                        transformed_curve_coordinates.append((result_matrix[0][0], result_matrix[1][0])) #Create the list of 4 coordinates
                    transformed_polygon["Drawing Instructions"].append([action[0], transformed_curve_coordinates])
            else: # if "L" or "S"
                matrix = [[action[1][0]], [action[1][1]], [1]] #action[0] is "S"/"L", action [1] is (x,y) 
                result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                transformed_polygon["Drawing Instructions"].append([action[0], (result_matrix[0][0], result_matrix[1][0])]) #Add new transformed coordinates into the list
                
        draw_polygon(transformed_polygon["Drawing Instructions"]) #Draw transformed polygon
        rotate_angle += 36
        shear_factor += 0.1
   

def draw_pattern3(polygon): #Draw a pattern that increases in size while rotating

    scale_factor = 1.2
    rotate_angle = 18
    draw_polygon(polygon["Drawing Instructions"])
    for i in range(19):
        transformed_polygon = {"Name": polygon["Name"] + " transformed", "Drawing Instructions": []}
        scale_matrix = convert_matrix("Scale",[scale_factor,scale_factor])
        rotate_matrix = convert_matrix("Rotate",[rotate_angle])
        transformation_matrix = square_matrix_multiplication(scale_matrix,rotate_matrix)

        for action in polygon["Drawing Instructions"]:

            if action[0] == "R": #Since "R" has 4 coordinates
                    transformed_curve_coordinates = []
                    for i in range(4): #Transform 4 coordinates 
                        matrix = [[action[1][i][0]], [action[1][i][1]], [1]] #action[0] is "R", action [i][1] is 4 of the curve (x,y)
                        result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                        transformed_curve_coordinates.append((result_matrix[0][0], result_matrix[1][0])) #Create the list of 4 coordinates
                    transformed_polygon["Drawing Instructions"].append([action[0], transformed_curve_coordinates])
            else: # if "L" or "S"
                matrix = [[action[1][0]], [action[1][1]], [1]] #action[0] is "S"/"L", action [1] is (x,y) 
                result_matrix = rect_matrix_multiplication(transformation_matrix,matrix)
                transformed_polygon["Drawing Instructions"].append([action[0], (result_matrix[0][0], result_matrix[1][0])]) #Add new transformed coordinates into the list
                
        draw_polygon(transformed_polygon["Drawing Instructions"]) #Draw transformed polygon
        rotate_angle += 18
        scale_factor += 0.1

def save_file():
    global transformation_list
    global polygon
    global pattern
    global transformed

    file = open(f"{polygon['Name']}.txt","w")
    file.write(f"Name:{polygon['Name']}\n")
    for action in polygon["Drawing Instructions"]:
        file.write(f"Instruction:{action}\n")
    for transformation in transformation_list:
        file.write(f"Transformations:{transformation}\n")
    file.write(f"{pattern}")
    file.close()         

### initialize turtle settings
t.shape("blank") #make turtle icon visible on the screen
t.speed(0) #set turtle speed to fastest
t.mode("logo") #Initialise the turtle to face north
t.title("Welcome to the shape factory!")
###

### initialize a message turtle
message = t.Turtle()
message.shape("blank")
message.pencolor("red")

### initialize screen settings
s = t.Screen() #initialize screen variable
s.screensize(1000,800)
###

### Load Start Menu
draw_start_screen()
###
