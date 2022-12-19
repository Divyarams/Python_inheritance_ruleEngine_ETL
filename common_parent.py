class common_rule:
  def __init__(self):
    print('Common Rule parent')
    
  def check_null(self):
    global cnull
    cnull=df.filter(col('COL_NAME').isNull()).count()
    return cnull
  
  def check_notnull(self):
    global cnotnull
    cnotnull=df.filter(col('COL_NAME'),isNotNull()).count()
    return cnotnull
  # instantiate class methods
  start=common_rule()
    
