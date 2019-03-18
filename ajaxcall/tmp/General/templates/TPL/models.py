class VOIP(models.Model):
  voip_name = models.CharField(max_length=255,default='')
  business_name =  models.CharField(default='Business Name',verbose_name='Business Name',null=True,blank=True)
  extension =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(1000),verbose_name='Extension' )
  locations =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100),verbose_name='Locations' )
  did_existing_local_number =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50),verbose_name='DiD Existing Local Number' )
  did_new_local_number =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50),verbose_name='DiD New Local Number' )
  fax_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(20),verbose_name='Fax Numbers' )
  current_phone_provider =  models.CharField(default='Current phone provider',verbose_name='Current phone provider',null=True,blank=True)
  number_of_employees =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(2000),verbose_name='Number of employees' )
  tfs_existing_toll_free_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50),verbose_name='TFs Existing Toll-Free Numbers' )
  tfs_new_toll_free_numbers =  models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(50),verbose_name='TFs New Toll-Free Numbers' )

  def __str__(self):
    return self.voip_name

  def get_display(self):
    content = { 'data' : self }
    return mark_safe(render_to_string('General/MODEL_TPL/voip.html' , content ))

  class Meta:
    verbose_name = 'VOIP'





### Template ####