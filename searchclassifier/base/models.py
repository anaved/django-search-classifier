
from django.contrib.gis.db import models
from django.contrib.gis.geos.point import Point
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models as djangomodels
from django.template.defaultfilters import slugify
import warnings
from datetime import date

class BaseModelMin(djangomodels.Model):
    '''
     Used for supporting models, which are perceived to be never converted into main models.     
    '''
    is_active = djangomodels.BooleanField(default=True)
    added = djangomodels.DateTimeField(auto_now_add=True)            
    timestamp = djangomodels.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

#
class BaseModel(BaseModelMin):
    '''
     Used for models which gets converted into pages, most of the models come under this category.     
    '''
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, db_index=True)
    manual_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)    
    page_title = models.TextField(null=True, blank=True)
    page_meta_desc = models.TextField(null=True, blank=True)
    page_meta_key = models.TextField(null=True, blank=True) 
    page_header = models.TextField(null=True, blank=True)    
    
    def __unicode__(self):
        return self.name
    
    def get_index_letter(self):
        return self.name and self.name.strip()[0].upper() or ''
    index_letter = property(get_index_letter)
        
    def get_slug(self):
        '''
        Returns name as slug, most of the models may need to override this
        '''
        return slugify(self.name)
    
    def get_page_header(self):
        '''
        Returns page header as name, most of the models may need to override this
        '''
        return self.name
    def save(self, force_insert=False, force_update=False, ** kwargs):
        if not self.slug:                
            self.slug = self.get_slug()
        if not self.page_header:
            self.page_header = self.get_page_header()
        super(BaseModel, self).save(force_insert, force_update, ** kwargs)
                 
    class Meta:
        abstract = True
        ordering = ['name', ]
                
class BaseGeoModel(BaseModel):
    lat = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(+90.0)])
    lng = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(+180.0)])  
    point = models.PointField(null=True, db_index=True)
    objects = models.GeoManager()
    
    def get_point(self):
        # Remember, longitude FIRST!
        if (self.lat and self.lng):
            return Point(self.lng, self.lat)
        else:
            warnings.warn("No latitude longitude provided, returning empty point.", UserWarning)                
            return Point(0, 0)
    
    def save(self, force_insert=False, force_update=False, ** kwargs):
        self.point = self.get_point()
        super(BaseGeoModel, self).save(force_insert, force_update, ** kwargs)
                
    class Meta:
        abstract = True


# default method to get file upload path
def get_upload_to(instance, filename):
    return instance.upload_to(filename)

class BaseImageModel(BaseModelMin):    
    '''
    Base model for banners and slideshows.
    We can create one extra field attched_to to attached a slideshow with a model.     
    '''
    name = models.TextField(blank=True, null=True)   
    subtitle = models.CharField(max_length=555, blank=True, null=True)    
    target_url = models.URLField(null=True, blank=True)    
    priority = models.IntegerField(default=0)
    html_content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    image = models.ImageField(upload_to=get_upload_to, max_length=555)
    def upload_to(self, filename):
#       PATH RELATIVE TO MEDIA_ROOT
        t = date.today()
        f = filename.split('.')
        name = slugify(' '.join(f[:-1])) + '.' + f[-1] 
        return 'master/img/misc/' + str(t.year) + '/' + str(t.month) + '/' + name       
    class Meta:
        abstract = True    
    
