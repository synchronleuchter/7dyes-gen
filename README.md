# Generator for 7Dyes instances
## General information
I haven't gotten around to writing good documentation for this. In short, this is a Python program that generates mods like the one I made called *7dyes*.

It originally came to be in a night with far too little sleep, a keyboard malfunction and an obsession with color. It generates recipes for dyes in *7 Days to Die*.

For details, please look inside the code. There should be a comment or two around the places you can change if you want more, less, different or differently sampled colors.

One thing I can say upfront: **Check the generated preview palette**. `7dyes-gen` generates a couple of images showing you what colors are created. Conceptually, it samples an HSV color cone and a grayscale line.

Gameplay-wise, you must find 7Dyes bottles and open them to get their pigment powder which you can then mix to get dye again. This dye can then be darkened or made paler with black or white dye which you can craft from coal or nitrate, respectively.

If you open a dye bottle, you get back the pigment powder or a part of the coal and nitrate involved if it's grayscale.

Since by mixing, you get back 2 bottles, you can infinitely replicate the pigments you already found. This is by design. Collect dye pigments like they're achievements! 😁

## Important
**Backup your world before using this mod!** Pushed versions may be bugged and brick your world. I develop this for me personally, so not every version is stable. Sorry for that.