from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Camera-related variables
camera_pos = [0, 200, 500]  # Third-person camera position
camera_distance = 300  # Distance from character in third-person mode
camera_height = 150  # Height of camera in third-person mode
camera_mode = 0  # 0 = third person, 1 = first person
camera_angle_offset = 0  # Allows camera rotation around character
fovY = 90  # Field of view
GRID_LENGTH = 600  # Length of grid lines

# Character variables
character_pos = [0, 0, 0]  # Character position (x, y, z)
character_angle = 0  # Character rotation angle
moving_forward = 0
moving_backward = 0
turning_left = 0
turning_right = 0
animation_counter = 0  # For limb animation

# Character colors
HEAD_COLOR = (1.0, 0.8, 0.6)  # Skin tone
TORSO_COLOR = (0.2, 0.4, 0.8)  # Blue shirt
ARM_COLOR = (0.2, 0.5, 0.8)  # Blue sleeves
LEG_COLOR = (0.2, 0.2, 0.5)  # Dark blue pants
FOOT_COLOR = (0.1, 0.1, 0.1)  # Black shoes

# ----------------------------------------------------------------------------------------------
def draw_villain_hair():
    """Draw slick, elegant villain hair style"""
    glColor3f(0.05, 0.05, 0.05)  # Very dark hair (black)
    
    # Main hair volume on top
    glPushMatrix()
    glTranslatef(0, 165, 0)
    glScalef(1.2, 0.6, 1.0)
    glutSolidSphere(25, 20, 10)
    glPopMatrix()
    
    # Slicked back hair style
    for i in range(8):
        # Main slicked back sections
        glPushMatrix()
        offset_x = (i - 3.5) * 5  # Distribute across the head
        glTranslatef(offset_x, 150, -10 - i)
        glRotatef(70, 1, 0, 0)  # Angle back
        glScalef(1.0, 3.5, 0.5)  # Long, thin strands
        glutSolidCube(5)
        glPopMatrix()
    
    # Side hair patches (more subtle)
    for side in [-1, 1]:  # Left and right sides
        for i in range(3):
            glPushMatrix()
            glTranslatef(side * 22, 145 - i * 4, -5 - i * 2)
            glRotatef(60 * side, 0, 1, 0)  # Angle toward the side
            glRotatef(30, 1, 0, 0)  # Angle slightly down
            glScalef(0.8, 2.0, 0.6)
            glutSolidCube(6)
            glPopMatrix()
    
    # Styled front hair - subtle widow's peak
    for i in range(5):
        factor = abs(i - 2) / 2.0  # Creates a peak in the middle
        glPushMatrix()
        glTranslatef((i - 2) * 6, 150 - factor * 5, 20)
        glRotatef(-40, 1, 0, 0)  # Angle forward
        glScalef(0.8, 1.5 - factor * 0.5, 0.5)
        glutSolidCube(5)
        glPopMatrix()
    
    # Back of the neck hair
    for i in range(4):
        glPushMatrix()
        glTranslatef(0, 120 + i * 5, -15)
        glScalef(2.0, 0.8, 0.5)
        glutSolidCube(6)
        glPopMatrix()

def draw_spiral(radius=8, turns=3):
    """Draw a spiral using a line strip"""
    glBegin(GL_LINE_STRIP)
    for i in range(100):
        angle = 2 * math.pi * turns * i / 100
        r = radius * i / 100
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

def draw_villain_head():
    """Draw the Jigsaw-style villain head"""
    glPushMatrix()

    # Neck
    glColor3f(0.9, 0.9, 0.9)
    glTranslatef(0, 120, 0)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 10, 10, 15, 12, 1)

    # Head (scaled sphere)
    glColor3f(0.9, 0.9, 0.9)
    glTranslatef(0, 0, 20)
    glRotatef(90, 1, 0, 0)
    glPushMatrix()
    glScalef(1.0, 1.3, 0.9)
    gluSphere(gluNewQuadric(), 28, 20, 20)
    glPopMatrix()

    # Spiral cheeks
    glColor3f(0.9, 0.1, 0.1)
    glPushMatrix()
    glTranslatef(18, -10, 25)
    glScalef(0.8, 0.8, 0.8)
    draw_spiral()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-18, -10, 25)
    glScalef(0.8, 0.8, 0.8)
    draw_spiral()
    glPopMatrix()

    # Eyes: red sclera + black pupils
    for side in [10, -10]:
        glPushMatrix()

        glTranslatef(side, 0, 25)
        glColor3f(0, 0, 0)  # outside
        gluSphere(gluNewQuadric(), 7, 20, 20)

        glTranslatef(0, 0, 6)
        glColor3f(0.9, 0.1, 0.1)  # Red
        gluSphere(gluNewQuadric(), 5, 10, 5)

        glTranslatef(0, 0, 6)
        glColor3f(0, 0, 0)  # pupil
        gluSphere(gluNewQuadric(), 3, 10, 10)
        
        glPopMatrix()

    # Eyebrows
    glColor3f(0.1, 0.1, 0.1)
    glPushMatrix()
    glTranslatef(0, 10, 28)
    for side, angle in [(10, -25), (-10, 25)]:
        glPushMatrix()
        glTranslatef(side, 0, 0)
        glRotatef(angle, 0, 0, -60)
        glScalef(10, 2, 2)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()

    # Nose
    glColor3f(0.85, 0.85, 0.85)
    glPushMatrix()
    glTranslatef(0, 0, 25)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 5, 3, 15, 8, 1)
    glPopMatrix()

    # Mouth - angular red smile
    glPushMatrix()
    glTranslatef(0, -5, 25)
    glColor3f(0.9, 0.1, 0.1)
    glLineWidth(2.5)
    # glBegin(GL_LINE_STRIP)
    # for i in range(11):
    #     t = i / 10.0
    #     x = 20 * (2*t - 1)
    #     y = -5 * math.sin(math.pi * t)
    #     glVertex3f(x, y, 0)
    # glEnd()
    glPopMatrix()

    # # Optional jaw piece
    # glColor3f(0.8, 0.8, 0.8)
    # glPushMatrix()
    # glTranslatef(0, -25, 5)
    # glScalef(1.2, 0.5, 1.0)
    # glutSolidCube(25)
    # glPopMatrix()

    # Red bow tie
    glPushMatrix()
    glTranslatef(0, -40, 20)
    glColor3f(0.9, 0.1, 0.1)
    glPushMatrix()
    glScalef(5, 5, 5)
    glutSolidCube(1)
    glPopMatrix()
    for side, angle in [(-10, 20), (10, -20)]:
        glPushMatrix()
        glTranslatef(side, 0, 0)
        glRotatef(angle, 0, 0, 1)
        glScalef(15, 7, 3)
        glutSolidCube(1)
        glPopMatrix()
    glPopMatrix()

    glPopMatrix()


def draw_villain_torso():
    """Draw the villain's suited torso"""
    glPushMatrix()
    
    # Main torso - black suit
    glColor3f(0.1, 0.1, 0.1)  # Black suit
    glTranslatef(0, 60, 0)  # Position torso above ground
    
    # Suit jacket
    glPushMatrix()
    glScalef(1.1, 1.5, 0.6)  # Wide shoulders, slightly thinner
    glutSolidCube(50)
    glPopMatrix()
    
    # White shirt beneath
    glColor3f(0.9, 0.9, 0.9)  # White shirt
    glPushMatrix()
    glTranslatef(0, 0, 3)  # Slightly in front of jacket
    glScalef(0.5, 1.4, 0.1)
    glutSolidCube(50)
    glPopMatrix()
    
    # Suit lapels
    glColor3f(0.1, 0.1, 0.1)  # Black lapels
    
    # Left lapel
    glPushMatrix()
    glTranslatef(-12, 10, 4)
    glRotatef(-20, 1, 0, 0)
    glRotatef(-10, 0, 0, 1)
    glScalef(0.3, 0.7, 0.1)
    glutSolidCube(50)
    glPopMatrix()
    
    # Right lapel
    glPushMatrix()
    glTranslatef(12, 10, 4)
    glRotatef(-20, 1, 0, 0)
    glRotatef(10, 0, 0, 1)
    glScalef(0.3, 0.7, 0.1)
    glutSolidCube(50)
    glPopMatrix()
    
    glPopMatrix()

def draw_villain_arm(side_factor):
    """Draw a villain's arm (left or right based on side_factor)"""
    glPushMatrix()
    
    # Shoulder joint position - wider for suit look
    glTranslatef(side_factor * 35, 90, 0)
    
    # Suit sleeve (upper arm)
    glColor3f(0.1, 0.1, 0.1)  # Black suit
    glRotatef(20 * side_factor, 0, 0, 1)  # Angle arms slightly outward
    
    # Upper arm
    glPushMatrix()
    glScalef(0.5, 1, 0.5)
    glutSolidCube(40)
    glPopMatrix()
    
    # Elbow joint
    glTranslatef(0, -25, 0)
    
    # Lower arm - slightly angled forward
    glRotatef(20, 1, 0, 0)
    glPushMatrix()
    glScalef(0.4, 1, 0.4)
    glutSolidCube(30)
    glPopMatrix()
    
    # Hand - white gloves
    glTranslatef(0, -20, 0)
    glColor3f(0.9, 0.9, 0.9)  # White gloves
    gluSphere(gluNewQuadric(), 8, 10, 10)
    
    glPopMatrix()

def draw_villain_leg(side_factor):
    """Draw a villain's leg (left or right based on side_factor)"""
    glPushMatrix()
    
    # Hip joint position
    glTranslatef(side_factor * 15, 30, 0)
    
    # Upper leg - black pants
    glColor3f(0.1, 0.1, 0.1)  # Black pants
    
    # Upper leg
    glPushMatrix()
    glScalef(0.5, 1, 0.5)
    glutSolidCube(40)
    glPopMatrix()
    
    # Knee joint
    glTranslatef(0, -25, 0)
    
    # Lower leg
    glPushMatrix()
    glScalef(0.4, 1, 0.4)
    glutSolidCube(30)
    glPopMatrix()
    
    # Foot - black dress shoes
    glTranslatef(0, -20, 5)
    glColor3f(0.05, 0.05, 0.05)  # Shiny black shoes
    glPushMatrix()
    glScalef(1.1, 0.4, 1.8)  # Longer, more formal shoes
    glutSolidCube(12)
    glPopMatrix()
    
    glPopMatrix()

def draw_villain():
    """Draw the complete villain character"""
    glPushMatrix()
    
    # Move to villain position
    glTranslatef(villain_pos[0], villain_pos[1], villain_pos[2])
    glRotatef(villain_angle, 0, 1, 0)  # Rotate villain around y-axis
    
    # Draw all body parts
    draw_villain_torso()
    draw_villain_head()
    draw_villain_arm(1)    # Right arm
    draw_villain_arm(-1)   # Left arm
    draw_villain_leg(1)    # Right leg
    draw_villain_leg(-1)   # Left leg
    
    glPopMatrix()

# Add these variables to your global variables section
villain_pos = [300, 0, 300]  # Position the villain somewhere on the grid
villain_angle = 225  # Make villain face toward the character/player
villain_state = 0  # 0=idle, 1=following, 2=attacking

def update_villain():
    """Update villain position and state"""
    global villain_pos, villain_angle, villain_state
    
    # Calculate distance to player
    dx = character_pos[0] - villain_pos[0]
    dz = character_pos[2] - villain_pos[2]
    distance = math.sqrt(dx*dx + dz*dz)
    
    if distance < 500:  # Within sensing range
        # Calculate angle to face player
        target_angle = math.degrees(math.atan2(dx, dz))
        
        # Gradually rotate toward player
        angle_diff = (target_angle - villain_angle) % 360
        if angle_diff > 180:
            angle_diff -= 360
        
        # Smooth rotation
        if abs(angle_diff) > 2:
            villain_angle += angle_diff * 0.05
        
        # If close enough, move toward player
        if distance > 150:  # Keep some distance
            villain_state = 1  # Following state
            move_speed = 1.5  # Slower than player
            villain_pos[0] += move_speed * math.sin(math.radians(villain_angle))
            villain_pos[2] += move_speed * math.cos(math.radians(villain_angle))
        else:
            villain_state = 2  # Attack state
    else:
        villain_state = 0  # Idle state

# # Update the idle function to also update the villain
# def idle():
#     """Idle function that runs continuously"""
#     update_character()
    
#     update_camera()
#     glutPostRedisplay()

# Update the showScreen function to draw the villain
# def showScreen():
#     """Display function to render the game scene"""
#     # Clear color and depth buffers
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     glViewport(0, 0, 1000, 800)
    
#     setupCamera()  # Configure camera perspective
    

#     # Draw the character
#     # draw_character()
    
#     # Draw the villain
#     # draw_villain()
    
#     # Draw HUD with camera mode info
#     draw_hud()
    
#     # Swap buffers for smooth rendering
#     glutSwapBuffers()

# Update HUD to show villain info
# def draw_hud():
#     """Draw heads-up display with game information"""
#     glMatrixMode(GL_PROJECTION)
#     glPushMatrix()
#     glLoadIdentity()
#     glOrtho(0, 1000, 0, 800, -1, 1)
#     glMatrixMode(GL_MODELVIEW)
#     glPushMatrix()
#     glLoadIdentity()
    
#     # Display camera mode
#     glColor3f(1, 1, 1)
#     glRasterPos2f(10, 770)
#     mode_text = "Camera Mode: First Person" if camera_mode == 1 else "Camera Mode: Third Person"
#     for char in mode_text:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
#     # Display position info
#     glRasterPos2f(10, 750)
#     pos_text = f"Position: X={int(character_pos[0])}, Z={int(character_pos[2])}, Angle={int(character_angle)}"
#     for char in pos_text:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
#     # Display villain info
#     glRasterPos2f(10, 730)
    
#     # Calculate distance to villain
#     dx = character_pos[0] - villain_pos[0]
#     dz = character_pos[2] - villain_pos[2]
#     distance = int(math.sqrt(dx*dx + dz*dz))
    
#     villain_text = f"Villain: Distance={distance}, State={'Idle' if villain_state == 0 else 'Following' if villain_state == 1 else 'Attacking'}"
#     for char in villain_text:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
#     # Display controls
#     glRasterPos2f(10, 710)
#     basic_controls = "Controls: W,A,S,D to move, C or Right-click to toggle camera mode"
#     for char in basic_controls:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
#     glRasterPos2f(10, 690)
#     if camera_mode == 0:  # Third-person specific controls
#         camera_controls = "Camera: Arrow UP/DOWN to adjust height, LEFT/RIGHT to orbit, PAGE UP/DOWN for zoom"
#     else:  # First-person specific controls
#         camera_controls = "First-person view: Look in direction of movement"
    
#     for char in camera_controls:
#         glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
#     glPopMatrix()
#     glMatrixMode(GL_PROJECTION)
#     glPopMatrix()
#     glMatrixMode(GL_MODELVIEW)
# ----------------------------------------------------------------------------------------------



def draw_head():
    """Draw the character's head"""
    glPushMatrix()
    
    # Neck
    glColor3f(0.9, 0.7, 0.6)
    glTranslatef(0, 120, 0)  # Position neck on top of torso
    glRotatef(-90, 1, 0, 0)  # Rotate to align with y-axis
    gluCylinder(gluNewQuadric(), 10, 10, 15, 12, 1)
    
    # Head
    glColor3f(*HEAD_COLOR)
    glTranslatef(0, 0, 10)  # Move up to position head
    gluSphere(gluNewQuadric(), 25, 20, 20)  # Head sphere
    
    # Eyes
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)  # White eyes
    glTranslatef(10, -20, 0)
    gluSphere(gluNewQuadric(), 5, 10, 10)
    glColor3f(0.0, 0.0, 0.0)  # Black pupils
    glTranslatef(0, -3, 0)
    gluSphere(gluNewQuadric(), 2.5, 10, 10)
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)  # White eyes
    glTranslatef(-10, -20, 0)
    gluSphere(gluNewQuadric(), 5, 10, 10)
    glColor3f(0.0, 0.0, 0.0)  # Black pupils
    glTranslatef(0, -3, 0)
    gluSphere(gluNewQuadric(), 2.5, 10, 10)
    glPopMatrix()
    
    # Mouth
    glColor3f(0.8, 0.3, 0.3)
    glTranslatef(0, -10, -15)
    glScalef(10, 2, 5)
    glutSolidCube(1)
    
    glPopMatrix()

def draw_torso():
    """Draw the character's torso"""
    glPushMatrix()
    
    glColor3f(*TORSO_COLOR)
    glTranslatef(0, 60, 0)  # Position torso above ground
    glScalef(1.1, 1.5, 0.8)   # Scale to make it more torso-like
    glutSolidCube(50)       # Main torso
    
    glPopMatrix()

def draw_arm(side_factor):
    """Draw an arm (left or right based on side_factor)"""
    glPushMatrix()
    
    # Shoulder joint position
    glTranslatef(side_factor * 30, 90, 0)
    
    # Upper arm
    glColor3f(*ARM_COLOR)
    glRotatef(30 * side_factor * math.sin(animation_counter / 10), 1, 0, 0)  # Swing animation
    glTranslatef(0, -20, 0)  # Position arm down from shoulder
    
    # Upper arm
    glPushMatrix()
    glScalef(0.5, 1, 0.5)
    glutSolidCube(40)
    glPopMatrix()
    
    # Elbow joint
    glTranslatef(0, -25, 0)
    
    # Lower arm
    glRotatef(20 * side_factor * math.sin(animation_counter / 10 + 0.5), 1, 0, 0)  # Slightly offset swing
    glPushMatrix()
    glScalef(0.4, 1, 0.4)
    glutSolidCube(30)
    glPopMatrix()
    
    # Hand
    glTranslatef(0, -20, 0)
    glColor3f(*HEAD_COLOR)  # Skin tone for hands
    gluSphere(gluNewQuadric(), 8, 10, 10)
    
    glPopMatrix()

def draw_leg(side_factor):
    """Draw a leg (left or right based on side_factor)"""
    glPushMatrix()
    
    # Hip joint position
    glTranslatef(side_factor * 15, 30, 0)
    
    # Upper leg
    glColor3f(*LEG_COLOR)
    glRotatef(-30 * side_factor * math.sin(animation_counter / 10), 1, 0, 0)  # Opposite swing to arms
    
    # Upper leg
    glPushMatrix()
    glScalef(0.5, 1, 0.5)
    glColor3f(0.2,0.2,0.4)
    glutSolidCube(40)
    glPopMatrix()
    
    # Knee joint
    glTranslatef(0, -25, 0)
    
    # Lower leg
    glRotatef(-20 * side_factor * math.sin(animation_counter / 10 + 0.5), 1, 0, 0)  # Slightly offset swing
    glPushMatrix()
    glScalef(0.8, 1, 0.4)
    glutSolidCube(30)
    glPopMatrix()
    
    # Foot
    glTranslatef(0, -20, 5)
    glColor3f(*FOOT_COLOR)
    glPushMatrix()
    glScalef(1.2, 0.5, 1.5)
    glutSolidCube(12)
    glPopMatrix()
    
    glPopMatrix()

def draw_character():
    """Draw the complete character by assembling all parts"""
    glPushMatrix()
    
    # Move to character position
    glTranslatef(character_pos[0], character_pos[1]+15, character_pos[2])
    glRotatef(character_angle, 0, 1, 0)  # Rotate character around y-axis
    
    # Draw all body parts
    draw_torso()
    draw_head()
    draw_arm(1.2)   # Right arm
    draw_arm(-1.2)  # Left arm
    draw_leg(1)   # Right leg
    draw_leg(-1)  # Left leg
    
    glPopMatrix()

def update_character():
    """Update character position and animation"""
    global character_pos, character_angle, animation_counter
    
    # Update character animation counter
    if moving_forward or moving_backward:
        animation_counter += 1
    
    # Calculate movement direction
    movement_speed = 3.0
    if moving_forward:
        character_pos[0] += movement_speed * math.sin(math.radians(character_angle))
        character_pos[2] += movement_speed * math.cos(math.radians(character_angle))
    if moving_backward:
        character_pos[0] -= movement_speed * math.sin(math.radians(character_angle))
        character_pos[2] -= movement_speed * math.cos(math.radians(character_angle))
    
    # Update character rotation
    rotation_speed = 3.0
    if turning_left:
        character_angle += rotation_speed
    if turning_right:
        character_angle -= rotation_speed
    
    # Keep character within grid bounds
    grid_limit = GRID_LENGTH - 50
    character_pos[0] = max(-grid_limit, min(grid_limit, character_pos[0]))
    character_pos[2] = max(-grid_limit, min(grid_limit, character_pos[2]))

def update_camera():
    """Update camera position based on character and camera mode"""
    global camera_pos
    
    if camera_mode == 0:  # Third-person view
        # Calculate camera position with offset and rotation
        combined_angle_rad = math.radians(character_angle + camera_angle_offset)
        
        # Position camera behind and slightly above character
        camera_pos[0] = character_pos[0] - camera_distance * math.sin(combined_angle_rad)
        camera_pos[1] = character_pos[1] + camera_height
        camera_pos[2] = character_pos[2] - camera_distance * math.cos(combined_angle_rad)
    
    # First-person view is handled in setupCamera()

def keyboardListener(key, x, y):
    """Handles keyboard inputs for character movement and camera control"""
    global moving_forward, moving_backward, turning_left, turning_right, camera_mode
    global camera_angle_offset, camera_height, camera_distance
    
    # Movement controls
    if key == b'w':
        moving_forward += 1
    elif key == b's':
        moving_backward -= 1
    elif key == b'a':
        turning_left = True
    elif key == b'd':
        turning_right = True
    
    # Camera toggle
    elif key == b'c':
        camera_mode = 1 - camera_mode  # Toggle between 0 and 1
        # Reset camera parameters when switching to third-person
        if camera_mode == 0:
            camera_angle_offset = 0
    
    # Reset camera parameters with R key
    elif key == b'r':
        if camera_mode == 0:  # Third-person camera reset
            camera_height = 150
            camera_distance = 300
            camera_angle_offset = 0
    
    # Predefined camera positions with number keys (only in third-person)
    elif key == b'1' and camera_mode == 0:
        # Top-down view
        camera_height = 400
        camera_distance = 200
        camera_angle_offset = 0
    elif key == b'2' and camera_mode == 0:
        # Front view
        camera_height = 150
        camera_distance = 300
        camera_angle_offset = 180
    elif key == b'3' and camera_mode == 0:
        # Side view
        camera_height = 150
        camera_distance = 300
        camera_angle_offset = 90

def keyboardUpListener(key, x, y):
    """Handles keyboard key releases"""
    global moving_forward, moving_backward, turning_left, turning_right
    
    # Stop movement when keys are released
    if key == b'w':
        moving_forward = False
    elif key == b's':
        moving_backward = False
    elif key == b'a':
        turning_left = False
    elif key == b'd':
        turning_right = False

def specialKeyListener(key, x, y):
    """Handles special key inputs (arrow keys) for adjusting the camera angle and height"""
    global camera_height, camera_distance, camera_angle_offset
    
    # These controls only work in third-person mode
    if camera_mode == 0:
        # UP/DOWN arrows adjust camera height
        if key == GLUT_KEY_UP:
            camera_height += 10
            if camera_height > 400:  # Set a reasonable maximum height
                camera_height = 400
        elif key == GLUT_KEY_DOWN:
            camera_height -= 10
            if camera_height < 50:  # Set a reasonable minimum height
                camera_height = 50
        
        # LEFT/RIGHT arrows rotate camera around character
        elif key == GLUT_KEY_LEFT:
            camera_angle_offset += 5
        elif key == GLUT_KEY_RIGHT:
            camera_angle_offset -= 5
            
        # PAGE_UP/PAGE_DOWN adjust camera distance from character
        elif key == GLUT_KEY_PAGE_UP:
            camera_distance -= 20
            if camera_distance < 100:  # Set a reasonable minimum distance
                camera_distance = 100
        elif key == GLUT_KEY_PAGE_DOWN:
            camera_distance += 20
            if camera_distance > 500:  # Set a reasonable maximum distance
                camera_distance = 500

def mouseListener(button, state, x, y):
    """Handles mouse inputs"""
    global camera_mode, camera_angle_offset, camera_distance  # ← FIXED: include camera_distance here
    
    # Right mouse button toggles camera mode
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        camera_mode = 1 - camera_mode
        # Reset camera angle offset when switching modes
        if camera_mode == 0:
            camera_angle_offset = 0
    
    # Mouse wheel adjusts camera distance in third-person mode
    if camera_mode == 0:
        if button == 3:  # Scroll up - zoom in
            # global camera_distance
            camera_distance -= 20
            if camera_distance < 100:
                camera_distance = 100
        elif button == 4:  # Scroll down - zoom out
            # global camera_distance
            camera_distance += 20
            if camera_distance > 500:
                camera_distance = 500

def setupCamera():
    """Configures the camera's projection and view settings"""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    if camera_mode == 0:  # Third-person view
        # Use the camera position that's been updated to follow the character
        # Look at a point slightly above the character's base (head level)
        head_height = 100
        
        gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],  # Camera position
                  character_pos[0], character_pos[1] + head_height, character_pos[2],  # Look at character's head
                  0, 1, 0)  # Up vector (y-axis)
    else:  # First-person view
        # Position camera at character's eye level
        eye_height = 140  # Slightly lower than the top of the head
        
        # Calculate view direction - where the character is looking
        angle_rad = math.radians(character_angle)
        look_x = character_pos[0] + 100 * math.sin(angle_rad)
        look_y = character_pos[1] + eye_height +30 # Look slightly downward
        look_z = character_pos[2] + 100 * math.cos(angle_rad)
        
        # Position the camera where the character's eyes would be (slightly forward from center)
        eye_forward_offset = 20
        eye_x = character_pos[0] + eye_forward_offset * math.sin(angle_rad)
        eye_z = character_pos[2] + eye_forward_offset * math.cos(angle_rad)
        
        gluLookAt(eye_x, character_pos[1] + eye_height + 30, eye_z,  # Eye position
                 look_x, look_y, look_z,  # Look direction
                 0, 1, 0)  # Up vector (y-axis)

def idle():
    """Idle function that runs continuously"""
    update_character()
    update_camera()
    glutPostRedisplay()
    update_villain()  # Add this line

def showScreen():
    """Display function to render the game scene"""
    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)

    setupCamera()  # Configure camera perspective

    # Draw the grid (game floor)
    glBegin(GL_QUADS)
    
    glColor3f(1, 1, 1)
    glVertex3f(-GRID_LENGTH, 0, GRID_LENGTH)
    glVertex3f(0, 0, GRID_LENGTH)
    glVertex3f(0, 0, 0)
    glVertex3f(-GRID_LENGTH, 0, 0)

    glVertex3f(GRID_LENGTH, 0, -GRID_LENGTH)
    glVertex3f(0, 0, -GRID_LENGTH)
    glVertex3f(0, 0, 0)
    glVertex3f(GRID_LENGTH, 0, 0)

    glColor3f(0.7, 0.5, 0.95)
    glVertex3f(-GRID_LENGTH, 0, -GRID_LENGTH)
    glVertex3f(-GRID_LENGTH, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, -GRID_LENGTH)

    glVertex3f(GRID_LENGTH, 0, GRID_LENGTH)
    glVertex3f(GRID_LENGTH, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, GRID_LENGTH)
    glEnd()

    # Draw the character
    draw_character()
    # draw_villain()
    # draw_villain_hair()

    # Draw HUD with camera mode info
    draw_hud()

    # Swap buffers for smooth rendering
    glutSwapBuffers()

def draw_hud():
    """Draw heads-up display with game information"""
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 1000, 0, 800, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Display camera mode
    glColor3f(1, 1, 1)
    glRasterPos2f(10, 770)
    mode_text = "Camera Mode: First Person" if camera_mode == 1 else "Camera Mode: Third Person"
    for char in mode_text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    # Display position info
    glRasterPos2f(10, 750)
    pos_text = f"Position: X={int(character_pos[0])}, Z={int(character_pos[2])}, Angle={int(character_angle)}"
    for char in pos_text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
    # Display controls - different for each camera mode
    glRasterPos2f(10, 730)
    basic_controls = "Controls: W,A,S,D to move, C or Right-click to toggle camera mode"
    for char in basic_controls:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
    glRasterPos2f(10, 710)
    if camera_mode == 0:  # Third-person specific controls
        camera_controls = "Camera: Arrow UP/DOWN to adjust height, LEFT/RIGHT to orbit, PAGE UP/DOWN for zoom"
    else:  # First-person specific controls
        camera_controls = "First-person view: Look in direction of movement"
    
    for char in camera_controls:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def main():
    """Main function to set up OpenGL window and loop"""
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"3D Character Game")
    
    # Enable depth testing and lighting
    glEnable(GL_DEPTH_TEST)
    
    # Register callback functions
    glutDisplayFunc(showScreen)
    glutKeyboardFunc(keyboardListener)
    glutKeyboardUpFunc(keyboardUpListener)  # Handle key releases
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    
    # Enter the main loop
    glutMainLoop()

if __name__ == "__main__":
    main()