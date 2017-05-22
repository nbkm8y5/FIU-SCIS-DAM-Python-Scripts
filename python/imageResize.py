# -*- coding: UTF-8 -*-
from __future__ import print_function
import os, sys
from PIL import Image

# or read in a file
data = [
"/disk/assets/upload/2017/5/1494352027291-girls-who-code-club-parent-and-community-night-dsc_5044_33854307716_o.jpg"
,
"/disk/assets/upload/2017/5/1494352028437-girls-who-code-club-parent-and-community-night-dsc_5064_33765983921_o.jpg"
,
"/disk/assets/upload/2017/5/1494352028054-girls-who-code-club-parent-and-community-night-dsc_5062_33854308076_o.jpg"
,
 "/disk/assets/upload/2017/5/1494352027674-girls-who-code-club-parent-and-community-night-dsc_5060_33854308196_o.jpg"
,
 "/disk/assets/upload/2017/5/1494352029170-girls-who-code-club-parent-and-community-night-dsc_5076_33854307786_o.jpg"
,
"/disk/assets/upload/2017/5/1494352029542-girls-who-code-club-parent-and-community-night-dsc_5077_33895361245_o.jpg"
,
"/disk/assets/upload/2017/5/1494352029897-girls-who-code-club-parent-and-community-night-dsc_5079_33854309216_o.jpg"
,
"/disk/assets/upload/2017/5/1494352030306-girls-who-code-club-parent-and-community-night-dsc_5082_33854309196_o.jpg"
,
"/disk/assets/upload/2017/5/1494352030679-girls-who-code-club-parent-and-community-night-dsc_5086_33854309476_o.jpg"
,
"/disk/assets/upload/2017/5/1494352028850-girls-who-code-club-parent-and-community-night-dsc_5066_33854308866_o.jpg"
,
"/disk/assets/upload/2017/5/1494352031419-girls-who-code-club-parent-and-community-night-dsc_5092_33854309706_o.jpg"
,
"/disk/assets/upload/2017/5/1494352031818-girls-who-code-club-parent-and-community-night-dsc_5098_33854309846_o.jpg"
,
"/disk/assets/upload/2017/5/1494352031017-girls-who-code-club-parent-and-community-night-dsc_5089_33895361545_o.jpg"
,
"/disk/assets/upload/2017/5/1494352032766-girls-who-code-club-parent-and-community-night-dsc_5145_33854310146_o.jpg"
,
"/disk/assets/upload/2017/5/1494352033221-girls-who-code-club-parent-and-community-night-dsc_5147_33082205963_o.jpg"
,
"/disk/assets/upload/2017/5/1494352034074-girls-who-code-club-parent-and-community-night-dsc_5170_33854310506_o.jpg"
,
"/disk/assets/upload/2017/5/1494352034491-girls-who-code-club-parent-and-community-night-dsc_5171_33082206483_o.jpg"
,
"/disk/assets/upload/2017/5/1494352033634-girls-who-code-club-parent-and-community-night-dsc_5148_33854310696_o.jpg"
,
"/disk/assets/upload/2017/5/1494352032211-girls-who-code-club-parent-and-community-night-dsc_5101_33082205443_o.jpg"
,
"/disk/assets/upload/2017/5/1494352034860-girls-who-code-club-parent-and-community-night-dsc_5173_33765986961_o.jpg"
,
"/disk/assets/upload/2017/5/1494352035251-girls-who-code-club-parent-and-community-night-dsc_5194_33082206993_o.jpg"
,
"/disk/assets/upload/2017/5/1494352035685-girls-who-code-club-parent-and-community-night-dsc_5195_33854311076_o.jpg"
,
"/disk/assets/upload/2017/5/1494352036911-girls-who-code-club-parent-and-community-night-dsc_5208_33082208273_o.jpg"
,
"/disk/assets/upload/2017/5/1494352036566-girls-who-code-club-parent-and-community-night-dsc_5207_33765987231_o.jpg"
,
"/disk/assets/upload/2017/5/1494352037263-girls-who-code-club-parent-and-community-night-dsc_5210_33854311626_o.jpg"
,
"/disk/assets/upload/2017/5/1494352037637-girls-who-code-club-parent-and-community-night-dsc_5211_33765987701_o.jpg"
,
"/disk/assets/upload/2017/5/1494352038048-girls-who-code-club-parent-and-community-night-dsc_5225_33765988331_o.jpg"
,
"/disk/assets/upload/2017/5/1494352036108-girls-who-code-club-parent-and-community-night-dsc_5201_33854311506_o.jpg"
,
"/disk/assets/upload/2017/5/1494352038949-girls-who-code-club-parent-and-community-night-dsc_5235_33765988061_o.jpg"
,
"/disk/assets/upload/2017/5/1494352039417-girls-who-code-club-parent-and-community-night-dsc_5242_33854312176_o.jpg"
,
"/disk/assets/upload/2017/5/1494352039798-girls-who-code-club-parent-and-community-night-dsc_5249_33854312406_o.jpg"
,
"/disk/assets/upload/2017/5/1494352038487-girls-who-code-club-parent-and-community-night-dsc_5233_33765988451_o.jpg"
]

for i in data:
    # print(i)

    try:
        im = Image.open(i)
        outfile = i.replace('/disk/assets', '/disk/assets/thumbnails')

        size = (im.size[0] * .1, im.size[1]* .1)

        # print(size)
    
        # print (im.format, im.size, im.mode)
        # print(outfile)

        im.thumbnail(size)
        im.save(outfile, "JPEG")
    except IOError:
            print("cannot create thumbnail for", i)