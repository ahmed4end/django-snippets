class NameModelAdmin(ModelAdmin):
    model = MODLENAME
	inlines = [MODLENAMEInLine,]
	date_hierarchy = 'models.Field'
    fields = () # or exclyde = ()
    
    @admin.display(description='TITLE')
	def upper_case_name(obj):
	    return str(obj).upper()
    
	list_display = ('content', 'author', upper_case_name)
    
