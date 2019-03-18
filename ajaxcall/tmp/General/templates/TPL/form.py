class VOIP_Form(forms.ModelForm):
  class Meta:
    model = VOIP
    fields = (
      'business_type',
      'business_name',
      'extension',
      'locations',
      'did_existing_local_number',
      'did_new_local_number',
      'fax_numbers',
      'current_phone_provider',
      'number_of_employees',
      'tfs_existing_toll_free_numbers',
      'tfs_new_toll_free_numbers'
    )