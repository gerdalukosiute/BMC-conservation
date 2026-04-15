# Load your structure manually before running these commands if needed
hide everything
show cartoon
spectrum b, blue_white_red, minimum=0, maximum=2.857163
set cartoon_transparency, 0.15
bg_color white
set color_missing, grey70
alter all, b=0.0
alter resi 1, b=2.772900
alter resi 2, b=1.573540
alter resi 3, b=2.183960
alter resi 4, b=2.534669
alter resi 5, b=2.099171
alter resi 6, b=2.664262
alter resi 7, b=1.881599
alter resi 8, b=2.857163
alter resi 9, b=2.777027
alter resi 10, b=1.901821
alter resi 11, b=2.493831
alter resi 12, b=2.226656
alter resi 13, b=1.892696
alter resi 14, b=2.857163
alter resi 15, b=2.857163
alter resi 16, b=2.716835
alter resi 17, b=1.865759
alter resi 18, b=1.550020
alter resi 19, b=2.020478
alter resi 20, b=1.725211
alter resi 21, b=2.857163
alter resi 22, b=2.071180
alter resi 23, b=2.098162
alter resi 24, b=2.226656
alter resi 25, b=2.857163
alter resi 26, b=1.670669
alter resi 27, b=2.857163
alter resi 28, b=1.940901
alter resi 29, b=2.018951
alter resi 30, b=2.358667
alter resi 31, b=2.537133
alter resi 32, b=1.234727
alter resi 33, b=2.098457
alter resi 34, b=2.857163
alter resi 35, b=0.974232
alter resi 36, b=1.630638
alter resi 37, b=1.049164
alter resi 38, b=2.584559
alter resi 39, b=0.934789
alter resi 40, b=0.745932
alter resi 41, b=1.666981
alter resi 42, b=1.926227
alter resi 43, b=2.226656
alter resi 44, b=1.849396
alter resi 45, b=2.857163
alter resi 46, b=2.857163
alter resi 47, b=2.636986
alter resi 48, b=2.457726
alter resi 49, b=2.857163
alter resi 50, b=2.857163
alter resi 51, b=1.201336
alter resi 52, b=2.857163
alter resi 53, b=2.857163
alter resi 54, b=2.664262
alter resi 55, b=2.857163
alter resi 56, b=2.857163
alter resi 57, b=2.857163
alter resi 58, b=1.735678
alter resi 59, b=1.873132
alter resi 60, b=2.857163
alter resi 61, b=2.857163
alter resi 62, b=2.857163
alter resi 63, b=2.857163
alter resi 64, b=2.857163
alter resi 65, b=2.857163
alter resi 66, b=2.857163
alter resi 67, b=0.848875
alter resi 68, b=1.498109
alter resi 69, b=2.857163
alter resi 70, b=1.205654
alter resi 71, b=2.100992
alter resi 72, b=2.857163
alter resi 73, b=2.857163
alter resi 74, b=2.493831
alter resi 75, b=2.857163
alter resi 76, b=2.532080
alter resi 77, b=2.616689
alter resi 78, b=2.777027
alter resi 79, b=2.857163
alter resi 80, b=2.857163
alter resi 81, b=2.493831
alter resi 82, b=2.777027
alter resi 83, b=2.857163
alter resi 84, b=0.815588
alter resi 85, b=1.810194
alter resi 86, b=1.140314
alter resi 87, b=1.382845
alter resi 88, b=1.024254
alter resi 89, b=2.096945
alter resi 90, b=1.306803
alter resi 91, b=0.000000
alter resi 92, b=1.971484
alter resi 93, b=2.219001
alter resi 94, b=0.713570
alter resi 95, b=2.857163
alter resi 96, b=1.945267
sort
rebuild
spectrum b, blue_white_red, minimum=0, maximum=2.857163
ramp_new conservation_ramp, all, [0, 2.857163], [blue, red]
show sticks, byres (resi 8+14+15+21+25+27+34+45+46+49+50+52+53+55+56)
set stick_radius, 0.2
