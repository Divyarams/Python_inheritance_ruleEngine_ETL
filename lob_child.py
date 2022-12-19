from common_parent import common_rule
class lob_child(common_parent):
  
  def __init__(self):
    # call super function to read parent rule file methods and attributes
    super().__init__()
    print('Parent class instantiated')
    
  def lob_rule1():
    global var1
    array_check=['CA','NY','LA']
    var1=df.filter(col('COL_NAME')).isin(array_check)).count()
    return var1
    
  def lob_rule2():
    global var2
    array_checksum=1000000
    if df.select(sum(col('COL_NAME'))) > array_checksum:
      var2=1
    else:
      var2=0
    return var2
   
rule_check=lob_child()
rule_check.check_null()
rule_check.check_notnull()
