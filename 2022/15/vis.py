from PIL import Image, ImageDraw, ImageFont

with open('sample_input.txt', 'r') as f:
    lines = [line[:-1].split() for line in f]

closest_beacons = dict()
beacon_distances = dict()

min_x , min_y = 10**100, 10**100
max_x, max_y = -1*10*100, -1*10*100 

def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

#Read in the data
for tokens in lines:
    x = int(tokens[2][2:-1])
    y = int(tokens[3][2:-1])
    
    xx = int(tokens[8][2:-1])
    yy = int(tokens[9][2:])
    closest_beacons[(x, y)] = (xx, yy)
    beacon_distances[(x, y)] = distance((x, y), (xx, yy))

# Find min and max potential x and y for the     
for sensor in beacon_distances:
    dist = beacon_distances[sensor]+1
    min_x = min((sensor[0] - dist, min_x))
    max_x = max((sensor[0] + dist, max_x))
    min_y = min((sensor[1] - dist, min_y))
    max_y = max((sensor[1] + dist, max_y))

board = [['.']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]

# Calculate the header rows so we don't have to recalculate them every time we print the board
max_y_width = max((len(str(min_y)), len(str(max_y)))) + 1
x_tickers = set([i for i in range(min_x, max_x+1) if i%5 == 0])
header_width = max([len(str(ticker)) for ticker in x_tickers])
header_rows = []
for r in range(header_width-1, -1, -1):
    row = [' ']*max_y_width
    for i in range(min_x, max_x+1):
        if i in x_tickers:
            if len(str(i)) > r:
                row.append(str(i)[::-1][r])
            else:
                row.append(' ')            
        else:
            row.append(' ')
    header_rows.append(''.join(row))


def generate_board_str():
    board_str_arr = []
    for row in header_rows:
        board_str_arr.append(row+'\n')
    for i, row in enumerate(board):
        board_str_arr.append(f'{i+min_y:<{max_y_width}}'+''.join([str(x) for x in row])+'\n')
    return ''.join(board_str_arr)

font_size = 40
fnt = ImageFont.truetype("/Users/aclavel/Library/Fonts/SourceCodePro-VariableFont_wght.ttf", font_size)
margin = 20
_, _, img_x, img_y = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textbbox((0, 0), generate_board_str(), font=fnt)
def board_str_to_image():
    out = Image.new("RGB", (img_x+2*margin, img_y+2*margin), (0, 0, 0))
    d = ImageDraw.Draw(out)
    board_str = generate_board_str()
    d.multiline_text((margin, margin), board_str, font=fnt, fill=(255,255,255))
    return out

pixel_size = 40
color_map = {
    'S': '#D000D0',
    'B': '#0000D0',
    '#': '#808080',
    1: '#400000',
    2: '#800000',
    3: '#D00000',
    4: '#FF0000',
    5: '#00FF00'
}
image_size = (pixel_size * len(board[0])+1, pixel_size * len(board[1])+1)
def board_to_image(board):
    out = Image.new("RGB", image_size, (0,0,0))
    d = ImageDraw.Draw(out)
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in color_map:
                start = (j*pixel_size, i*pixel_size)
                end = ((j+1)*pixel_size, (i+1)*pixel_size)
                d.rectangle([start, end], fill=color_map[board[i][j]])
    return out

def place(point, value):
    board[point[1] - min_y][point[0] - min_x] = value

def add_value(point):
    if board[point[1] - min_y][point[0] - min_x] == '.':
        board[point[1] - min_y][point[0] - min_x] = 1
    elif isinstance(board[point[1] - min_y][point[0] - min_x], int):
        board[point[1] - min_y][point[0] - min_x] += 1
    
# Initialize board with the sensors and Beacons
for sensor in closest_beacons:
    place(closest_beacons[sensor], 'B')
    place(sensor, 'S')

def render_basic_frame(max_dist):
    new_board = [row.copy() for row in board]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x+1):
            if new_board[y-min_y][x-min_x] == '.':
                for sensor in beacon_distances:
                    if distance(sensor, (x, y)) <= min((beacon_distances[sensor], max_dist)):
                        new_board[y-min_y][x-min_x] = '#'
    return board_to_image(new_board)

basic_frames = [render_basic_frame(x) for x in range(0, max(beacon_distances.values()))]
for _ in range(10):
    basic_frames.append(basic_frames[-1])
basic_frames[0].save('basic.gif', save_all=True, append_images = basic_frames[1:], duration=100, loop=0)

frames = []
for sensor in beacon_distances:
    dist = beacon_distances[sensor]
    x = sensor[0] - dist
    y = sensor[1]
    while x < sensor[0]:
        place((x, y), '#')
        add_value((x, y-1))
        x += 1
        y -= 1
        frames.append(board_to_image(board))
    add_value((x, y-1))
    frames.append(board_to_image(board))
    while y < sensor[1]:
        place((x, y), '#')
        add_value((x+1, y))
        x += 1
        y += 1
        frames.append(board_to_image(board))
    add_value((x+1, y))
    frames.append(board_to_image(board))
    while x > sensor[0]:
        place((x, y), '#')
        add_value((x, y+1))
        x -= 1
        y += 1
        frames.append(board_to_image(board))
    add_value((x, y+1))
    frames.append(board_to_image(board))
    while y > sensor[1]:
        place((x, y), '#')
        add_value((x-1, y))
        x -= 1
        y -= 1
        frames.append(board_to_image(board))
    add_value((x-1, y))
    frames.append(board_to_image(board))



for _ in range(10):
    frames.append(frames[-1])
frames[0].save('2022_day_15_vis.gif', save_all=True, append_images = frames[1:], duration = 40, loop=0)
