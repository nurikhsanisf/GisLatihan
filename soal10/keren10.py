import shapefile

w=shapefile.Writer('soal10/soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("wah","dua")


w.poly([[[-1,-1], [2,-6], [5,-1], [2,4], [-1,-1]]])
w.poly([[[-3,5], [-5,1], [-3,-3], [-1,1], [-3,5]]])