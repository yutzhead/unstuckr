# unstuckr: Fix stuck pixels.

Unstuckr intends to fix stuck pixel on your display by flashing solid colors on
the screen.

Unlike other software

- Your computer remains usable
- It doesn't give you seizures (especially when you only flash the stuck pixel)
- Flashes at full blast with the refresh frequency of the display

Usage: unstuckr.py [&lt;x&gt;] [&lt;y&gt;] [&lt;rectangle size&gt;] [&lt;rectangle size&gt;]

If started without options, unstuckr will display a black square. Move it with
the cursors above the stuck pixel, resize square with +/- and start flashing
by pressing *s*.

Colors are red, green, blue, white and sequence. sequence alternates between
red, green and blue and is the default.

If science is to be believed, flashing white or the individual color of the stuck
subpixel increases the frequency by 2/3 and may even work better.
