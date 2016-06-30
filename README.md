# stl-to-voxel

Turn STL files into a three-dimensional array of boolean values.

## install

```
git clone https://github.com/elsehow/stl-to-voxel.git
```

You will need python3, and you will need to `pip3 install numpy` if you don't have numpy already.

## use

```
python3 stltovoxel.py nickedtorus.stl 100
```

This will produce a voxelized image of the stl with a resolution of 100.
The result will be printed to `stdout`, as JSON.

This code is a boiled-down version of [rcpedersen's stl-to-voxel](https://github.com/rcpedersen/stl-to-voxel) library, which translated these arrays into images or videos. Demo on the Stanford bunny below, for eye candy / posterity.

![alt text](https://github.com/elsehow/stl-to-voxel/raw/master/stanford_bunny.png "STL version of the stanford bunny")
![alt text](https://github.com/elsehow/stl-to-voxel/raw/master/stanford_bunny.gif "voxel version of the stanford bunny")
