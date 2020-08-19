from django.db import models


class Movie(models.Model):
    """
    represent movie
   """

    class Meta:
        verbose_name = 'فيلم'
        verbose_name_plural = 'فيلم'

    name = models.CharField('عنوان', max_length=100)
    director = models.CharField('كارگردان', max_length=50)
    year = models.IntegerField('سال توليد')
    length = models.IntegerField('مدت زمان')
    description = models.TextField('توضيحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
   Respernst a cinma saloon
   """

    class Meta:
        verbose_name = 'سينما'
        verbose_name_plural = 'سينما'

    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField('نام سينما', max_length=50)
    city = models.CharField('شهر', max_length=30, default='تهران')
    capacity = models.IntegerField('ظرفيت')
    phone = models.CharField('شماره تلفن', max_length=20, null=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    Represent movie in cinema at specific time
    """

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, verbose_name='فيلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT, verbose_name='سينما')
    start_time = models.DateTimeField('زمان شروع نمايش')
    price = models.IntegerField('قيمت')
    salable_seats = models.IntegerField('صندل هاي قابل فروش')
    free_seats = models.IntegerField('صندلي خالي')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش شروع نشده'),
        (SALE_OPEN, 'در حال فروش بليط'),
        (TICKETS_SOLD, 'بليط تمام شد'),
        (SALE_CLOSED, 'فروش بليط بسته شد'),
        (MOVIE_PLAYED, 'فيلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )
    status = models.IntegerField('وضعيت', choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
