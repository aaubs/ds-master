"""Rebuild the four teaching diagrams: python render_diagrams.py."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

OUT = Path(__file__).parent
NAVY, TEAL, GRAY, AMBER = '#211a52', '#187c80', '#54616e', '#b87322'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': NAVY})

def canvas(title, subtitle):
    fig, ax = plt.subplots(figsize=(14, 7), dpi=160)
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 14), ylim=(0, 7)); ax.axis('off')
    ax.text(.35, 6.65, title, fontsize=25, weight='bold', va='top')
    ax.text(.35, 6.08, subtitle, fontsize=12, color=GRAY, va='top')
    return fig, ax

def table(ax, x, y, headers, rows, widths, colors=None, size=12):
    h=.46
    for i, row in enumerate([headers]+rows):
        xx=x
        for j, (s,w) in enumerate(zip(row, widths)):
            fc=NAVY if i==0 else (colors[i-1] if colors else '#f1f2f3')
            ax.add_patch(Rectangle((xx,y-(i+1)*h), w,h, facecolor=fc, edgecolor='white', linewidth=2))
            ax.text(xx+.11,y-(i+.5)*h,str(s),va='center',fontsize=size,color='white' if i==0 else NAVY)
            xx+=w
    return y-(len(rows)+1)*h

def arrow(ax, a,b,label=None):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color=TEAL,lw=2))
    if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.25,label,ha='center',fontsize=11,color=TEAL)

def save(fig,name):
    fig.savefig(OUT/name,bbox_inches='tight',pad_inches=.18,facecolor='white');plt.close(fig)

fig,ax=canvas('One question, three representations','Which courses are free? The condition stays the same; the way we express it changes.')
table(ax,.4,5.3,['course','price'],[['A',0],['B',45],['C',0],['D',100]],[1.3,1.2],['#d9efed','#f1f2f3','#d9efed','#f1f2f3'])
ax.text(3.55,5.12,'PYTHON  •  one record at a time',fontsize=12,weight='bold')
ax.text(3.55,4.66,'for course in courses:\n    if course["price"] == 0:\n        free.append(course)',fontfamily='monospace',fontsize=13,linespacing=1.6,va='top')
ax.text(.4,2.4,'NUMPY  •  positions',fontsize=12,weight='bold')
ax.text(.4,1.98,'prices = np.array([0, 45, 0, 100])\nprices == 0  →  [True, False, True, False]',fontfamily='monospace',fontsize=12,linespacing=1.7,va='top')
ax.text(7.65,2.4,'PANDAS  •  labeled rows',fontsize=12,weight='bold')
ax.text(7.65,1.98,'is_free = df["price"] == 0\ndf.loc[is_free, ["course", "price"]]',fontfamily='monospace',fontsize=12,linespacing=1.7,va='top')
table(ax,10.8,5.3,['course','price'],[['A',0],['C',0]],[1.3,1.2],['#d9efed','#d9efed'])
arrow(ax,(8.9,4.4),(10.5,4.4),'keep True')
ax.text(.4,.38,'A mask is a yes/no decision for every row. In pandas, the mask also carries index labels.',fontsize=13,color=TEAL)
save(fig,'loop_to_mask.png')

fig,ax=canvas('Group → calculate → one row per group','Before you aggregate, say what one input row represents and what one output row will represent.')
table(ax,.4,5.0,['subject','enrollments'],[['Web',10],['Business',5],['Web',20],['Business',15]],[1.5,1.6],['#d9efed','#faead6','#d9efed','#faead6'])
arrow(ax,(3.7,3.7),(4.9,3.7),'groupby')
table(ax,5.2,5.0,['Web'],[[10],[20]],[1.6],['#d9efed']*2)
table(ax,5.2,3.15,['Business'],[[5],[15]],[1.6],['#faead6']*2)
arrow(ax,(7.2,3.7),(8.7,3.7),'sum')
table(ax,9,5.0,['subject','total'],[['Business',20],['Web',30]],[1.9,1.5],['#faead6','#d9efed'])
ax.text(.4,1.2,'df.groupby("subject")["enrollments"].sum()',fontsize=18,fontfamily='monospace')
ax.text(.4,.5,'Input: one row per course.  Output: one row per subject.  Add a count to show how much data supports each result.',fontsize=12,color=TEAL)
save(fig,'split_apply_combine.png')

fig,ax=canvas('A join matches every compatible pair','Duplicate keys on the lookup side can multiply rows. Predict the row count before you merge.')
table(ax,.4,5.05,['membership','track_id'],[['P1','A'],['P2','A']],[1.65,1.25])
table(ax,4.25,5.05,['track_id','energy'],[['A',.8],['A',.8]],[1.25,1.3],['#faead6']*2)
arrow(ax,(7.15,4.1),(8.45,4.1),'merge')
table(ax,8.7,5.05,['membership','track_id','energy'],[['P1','A',.8],['P1','A',.8],['P2','A',.8],['P2','A',.8]],[1.65,1.25,1.2],size=11)
ax.text(.4,2.25,'2 left rows × 2 matches each = 4 output rows',fontsize=21,weight='bold',color=AMBER)
ax.text(.4,1.5,'memberships.merge(tracks, on="track_id", how="left",\n                  validate="many_to_one")',fontfamily='monospace',fontsize=15,linespacing=1.55,va='top')
ax.text(.4,.3,'The validation rejects this lookup table. Investigate repeated keys; keep one row per track only when justified.',fontsize=12,color=TEAL)
save(fig,'join_cardinality.png')

fig,ax=canvas('Reshape changes the layout','Long format supports grouping and plotting. Wide format makes comparisons across columns easy.')
table(ax,.4,5.05,['genre','metric','mean'],[['pop','energy',.7],['pop','danceability',.8],['rock','energy',.9],['rock','danceability',.5]],[1.1,1.95,1.0])
table(ax,9,5.05,['genre','energy','danceability'],[['pop',.7,.8],['rock',.9,.5]],[1.1,1.25,1.85],size=11)
arrow(ax,(4.9,4.55),(8.5,4.55),'pivot_table: long → wide')
arrow(ax,(8.5,3.4),(4.9,3.4),'melt: wide → long')
ax.text(.4,1.8,'pivot_table(..., aggfunc="mean") can combine multiple rows into a mean.',fontsize=16,weight='bold')
ax.text(.4,1.14,'melt() changes the layout back; it cannot recover observations lost in an aggregation.',fontsize=14)
ax.text(.4,.48,'An empty combination is missing data, not evidence that its mean equals zero. Values shown here are illustrative.',fontsize=12,color=TEAL)
save(fig,'reshape.png')
