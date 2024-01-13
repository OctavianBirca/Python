from datetime import datetime

class Period:
   
  def __init__(self,start,end):
    self.start = datetime.strptime(start, "%d.%m.%Y").date()
    self.end = datetime.strptime(end, "%d.%m.%Y").date()


  def  __str__(self):
    if self.start >= self.end:
        return f"ValueError"
         
    else:
        return f'{self.start.strftime("%d-%m-%Y")} – {self.end.strftime("%d-%m-%Y")}'
        





##############


