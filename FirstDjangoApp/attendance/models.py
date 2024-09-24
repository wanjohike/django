from django.db import models


class Attendance(models.Model):
	fname=models.CharField(max_length=50, blank=False, null=False)
	sname = models.CharField(max_length=50)
	
def __string__(self):
	return self.fname, self.sname

	



