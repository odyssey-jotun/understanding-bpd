import io, os, sys
D=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,D)
from build import page, cover, refs, about, ABOUT
import g1,g2,g3,g4
OUT=[("BPD_Overview",g1),("bpd_patient_guide_v6",g2),("bpd_loved_ones_guide_v2",g3)]
for name,g in OUT:
    body = cover(g.KICKER,g.TITLE,g.SUB,g.IMG) + g.BODY + ABOUT + refs(g.REFS,g.NOTE)
    io.open(os.path.join(D,name+".html"),"w",encoding="utf-8").write(page(g.TITLE,body))
    print("wrote",name+".html")

# Guide four follows the newer house rules: no small-caps eyebrows anywhere.
name = "bpd_guide_for_teens"
body = (cover("", g4.TITLE, g4.SUB, g4.IMG) + g4.BODY
        + about(kicker="", foot="Every guide in the series is free at")
        + refs(g4.REFS, g4.NOTE, kicker=None, cls="tight"))
io.open(os.path.join(D,name+".html"),"w",encoding="utf-8").write(page(g4.TITLE,body))
print("wrote",name+".html")
