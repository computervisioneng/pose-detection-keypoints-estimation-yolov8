import ast
import os.path
from xml.dom import minidom


#### ONLY ONE OBJECT PER IMAGE IS ASSUMED ####

out_dir = './out'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

file = minidom.parse('annotations.xml')

images = file.getElementsByTagName('image')

for image in images:

    width = int(image.getAttribute('width'))
    height = int(image.getAttribute('height'))
    name = image.getAttribute('name')
    elem = image.getElementsByTagName('points')
    bbox = image.getElementsByTagName('box')[0]
    xtl = int(float(bbox.getAttribute('xtl')))
    ytl = int(float(bbox.getAttribute('ytl')))
    xbr = int(float(bbox.getAttribute('xbr')))
    ybr = int(float(bbox.getAttribute('ybr')))
    w = xbr - xtl
    h = ybr - ytl
    label_file = open(os.path.join(out_dir, name[:-4] + '.txt'), 'w')

    for e in elem:

        label_file.write('0 {} {} {} {} '.format(str((xtl + (w / 2)) / width), str((ytl + (h / 2)) / height),
                                                 str(w / width), str(h / height)))

        points = e.attributes['points']
        points = points.value.split(';')
        points_ = []
        for p in points:
            p = p.split(',')
            p1, p2 = p
            points_.append([int(float(p1)), int(float(p2))])
        for p_, p in enumerate(points_):
            label_file.write('{} {}'.format(p[0] / width, p[1] / height))
            if p_ < len(points_) - 1:
                label_file.write(' ')
            else:
                label_file.write('\n')
