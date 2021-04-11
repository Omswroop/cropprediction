from django.db import models


class pred_one(models.Model):
    crop=models.CharField(max_length=15)
    Gross_Production_Value_constant_2004_2006_1000_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Net_Production_Value_constant_2004_2006_1000_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_current_million_SLC=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_constant_2004_2006_million_SLC=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_current_million_US_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_constant_2004_2006_million_US_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)

    def __str__(self):
    	return self.crop


class prod_area(models.Model):
    state=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    crop=models.CharField(max_length=25)
    org_val=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    pred_val=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)

    def __str__(self):
    	return '%s %s %s' % (self.state, self.district, self.crop)


class one(models.Model):
    crop=models.CharField(max_length=15)
    Gross_Production_Value_constant_2004_2006_1000_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Net_Production_Value_constant_2004_2006_1000_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_current_million_SLC=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_constant_2004_2006_million_SLC=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_current_million_US_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    Gross_Production_Value_constant_2004_2006_million_US_dollar=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)

    def __str__(self):
    	return self.crop


class two(models.Model):
    crop=models.CharField(max_length=25)
    area_harvested=models.IntegerField()
    yieldd=models.IntegerField()
    production=models.IntegerField()

    def __str__(self):
    	return self.crop


class three(models.Model):
    crop=models.CharField(max_length=15)
    Production=models.IntegerField()
    Imports=models.IntegerField()
    Stock=models.IntegerField()
    Export=models.IntegerField()
    Seed=models.IntegerField()
    Domestic=models.IntegerField()

    def __str__(self):
    	return self.crop


class pred_three(models.Model):
    crop=models.CharField(max_length=15)
    imports=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    exports=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    production=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    production_mean=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    imports_mean=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)
    exports_mean=models.DecimalField(max_digits=12,decimal_places=4,default=0.0)

    def __str__(self):
    	return self.crop



class Users(models.Model):
    emp_id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,default="None")
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50,help_text="Minimum of 8 Characters")
    phone = models.CharField(max_length=20)
    ques_1_id = models.CharField(max_length=5)
    ans_1 = models.CharField(max_length=50)
    ques_2_id = models.CharField(max_length=5)
    ans_2 = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_id+";"+self.name+";"+self.gender+";"+self.email+";"+self.password+";"+self.phone+";"+self.ques_1_id+";"+self.ans_1+";"+self.ques_2_id+";"+self.ans_2
