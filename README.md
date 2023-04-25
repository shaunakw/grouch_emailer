# Grouch emailer

Sends you and your friends emails when courses open/close.

Uses code from [https://github.com/JIceberg/grouch](https://github.com/JIceberg/grouch) to scrape OSCAR.

### config.json format

- `season`: Which season to search classes for. Set to either "fall", "spring", or "summer"
- `notifiers`: List of notifier objects. Each notifier object should contain the following:
  - `crn`: CRN for the course (as a string)
  - `emails`: List of emails to notify for updates to the course
- `yagmail`: Configuration for yagmail
  - `user`: Google email to use to send updates
  - `password`: Password for the email (must use app password)
