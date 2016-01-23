import MySQLdb
import os
import webapp2

class IndexPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    if (os.getenv('SERVER_SOFTWARE') and
      os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
      db = MySQLdb.connect(unix_socket='/cloudsql/whats-4-dinner-1199:instance', user='root')
      self.response.write('connect db')
    else:
      db = MySQLdb.connect(host='localhost', user='root')
      self.response.write('connect db2')

    cursor = db.cursor()
    cursor.execute('SHOW VARIABLES')
    for r in cursor.fetchall():
      self.response.write('%s\n' % str(r))
    self.response.write('close db')
    db.close()

app = webapp2.WSGIApplication([
    ('/', IndexPage),
    ])
