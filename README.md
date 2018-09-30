
# Floyd Steinberg Image Dithering

[![N|Solid](https://user-images.githubusercontent.com/40122948/46173008-c1b81e80-c2ad-11e8-9fb6-fa435e114354.png)](https://py.processing.org/)


Floyd Steinberg's image dithering algorithm written with python and Processing

### Example
![](https://img00.deviantart.net/2b92/i/2018/273/1/0/image_dithering_by_itailv-dco6emp.png)

### How it works
The algorithm achieves dithering using error diffusion, meaning it pushes (adds) the residual quantization error of a pixel onto its neighboring pixels, to be dealt with later.
```python
for each y from top to bottom
   for each x from left to right
      oldpixel  := pixel[x][y]
      newpixel  := find_closest_palette_color(oldpixel)
      pixel[x][y]  := newpixel
      quant_error  := oldpixel - newpixel
      pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error * 7 / 16
      pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error * 3 / 16
      pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error * 5 / 16
      pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error * 1 / 16
```


