from django.db import models

# Create your models here.

class Tutee(models.Model):
    ''' Model representing tutee's details'''
    name = models.CharField(max_length=25, help_text='Name of Tutee')
    email = models.EmailField(max_length=254)
    mobile_no = models.IntegerField()
    subjects = models.CharField(max_length=200, help_text='Subjects')
    TIME_OF_DAY = (
    ('0', '08:00-09:00'),
    ('1', '09:00-10:00'),
    ('2', '10:00-11:00'),
    ('3', '11:00-12:00'),
    ('4', '12:00-13:00'),
    ('5', '13:00-14:00'),
    ('6', '14:00-15:00'),
    ('7', '15:00-16:00'),
    ('8', '16:00-17:00'),
    ('9', '17:00-18:00'),
    ('10', '18:00-19:00'),
    ('11', '19:00-20:00'),
    ('12', '20:00-21:00'),
    ('13', '21:00-22:00')
    )
    timeslot = models.CharField(max_length=2, choices=TIME_OF_DAY, default=0)
    DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
    )


    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK, default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        '''String for representing model object'''
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this tutee."""
        return reverse('tutee-detail', args=[str(self.id)])

class Tutor(models.Model):
    ''' Model representing tutor's details'''
    name = models.CharField(max_length=25, help_text='Name of Tutor')
    email = models.EmailField(max_length=254)
    mobile_no = models.IntegerField()
    grade = models.CharField(max_length=5)
    subjects = models.CharField(max_length=200, help_text='Subjects')
    TIME_OF_DAY = (
    ('0', '08:00-09:00'),
    ('1', '09:00-10:00'),
    ('2', '10:00-11:00'),
    ('3', '11:00-12:00'),
    ('4', '12:00-13:00'),
    ('5', '13:00-14:00'),
    ('6', '14:00-15:00'),
    ('7', '15:00-16:00'),
    ('8', '16:00-17:00'),
    ('9', '17:00-18:00'),
    ('10', '18:00-19:00'),
    ('11', '19:00-20:00'),
    ('12', '20:00-21:00'),
    ('13', '21:00-22:00')
    )
    timeslot = models.CharField(max_length=2, choices=TIME_OF_DAY, default=0)
    DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
    )

    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK, default=0)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        '''String for representing model object'''
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this tutor."""
        return reverse('tutor-detail', args=[str(self.id)])




