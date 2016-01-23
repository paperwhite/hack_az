import MySQLdb
import _mysql
import os
import webapp2

class Page(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    if (os.getenv('SERVER_SOFTWARE') and
      os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
      db = MySQLdb.connect(unix_socket='/cloudsql/whats-4-dinner-1199:instance', user='root')
    else:
      db = MySQLdb.connect(host='localhost', user='root')

    db.query('SHOW VARIABLES')
    result = db.store_result()
    while True:
      row = result.fetch_row()
      if row:
        self.response.write('%s\n' % str(row[0]))
      else:
        break

    db.close()

app = webapp2.WSGIApplication([
    ('/mysql', Page),
    ])
