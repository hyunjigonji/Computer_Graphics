import glfw
from OpenGL.GL import *
import numpy as np

T = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]])

def render(T):
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	
	# draw cooridnate
	glBegin(GL_LINES)
	glColor3ub(255, 0, 0)
	glVertex2fv(np.array([0.,0.])) 
	glVertex2fv(np.array([1.,0.]))
	glColor3ub(0, 255, 0)
	glVertex2fv(np.array([0.,0.])) 
	glVertex2fv(np.array([0.,1.]))
	glEnd()
	
	# draw triangle
	glBegin(GL_TRIANGLES)
	glColor3ub(255, 255, 255)
	glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1] )
	glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1] )
	glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1] )
	glEnd()

def press_key(window, key, scan, action, mods):
    global T
    
    if key == glfw.KEY_Q:
        if(action == glfw.PRESS):
            T = np.array([[1.,0.,-0.1], [0.,1.,0.], [0.,0.,1.]]) @ T
    if key == glfw.KEY_E:
        if(action == glfw.PRESS):
            T = np.array([[1.,0.,0.1], [0.,1.,0.], [0.,0.,1.]]) @ T
    if key == glfw.KEY_A:
        if(action == glfw.PRESS):
            T = T @ np.array([[np.cos(np.pi*10/180),-np.sin(np.pi*10/180),0.], [np.sin(np.pi*10/180),np.cos(np.pi*10/180),0.], [0.,0.,1.]])
    if key == glfw.KEY_D:
        if(action == glfw.PRESS):
            T = T @ np.array([[np.cos(-np.pi*10/180),-np.sin(-np.pi*10/180),0.], [np.sin(-np.pi*10/180),np.cos(-np.pi*10/180),0.], [0.,0.,1.]])
    if key == glfw.KEY_1:
        if(action == glfw.PRESS):
            T = np.array([[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]]) 
    if key == glfw.KEY_W:
        if(action == glfw.PRESS):
            T = np.array([[0.9,0.,0.], [0.,1.,0.], [0.,0.,1.]]) @ T
    if key == glfw.KEY_S:
        if(action == glfw.PRESS):
            T = np.array([[np.cos(np.pi*10/180),-np.sin(np.pi*10/180),0.], [np.sin(np.pi*10/180),np.cos(np.pi*10/180),0.], [0.,0.,1.]]) @ T

def main():
    global T
    
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"2017030191-3-1", None,None)
    if not window:
        glfw.terminate()
        return

    glfw.set_key_callback(window, press_key)
    
    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll events
        glfw.poll_events()
        
        # Render here, e.g. using pyOpenGL
        render(T)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
