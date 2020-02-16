from djongo import models

class Candidate(models.Model):
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    vote_count = models.IntegerField(default=0, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

