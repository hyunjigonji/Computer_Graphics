import glfw
from OpenGL.GL import *
import numpy as np

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    #coordinate
    glBegin(GL_LINES)
    glColor3ub(255,0,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0,255,0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    #triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255,255,255)
    glVertex2fv( (T @ np.array([.0,.5,1.]))[:-1])
    glVertex2fv( (T @ np.array([.0,.0,1.]))[:-1])
    glVertex2fv( (T @ np.array([.5,.0,1.]))[:-1])
    glEnd()

def main():
    # Initialize the librarym 
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(480,480,"2017030191-2-2", None,None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
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

