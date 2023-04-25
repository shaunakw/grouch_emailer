import json
import yagmail

from grouch.courses import Course
from grouch.term import get_term

class Notifier:
  def __init__(self, crn: str, term: str, emails: list[str]):
    self.course = Course(crn, term)
    self.term = term
    self.emails = emails

    self.spots = 0
    self.wl_spots = 0
  
  def fetch_info(self):
    info = self.course.get_registration_info(self.term)
    self.spots = info['vacant']
    self.wl_spots = info['waitlist']['vacant']

smtp: yagmail.SMTP

def load_notifiers() -> list[Notifier]:
  global smtp

  with open('config.json') as config_json:
    config = json.load(config_json)

    smtp = yagmail.SMTP(config['yagmail']['user'], config['yagmail']['password'])

    term = get_term(config['season'])
    notifiers = [Notifier(i['crn'], term, i['emails']) for i in config['notifiers']]
    return notifiers

def notify(notifier: Notifier, contents: list[str]):
  subject = f'Registration Update: {notifier.course.name}'
  smtp.send(bcc=notifier.emails, subject=subject, contents=contents)
  print(f'Notified {len(notifier.emails)} people about {notifier.course.crn}')
