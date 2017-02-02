import requests
from datetime import datetime
from threading import Timer

#set up timer and set what time to go off at periodically
x=datetime.today()
#i chose 7 am daily
y=x.replace(day=x.day+1, hour=7, minute=0, second=0, microsecond=0)
#get the time difference for when to execute t.start()
delta_t=y-x

secs=delta_t.seconds+1

def post_job():
    #subject and context strings for the job posting
    sub = ""
    con = ""
    #category, can be either Full time or Part time
    cat = 'Part time'

    #gain a session and add headers
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
    })
    #get cookies from radiokorea
    response = session.get('http://www.radiokorea.com')
    #post login information
    response = session.post('http://www.radiokorea.com/account/signin_home.php', data={
        'id': "",
        'pw': ""
    }, allow_redirects=False)

    #check cookie to see if login successful, dunno why clubgame is the name of their logged in variable
    if 'clubgame' in response.cookies:
        print "success!"

        #add post params for the form
        response1 = session.post('http://www.radiokorea.com/bulletin/bbs/write_update.php', data={
            'ca_name': cat,
            'wr_subject': sub,
            'wr_content': con,
            'bo_table': 'c_findjobs'
        }, allow_redirects=False)

t = Timer(secs, post_job)
t.start()