import argparse
import os.path
import io
import numpy as np
import slice
import stl_reader
import perimeter
from util import arrayToWhiteGreyscalePixel, padVoxelArray
import json

def voxelsFromStl (inputFilePath, resolution):
    mesh = list(stl_reader.read_stl_verticies(inputFilePath))
    (scale, shift, bounding_box) = slice.calculateScaleAndShift(mesh, resolution)
    mesh = list(slice.scaleAndShiftMesh(mesh, scale, shift))
    #Note: vol should be addressed with vol[z][x][y]
    vol = np.zeros((bounding_box[2],bounding_box[0],bounding_box[1]), dtype=bool)
    for height in range(bounding_box[2]):
        # print('Processing layer %d/%d'%(height+1,bounding_box[2]))
        lines = slice.toIntersectingLines(mesh, height)
        prepixel = np.zeros((bounding_box[0], bounding_box[1]), dtype=bool)
        perimeter.linesToVoxels(lines, prepixel)
        vol[height] = prepixel
    vol, bounding_box = padVoxelArray(vol)
    # outputFilePattern, outputFileExtension = os.path.splitext(outputFilePath)
    return vol

def file_choices(choices,fname):
    filename, ext = os.path.splitext(fname)
    if ext == '' or ext not in choices:
        if len(choices) == 1:
            parser.error('%s doesn\'t end with %s'%(fname,choices))
        else:
            parser.error('%s doesn\'t end with one of %s'%(fname,choices))
    return fname

# TODO support resolution intead
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert STL files to voxels')
    parser.add_argument('input', nargs='?', type=lambda s:file_choices(('.stl'),s))
    parser.add_argument('resolution', nargs='?', type=int, default=100)
    args = parser.parse_args()
    voxels = voxelsFromStl(args.input, args.resolution)
    print(json.dumps(voxels.tolist()))
