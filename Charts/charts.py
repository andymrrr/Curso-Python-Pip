import matplotlib.pyplot as pylot

def generate_pie_chart():
    Labels =['A','B','C']
    values =[200,34,120]
    fig,ax = pylot.subplots()
    ax.pie(values, labels=Labels)
    pylot.savefig('pie.png')
    pylot.close()