#! /usr/bin/env python3
import json
import pygame
import sys

def parse_dbjson(line):
    if line.strip().startswith("{"):
        data = line.strip()
        if data.endswith(','):
            data = data[:-1]
        star = json.loads(data)
        return star
    return None


def filter_db(dbjson, systems):
    """Return a version of the db with only the systems specified """

    counter = 0
    filter = []
    results = []
    with open(systems) as f:
        for line in f:
            filter.append(line.strip())

    with open(dbjson) as f:
        for line in f:
            star = parse_dbjson(line)
            if star:
                counter += 1
                if star['name'] in filter:
                    results.append(star)
            if counter%100000 == 0:
                print("Parsed %d systems"%counter)

    output = ""
    output += "[\n"
    i = 0
    counter = len(results)
    for r in results:
        output += json.dumps(r)
        i += 1
        if i < counter:
            output += ","
        output += "\n"
    output += "]"
    return output

def draw_systems(dbjson, canvas_size=2048, color=(255,255,0)):
    counter = 0
    surf = pygame.Surface((canvas_size, canvas_size), pygame.SRCALPHA)
    surf.fill((0,0,0,0))
    with open(dbjson) as f:
        for line in f:
            star = parse_dbjson(line)
            if star:
                counter += 1
                point = bind_coords(star['coords']['x'], star['coords']['y'], star['coords']['z'])
                surf.set_at(point,color)
            if counter%100000 == 0:
                print("Parsed %d systems"%counter)
    return surf

def collect_all_systems():
    visited = filter_db("systemsWithCoordinates.json", 'all.txt')
    open('systems-visited.json', 'w').write(visited)
    discovered = filter_db('systems-visited.json', 'first.txt')
    open('systems-discovered.json', 'w').write(discovered)


def draw_my_layers(canvas_size=2048):
    bg = pygame.image.load("backgroundMap.png")
    fg = pygame.image.load("galregions.png")
    explored = draw_systems("systems-visited.json", canvas_size, color=(255,255,0))
    discovered = draw_systems("systems-discovered.json", canvas_size, color=(0,255,0))
    bg.blit(explored, (0,0))
    bg.blit(discovered, (0,0))
    bg.blit(fg, (0,0))
    pygame.image.save(bg, "results.png")


def bind_coords(x , y , z, canvas_size=2048):
    clamp_galsize = 50000.0
    clamp_canvas = canvas_size//2

    _x = x - 25.21875
    _y = y + 20.90625
    _z = z - 25899.96875

    pixel_x = int( (_x / clamp_galsize * clamp_canvas) + clamp_canvas)
    pixel_y = int(-(_z / clamp_galsize * clamp_canvas) + clamp_canvas)

    return pixel_x, pixel_y


if __name__=="__main__":
    if sys.argv[1] == 'parse':
        collect_all_systems()
    elif sys.argv[1] == 'draw':
        draw_my_layers()
    
