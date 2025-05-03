from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
# Camera-related variables
camera_pos = (100, 100, 400)
fps_mode=False

fovY = 120  # Field of view
GRID_LENGTH = 600  # Length of grid lines
grid_size = GRID_LENGTH
cell_size = grid_size / 26
wall_height=150
def draw_pipes():
    #small pipe
    glPushMatrix()
    glTranslatef(100, 20, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 7, 7, 140, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(100, 20, 130)
    glRotatef(90, 1, 0, 0)
    glColor3f(0.3, 0.1, 0)    
    gluCylinder(gluNewQuadric(), 7, 7, 20, 10, 10)
    glPopMatrix()
    #small pipe2
    glPushMatrix()
    glTranslatef(20, 100, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 7, 7, 140, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 100, 130)
    glRotatef(90, 0, 1, 0)
    glColor3f(0.3, 0.1, 0)    
    gluCylinder(gluNewQuadric(), 7, 7, 20, 10, 10)
    glPopMatrix()

    #small pipe-3
    glPushMatrix()
    glTranslatef(20, 550, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 7, 7, 140, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 550, 130)
    glRotatef(90, 0, 1, 0)
    glColor3f(0.3, 0.1, 0)    
    gluCylinder(gluNewQuadric(), 7, 7, 20, 10, 10)
    glPopMatrix()

    #small pipe -4
    glPushMatrix()
    glTranslatef(20, 580, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 7, 7, 140, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(20, 580, 130)
    glRotatef(90, 1, 0, 0)
    glColor3f(.5, .5, .5)   
    gluCylinder(gluNewQuadric(), 3, 3, 30, 10, 10)
    glPopMatrix()
    #wrapped pipe
    glPushMatrix()
    glTranslatef(520, 40, 20)
    glRotatef(90, 0, 1, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 10, 10, 50, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(530, 40, 0)
    glColor3f(0.3, 0.1, 0) 
    gluCylinder(gluNewQuadric(), 10, 10, 20, 10, 10)
    glPopMatrix()
    #wrapped pipe-2
    glPushMatrix()
    glTranslatef(580, 570, 100)
    glRotatef(90, 1, 0, 0)
    glColor3f(.5, .5, .5) 
    gluCylinder(gluNewQuadric(), 2, 2, 515, 10, 10)
    glPopMatrix()
    #big pipe
    glPushMatrix()
    glTranslatef(580, 40, 0)
    glColor3f(0.3, 0.1, 0)  
    gluCylinder(gluNewQuadric(), 20,20, 140, 10, 10)
    glPopMatrix()
    #big pipe-2
    glPushMatrix()
    glTranslatef(580, 580, 0)
    glColor3f(0.3, 0.1, 0)  
    gluCylinder(gluNewQuadric(), 15,15, 140, 10, 10)
    glPopMatrix()
    glColor3f(0.8, 0.8, 0.8)  # Off-white for ceramic
   
    
def draw_tiled_wall(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    """
    Draw a wall with a tiled pattern
    Parameters define the four corners of the wall
    """
    global cell_size, wall_height
    
    # Calculate the number of tiles to fit on the wall
    wall_length = max(abs(x2 - x1), abs(y2 - y1))
    num_tiles = int(wall_length / cell_size)
    
    # Determine if the wall is along x or y axis
    is_x_axis = abs(y2 - y1) < abs(x2 - x1)
    
    # For each tile on the wall
    for i in range(num_tiles):
        for j in range(int(wall_height / cell_size)):
            # Calculate the corners of this tile
            if is_x_axis:
                tx1 = x1 + i * cell_size
                ty1 = y1
                tz1 = j * cell_size
                
                tx2 = x1 + (i + 1) * cell_size
                ty2 = y1
                tz2 = j * cell_size
                
                tx3 = x1 + (i + 1) * cell_size
                ty3 = y1
                tz3 = (j + 1) * cell_size
                
                tx4 = x1 + i * cell_size
                ty4 = y1
                tz4 = (j + 1) * cell_size
            else:
                tx1 = x1
                ty1 = y1 + i * cell_size
                tz1 = j * cell_size
                
                tx2 = x1
                ty2 = y1 + (i + 1) * cell_size
                tz2 = j * cell_size
                
                tx3 = x1
                ty3 = y1 + (i + 1) * cell_size
                tz3 = (j + 1) * cell_size
                
                tx4 = x1
                ty4 = y1 + i * cell_size
                tz4 = (j + 1) * cell_size
            
            # Set color based on checkerboard pattern
            if (i + j) % 2 == 0:
                glColor3f(0.8, 0.8, 0.8)# Slightly lighter gray
            else:
                glColor3f (0.7, 0.7, 0.7)   # Darker gray
            
            # Draw the tile
            glBegin(GL_QUADS)
            glVertex3f(tx1, ty1, tz1)
            glVertex3f(tx2, ty2, tz2)
            glVertex3f(tx3, ty3, tz3)
            glVertex3f(tx4, ty4, tz4)
            glEnd()
            
            # Draw thin black grid lines
            line_width = cell_size * 0.03  # Very thin lines
            glColor3f(0, 0, 0)  # Black for grid lines
            
            # Draw horizontal grid line at the bottom of the tile
            glBegin(GL_QUADS)
            if is_x_axis:
                glVertex3f(tx1, ty1 + 0.1, tz1)
                glVertex3f(tx2, ty2 + 0.1, tz2)
                glVertex3f(tx2, ty2 + 0.1, tz2 + line_width)
                glVertex3f(tx1, ty1 + 0.1, tz1 + line_width)
            else:
                glVertex3f(tx1 + 0.1, ty1, tz1)
                glVertex3f(tx1 + 0.1, ty2, tz2)
                glVertex3f(tx1 + 0.1, ty2, tz2 + line_width)
                glVertex3f(tx1 + 0.1, ty1, tz1 + line_width)
            glEnd()
            
            # Draw vertical grid line at the left of the tile
            glBegin(GL_QUADS)
            if is_x_axis:
                glVertex3f(tx1, ty1 + 0.1, tz1)
                glVertex3f(tx1, ty1 + 0.1, tz4)
                glVertex3f(tx1 + line_width, ty1 + 0.1, tz4)
                glVertex3f(tx1 + line_width, ty1 + 0.1, tz1)
            else:
                glVertex3f(tx1 + 0.1, ty1, tz1)
                glVertex3f(tx1 + 0.1, ty1, tz4)
                glVertex3f(tx1 + 0.1, ty1 + line_width, tz4)
                glVertex3f(tx1 + 0.1, ty1 + line_width, tz1)
            glEnd()
def draw_saw():
    """
    Draw a 3D saw model similar to the image.
    This function draws a saw with wooden handle and metal blade.
    Positioned at x=550, y=550, z=10, with overall size of 50.
    """
    # Position the saw at the specified coordinates
    glPushMatrix()
    glTranslatef(530, 530, 10)  # Position at x=550, y=550, z=10
    glScalef(0.2, 0.2, 0.2)  # Scale down to approximately 50 units in size
    
    # Draw the blade
    glColor3f(0.8, 0.8, 0.8)  # Silver/gray color for the blade
    
    # The main blade - flat rectangle with slight thickness
    glBegin(GL_QUADS)
    # Front surface
    glVertex3f(-100, 0, 0)
    glVertex3f(100, 0, 0)
    glVertex3f(100, 10, 0)
    glVertex3f(-100, 10, 0)
    
    # Back surface
    glVertex3f(-100, 0, -1)
    glVertex3f(100, 0, -1)
    glVertex3f(100, 30, -1)
    glVertex3f(-100, 30, -1)
    
    # Top edge
    glVertex3f(-100, 30, 0)
    glVertex3f(100, 30, 0)
    glVertex3f(100, 30, -1)
    glVertex3f(-100, 30, -1)
    
    # Bottom edge with teeth
    # We'll draw the bottom edge separately for the teeth
    glEnd()
    
    # Draw teeth on the bottom edge of the blade
    glBegin(GL_TRIANGLES)
    num_teeth = 40
    tooth_width = 150 / num_teeth
    tooth_height = 6
    
    for i in range(num_teeth):
        # Each tooth is a small triangle
        glVertex3f(-100 + i * tooth_width, 0, -1.5)  # Middle of blade thickness
        glVertex3f(-100 + (i + 0.5) * tooth_width, -tooth_height, -1.5)  # Tip of tooth
        glVertex3f(-100 + (i + 1) * tooth_width, 0, -1.5)  # Next tooth start
    glEnd()
    
    # Draw the handle (BIGGER HANDLE)
    glColor3f(0.76, 0.6, 0.42)  # Light wood color
    
    # Base of handle (connects to blade) - INCREASED DIMENSIONS
    glBegin(GL_QUADS)
    # Front face - wider and taller
    glVertex3f(60, -10, -8)
    glVertex3f(110, -10, -8)
    glVertex3f(110, 25, -8)
    glVertex3f(60, 25, -8)
    
    # Back face - wider and taller
    glVertex3f(60, -10, 6)
    glVertex3f(110, -10, 6)
    glVertex3f(110, 25, 6)
    glVertex3f(60, 25, 6)
    
    # Left side face
    glVertex3f(60, -10, -8)
    glVertex3f(60, -10, 6)
    glVertex3f(60, 25, 6)
    glVertex3f(60, 25, -8)
    
    # Right side face
    glVertex3f(110, -10, -8)
    glVertex3f(110, -10, 6)
    glVertex3f(110, 25, 6)
    glVertex3f(110, 25, -8)
    
    # Bottom face
    glVertex3f(60, -10, -8)
    glVertex3f(110, -10, -8)
    glVertex3f(110, -10, 6)
    glVertex3f(60, -10, 6)
    
    # Top face
    glVertex3f(60, 25, -8)
    glVertex3f(110, 25, -8)
    glVertex3f(110, 25, 6)
    glVertex3f(60, 25, 6)
    glEnd()
    
    glPopMatrix()  # End of saw drawing

def draw_steel_door(x, y, is_x_wall):
    """
    Draw a black steel door on a wall
    Parameters:
    x, y - coordinates where the door should be placed
    is_x_wall - True if the door is on a wall parallel to x-axis, False if parallel to y-axis
    """
    global wall_height, cell_size
    
    # Door dimensions
    door_width = cell_size * 4  # 6 cells wide
    door_height = wall_height * 0.8  # 80% of wall height
    
    # Steel black color
    door_color = (0.15, 0.15, 0.17)  # Dark gray with slight blue tint for steel look
    frame_color = (0.1, 0.1, 0.1)  # Even darker for the frame
    z_offset = 0.2  # Small offset to prevent z-fighting with the wall
    
    # Draw the door frame first (slightly bigger than the door)
    frame_width = door_width * 1.1
    frame_height = door_height * 1.05
    
    glPushMatrix()
    
    if is_x_wall:  # Door on north or south wall
        # Door frame
        glColor3f(*frame_color)
        glBegin(GL_QUADS)
        # Front face of frame
        glVertex3f(x - frame_width/2, y + z_offset, 0)
        glVertex3f(x + frame_width/2, y + z_offset, 0)
        glVertex3f(x + frame_width/2, y + z_offset, frame_height)
        glVertex3f(x - frame_width/2, y + z_offset, frame_height)
        glEnd()
        
        # Door itself
        glColor3f(*door_color)
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(x - door_width/2, y + z_offset + 2, 0)
        glVertex3f(x + door_width/2, y + z_offset + 2, 0)
        glVertex3f(x + door_width/2, y + z_offset + 2, door_height)
        glVertex3f(x - door_width/2, y + z_offset + 2, door_height)
        glEnd()
        
        
   
    
    # Add door details - horizontal panels
    num_panels = 3
    panel_height = door_height / num_panels
    panel_inset = 1.0
    
    glColor3f(*[c * 0.9 for c in door_color])  # Slightly lighter for panels
    
    for i in range(num_panels):
        panel_z_bottom = i * panel_height
        panel_z_top = (i + 1) * panel_height
        
        if is_x_wall:
            glBegin(GL_QUADS)
            glVertex3f(x - door_width/2 + panel_inset, y + z_offset + 3, panel_z_bottom + panel_inset)
            glVertex3f(x + door_width/2 - panel_inset, y + z_offset + 3, panel_z_bottom + panel_inset)
            glVertex3f(x + door_width/2 - panel_inset, y + z_offset + 3, panel_z_top - panel_inset)
            glVertex3f(x - door_width/2 + panel_inset, y + z_offset + 3, panel_z_top - panel_inset)
            glEnd()
        else:
            glBegin(GL_QUADS)
            glVertex3f(x + z_offset + 3, y - door_width/2 + panel_inset, panel_z_bottom + panel_inset)
            glVertex3f(x + z_offset + 3, y + door_width/2 - panel_inset, panel_z_bottom + panel_inset)
            glVertex3f(x + z_offset + 3, y + door_width/2 - panel_inset, panel_z_top - panel_inset)
            glVertex3f(x + z_offset + 3, y - door_width/2 + panel_inset, panel_z_top - panel_inset)
            glEnd()
    
    glPopMatrix()
def grid():
    global grid_size, wall_height, cell_size
    num_cells=26
    # Draw floor tiles with more detail - smaller grid squares
    
    for i in range(num_cells):
        for j in range(num_cells):
            # Calculate the corners of each cell
            x1 = i * cell_size
            y1 = j * cell_size
            x2 = (i + 1) * cell_size
            y2 = (j + 1) * cell_size
            
            # Set base color based on checkerboard pattern
            if (i + j) % 2 == 0:
                base_color = (1, 1, 1)  # White
            else:
                base_color = (1, 1, 1)  # Also white (you might want to change this for contrast)
            
            # Draw the main tile
            glBegin(GL_QUADS)
            glColor3f(*base_color)
            glVertex3f(x1, y1, 0)
            glVertex3f(x2, y1, 0)
            glVertex3f(x2, y2, 0)
            glVertex3f(x1, y2, 0)
            glEnd()
            
            # Draw grid lines (thin lines between tiles)
            line_width = cell_size * 0.03  # Very thin lines
            
            # Draw horizontal grid line at the bottom of the cell
            glBegin(GL_QUADS)
            glColor3f(0, 0, 0)  # Black for grid lines
            glVertex3f(x1, y1, 0.1)
            glVertex3f(x2, y1, 0.1)
            glVertex3f(x2, y1 + line_width, 0.1)
            glVertex3f(x1, y1 + line_width, 0.1)
            glEnd()
            
            # Draw vertical grid line at the left of the cell
            glBegin(GL_QUADS)
            glColor3f(0, 0, 0)  # Black for grid lines
            glVertex3f(x1, y1, 0.1)
            glVertex3f(x1 + line_width, y1, 0.1)
            glVertex3f(x1 + line_width, y2, 0.1)
            glVertex3f(x1, y2, 0.1)
            glEnd()
    
    # Draw walls with tiled appearance
    # North wall (back)
    draw_tiled_wall(0, grid_size, 0,
                   grid_size, grid_size, 0,
                   grid_size, grid_size, wall_height,
                   0, grid_size, wall_height)
    
    # South wall (front)
    draw_tiled_wall(0, 0, 0,
                   grid_size, 0, 0,
                   grid_size, 0, wall_height,
                   0, 0, wall_height)
    draw_steel_door(grid_size/2, 0, True)
    # East wall (right)
    draw_tiled_wall(grid_size, 0, 0,
                   grid_size, grid_size, 0,
                   grid_size, grid_size, wall_height,
                   grid_size, 0, wall_height)
    
    # West wall (left)
    draw_tiled_wall(0, 0, 0,
                   0, grid_size, 0,
                   0, grid_size, wall_height,
                   0, 0, wall_height)
def draw_sink(x_pos,y_pos):
    """
    Draw a simple sink at a fixed position
    """
    # Fixed position
    wall_offset = 5
    
    # Sink dimensions
    sink_width = 40
    sink_depth = 30
    sink_height = 15
    
    # Position calculation
    z_pos = wall_height * 0.4  # Height from floor

    drain_radius = sink_width * 0.08
    # Draw the main sink body
    glPushMatrix()
    
    # Top rim of sink
    glColor3f(0,0,.9)
    glBegin(GL_QUADS)
    # Top surface
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset, z_pos-7)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset, z_pos-7)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset + sink_depth, z_pos-7)
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset + sink_depth, z_pos-7)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.9, 0.9, 0.92)
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset, z_pos - sink_height)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset, z_pos - sink_height)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset, z_pos)
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset, z_pos)
    
    # Left side face
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset, z_pos - sink_height)
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset + sink_depth, z_pos - sink_height)
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset + sink_depth, z_pos)
    glVertex3f(x_pos - sink_width/2, y_pos + wall_offset, z_pos)
    
    # Right side face
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset, z_pos - sink_height)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset + sink_depth, z_pos - sink_height)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset + sink_depth, z_pos)
    glVertex3f(x_pos + sink_width/2, y_pos + wall_offset, z_pos)
    
    
    glEnd()
    
    # Draw a simple tap/faucet
    glColor3f(0.9, 0.9, 0.92)
    glPushMatrix()
    glTranslatef(x_pos, y_pos + wall_offset + sink_depth - 1, z_pos + 15)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 3, 3, 15, 8, 1)
    glPopMatrix()
    
    # Draw a simple drain
    glColor3f(0.3, 0.1, 0) 
    glPushMatrix()
    glTranslatef(x_pos, y_pos + wall_offset + (sink_depth/2), z_pos - (sink_height+50))
    gluCylinder(gluNewQuadric(), drain_radius, drain_radius, z_pos - sink_height+4, 8, 1)
    glPopMatrix()
    
    glPopMatrix()
def key_box():
    glColor3f(0.9, 0.9, 0.92)
    glPushMatrix()
    glTranslatef(300,300, 10)
    glRotatef(90, 1, 0, 0)
    glutSolidCube(100)
    glPopMatrix()



def idle():
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """
    
    # Ensure the screen updates with the latest changes
    glutPostRedisplay()
    
    # Enable depth testing for correct rendering of overlapping objects
    glEnable(GL_DEPTH_TEST)
    
def setupCamera():
    """
    Configures the camera's projection and view settings.
    Uses a perspective projection and positions the camera to look at the target.
    """
    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix mode
    glLoadIdentity()  # Reset the projection matrix
    # Set up a perspective projection (field of view, aspect ratio, near clip, far clip)
    gluPerspective(fovY, 1.25, 0.1, 1500) # Think why aspect ratio is 1.25?
    glMatrixMode(GL_MODELVIEW)  # Switch to model-view matrix mode
    glLoadIdentity()  # Reset the model-view matrix

    
    # Default third-person camera
    x, y, z = camera_pos
    gluLookAt(x, y, z,          # Camera position
              200, 200, 0,      # Look-at center of grid
              0, 0, 1)    

def showScreen():
    global game_over,hero_life,game_score,missing_bullet,camera_pos,cheat_mode
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 800)  # Set viewport size
    setupCamera()  # Configure camera perspective
    grid()
    draw_sink(300,565)
    draw_sink(200,565)
    draw_pipes()
    draw_saw()
    key_box()
    glutSwapBuffers()
    
def specialKeyListener(key, x, y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global camera_pos
    x, y, z = camera_pos
    # Move camera up (UP arrow key)
    if key == GLUT_KEY_UP:
        x+=5

    # # Move camera down (DOWN arrow key)
    if key == GLUT_KEY_DOWN:
        x-=5 

    # moving camera left (LEFT arrow key)
    if key == GLUT_KEY_LEFT:
        y -= 10
         # Small angle decrement for smooth movement
    # moving camera right (RIGHT arrow key)
    if key == GLUT_KEY_RIGHT:
        y += 10  # Small angle increment for smooth movement
        
    camera_pos = (x, y, z)
def mouseListener(button, state, x, y):
    global camera_pos
    x, y, z = camera_pos
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
        z+=30
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN :
        z-=30
    camera_pos = (x, y, z)
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 800)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    glutCreateWindow(b"SAW")  # Create the window
    glutDisplayFunc(showScreen)  # Register display function
    # glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)

    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically
    glutMainLoop()  # Enter the GLUT main loop
    
if __name__ == "__main__":
    main()