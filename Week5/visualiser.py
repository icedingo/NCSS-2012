import sys

import pygame

HEIGHT = 600
WIDTH  = 600

COLOURS = {
  'black': (0, 0, 0),
  'blue': (0, 0, 200),
  'green': (0, 200, 0),
  'red': (255, 0, 0),
  'white': (255, 255, 255),
  'yellow': (200, 200, 50),
}

T_CITY, T_LINE, T_SATELLITE = range(3)

R_EARTH = 6353000.0


def read_dump(filename):
  ticks, xs, ys = [], [], []
  with open(filename, 'rU') as f:
    tick = []
    for line in f:
      line = line.strip()
      if not line:
        ticks.append(tick)
        tick = []
      else:
        cols = line.split()
        if cols[0] == 'satellite':
          assert len(cols) == 3
          x = float(cols[1])
          y = float(cols[2])
          tick.append((T_SATELLITE, x, y))
          xs.append(x)
          ys.append(y)
        elif cols[0] == 'city':
          assert len(cols) == 4
          label = cols[1]
          x = float(cols[2])
          y = float(cols[3])
          xs.append(x)
          ys.append(y)
          tick.append((T_CITY, label, x, y))
        elif cols[0] == 'line':
          assert len(cols) == 6
          colour = cols[1].lower()
          if colour not in COLOURS:
            raise ValueError('Unknown colour %r' % cols[1])
          x1 = float(cols[2])
          y1 = float(cols[3])
          x2 = float(cols[4])
          y2 = float(cols[5])
          tick.append((T_LINE, COLOURS[colour], x1, y1, x2, y2))
          xs += [x1, x2]
          ys += [y1, y2]
        else:
          raise ValueError('Unexpected type %r' % cols[0])

  xs.sort()
  ys.sort()

  width = max(abs(xs[-1]), abs(xs[0])) * 2
  height = max(abs(ys[-1]), abs(ys[0])) * 2

  return ticks, width, height


def main(filename):
  # read the dump file
  ticks, width, height = read_dump(filename)

  # work out scaling factor
  SCALE = min(WIDTH / width, HEIGHT / height)
  OFF_X = WIDTH / 2.0
  OFF_Y = HEIGHT / 2.0

  # init pygame
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  clock = pygame.time.Clock()
  tick = 0

  # event loop
  while 1:
    print tick

    # handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        return

    # tick and black
    clock.tick(100)  # make this number larger to speed up the visualisation
    screen.fill(COLOURS['black'])

    # draw the Earth
    pygame.draw.circle(screen, COLOURS['white'], (int(OFF_X), int(OFF_Y)), int(R_EARTH*SCALE))

    # draw the shapes
    for shape in ticks[tick]:
      if shape[0] == T_LINE:
        _, colour, x1, y1, x2, y2 = shape
        p1 = (int(x1*SCALE + OFF_X), int(y1*SCALE + OFF_Y))
        p2 = (int(x2*SCALE + OFF_X), int(y2*SCALE + OFF_Y))
        pygame.draw.line(screen, colour, p1, p2)
      elif shape[0] == T_CITY:
        _, label, x, y = shape
        p = (int(x*SCALE + OFF_X), int(y*SCALE + OFF_Y))
        pygame.draw.circle(screen, COLOURS['red'], p, 3)
      else:
        _, x, y = shape
        p = (int(x*SCALE + OFF_X), int(y*SCALE + OFF_Y))
        pygame.draw.circle(screen, COLOURS['green'], p, 3)

    # repaint
    pygame.display.flip()

    tick = (tick + 1) % len(ticks)


if __name__ == '__main__':
  filename = 'dump.txt'
  if len(sys.argv) == 2:
    filename = sys.argv[1]
  main(filename)
