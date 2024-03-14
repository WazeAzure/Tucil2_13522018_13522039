import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i, animation_data):
  # Update data based on animation_data and frame number (i)
  line, = animation_data['ax'].plot(animation_data['data'][i])
  # Add any specific initialization logic here based on animation_data
  return line  # Returning the artist allows for updates

N = 3
fig, ax = plt.subplots()
animations = []
for i in range(N):
  # Define data for each animation
  data = [1, 2, 3]
  # Create subplot for each animation (optional)
  ax = fig.add_subplot(111)
  animations.append({'ax': ax, 'data': data})

previous_ani = None
for animation_data in animations:
  print(len(animation_data['data']))
  ani = animation.FuncAnimation(fig, animate, frames=len(animation_data['data']), 
                                 interval=10, fargs=(animation_data,))
  if previous_ani is not None:
    # Set _start_func only if there's a previous animation
    ani._start_func = previous_ani._end_func
  previous_ani = ani
