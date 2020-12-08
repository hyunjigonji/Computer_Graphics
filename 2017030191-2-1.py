import glfw
from OpenGL.GL import *
import numpy as np

v = np.linspace(0,np.pi*2,13)

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    if T == 1: glBegin(GL_POINTS)
    if T == 2: glBegin(GL_LINES)
    if T == 3: glBegin(GL_LINE_STRIP)
    if T == 4: glBegin(GL_LINE_LOOP)
    if T == 5: glBegin(GL_TRIANGLES)
    if T == 6: glBegin(GL_TRIANGLE_STRIP)
    if T == 7: glBegin(GL_TRIANGLE_FAN)
    if T == 8: glBegin(GL_QUADS)
    if T == 9: glBegin(GL_QUAD_STRIP)
    if T == 0: glBegin(GL_POLYGON)
    
    for i in range(0,12): glVertex2f(np.cos(v)[i],np.sin(v)[i])
    glEnd()

def press_key(window, key, scan, action, mods):
    global num
    if key == glfw.KEY_1:
        if(action == glfw.PRESS):
            num = 1
    if key == glfw.KEY_2:
        if(action == glfw.PRESS):
            num = 2
    if key == glfw.KEY_3:
        if(action == glfw.PRESS):
            num = 3
    if key == glfw.KEY_4:
        if(action == glfw.PRESS):
            num = 4
    if key == glfw.KEY_5:
        if(action == glfw.PRESS):
            num = 5
    if key == glfw.KEY_6:
        if(action == glfw.PRESS):
            num = 6
    if key == glfw.KEY_7:
        if(action == glfw.PRESS):
            num = 7
    if key == glfw.KEY_8:
        if(action == glfw.PRESS):
            num = 8
    if key == glfw.KEY_9:
        if(action == glfw.PRESS):
            num = 9
    if key == glfw.KEY_0:
        if(action == glfw.PRESS):
            num = 0

def main():
    # Initialize the librarym
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"2017030191-2-1", None,None)
    if not window:
        glfw.terminate()
        return
    
    # Make the window's context current
    glfw.set_key_callback(window, press_key)
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events
        glfw.poll_events()
        t = glfw.get_time()
    
        R = np.array([[np.cos(t),-np.sin(t),0.],[np.sin(t),np.cos(t),0.],[0.,0.,1.]])
        T = np.array([[1.,0.,.3],[0.,1.,.3],[0.,0.,1.]])
        
        # Render here, e.g. using pyOpenGL
        render(R @ T)
        
        # Swap front and back buffers
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()

