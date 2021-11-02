import shapefile

w=shapefile.Writer('soal9/soal9',shapeType=shapefile.POLYLINE)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")



w.line([[[1,3],[5,3], [5,2],[1,2], [1,3]]])
w.line([[[1,6],[5,6], [5,9],[1,9], [1,6]]])