import io, os, sys
D=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,D)
from build import page, cover, refs, ABOUT
import g1,g2,g3
OUT=[("BPD_Overview",g1),("bpd_patient_guide_v6",g2),("bpd_loved_ones_guide_v2",g3)]
for name,g in OUT:
    body = cover(g.KICKER,g.TITLE,g.SUB,g.IMG) + g.BODY + ABOUT + refs(g.REFS,g.NOTE)
    io.open(os.path.join(D,name+".html"),"w",encoding="utf-8").write(page(g.TITLE,body))
    print("wrote",name+".html")
