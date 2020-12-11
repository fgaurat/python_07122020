

class Todo:
    
    def __init__(self,title="",completed=False,dueDate=0):
        self._title = title
        self._completed = completed
        self._dueDate = dueDate
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title
    
    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self,completed):
        self._completed = completed
    
    @property
    def dueDate(self):
        return self._dueDate

    @dueDate.setter
    def dueDate(self,dueDate):
        self._dueDate = dueDate
    
    def __str__(self):
        return f"Todo : title={self._title}, completed={self._completed}, dueDate={self._dueDate} "