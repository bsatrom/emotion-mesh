import pymysql
import time
from . import db_config as config

def createResult(img, faceDictionary):
  print('Connecting to DB to save result')
  connection = pymysql.connect(host='localhost', 
                            user=config.db_user,
                            password=config.db_pw,
                            database=config.db_name)
  
  print(faceDictionary)

  try:
    with connection.cursor() as cursor:
        for face in faceDictionary:
          sql = "INSERT INTO `result` (`img`, `anger`, `contempt`, `disgust`, `fear`, \
                                      `happiness`, `neutral`, `sadness`, `surprise`, \
                                      `created`) VALUES (%s, %s, %s, %s, %s, %s, %s, \
                                        %s, %s, %s)"
          cursor.execute(sql, (img, face['anger'], face['contempt'], face['disgust'], 
                              face['fear'], face['happiness'], face['neutral'], face['sadness'], 
                              face['surprise'], time.strftime('%Y-%m-%d %H:%M:%S')))

    connection.commit()
  finally:
      connection.close()

def saveResponse(img, correct):
  print('Connecting to DB to update with user response for ' + img + ' and result ' + str(correct))
  connection = pymysql.connect(host='localhost', 
                            user=config.db_user,
                            password=config.db_pw,
                            database=config.db_name)
  
  try: 
    with connection.cursor() as cursor:
          sql = "UPDATE `result` SET `correct`=%s WHERE `img`=%s"
          cursor.execute(sql, (correct, img))

    connection.commit()
  finally:
      connection.close()

def getLastResult():
  result = None
  print('Connecting to DB to fetch last result')
  connection = pymysql.connect(host='localhost', 
                            user=config.db_user,
                            password=config.db_pw,
                            database=config.db_name)
  
  try: 
    with connection.cursor() as cursor:
          sql = "SELECT * from `result` ORDER BY `created` DESC"
          cursor.execute(sql)
          result = cursor.fetchone()

    connection.commit()
  finally:
      connection.close()

  return result

def getStats(): 
  result = {
    'total': 0.0,
    'correct': 0.0,
    'incorrect': 0.0,
    'anger': 0.0,
    'neutral': 0.0,
    'happiness': 0.0,
    'contempt': 0.0,
    'disgust': 0.0,
    'fear': 0.0,
    'sadness': 0.0,
    'surprise': 0.0
  }
  connection = pymysql.connect(host='localhost', 
                            user=config.db_user,
                            password=config.db_pw,
                            database=config.db_name)
  
  try: 
    with connection.cursor() as cursor:
          # get the total # of records
          sql = "SELECT COUNT(*) from `result`"
          cursor.execute(sql)
          result['total'] = cursor.fetchone()

          #get the number incorrect
          sql = "SELECT COUNT(*) from `result` WHERE `correct`=0"
          cursor.execute(sql)
          result['incorrect'] = cursor.fetchone()

          #get the number correct
          sql = "SELECT COUNT(*) from `result` WHERE `correct`=1"
          cursor.execute(sql)
          result['correct'] = cursor.fetchone()

          #get averages
          sql = "SELECT AVG(anger) AS anger, AVG(neutral) as neutral, AVG(happiness) as happiness,\
                AVG(contempt) AS contempt, AVG(disgust) as disgust, AVG(fear) as fear, AVG(sadness) \
                as sadness, AVG(surprise) as surprise from result"
          cursor.execute(sql)
          avgs = cursor.fetchone()
          result['anger'] = avgs[0]
          result['neutral'] = avgs[1]
          result['happiness'] = avgs[2]
          result['contempt'] = avgs[3]
          result['disgust'] = avgs[4]
          result['fear'] = avgs[5]
          result['sadness'] = avgs[6]
          result['surprise'] = avgs[7]

    connection.commit()
  finally:
      connection.close()

  return result