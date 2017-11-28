from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    Terry = Professor(name='Terry', department='Finance department')
    Harry = Professor(name='Harry', department='ACCT and MISY department')
    Richard = Professor(name='Richard', department='Finance Department')
    finc415 = Course(coursenumber='FINC415', title='International Finance', professor_id=1, description='Examines the international monetary environment and its impact on financial planning for the firm. Topics include exchange rates, currency restrictions, tax regulations, direct investment theory, capital budgeting, financing, risk management, and working capital management')
    misy350 = Course(coursenumber='MISY350', title='Business Application Development', professor_id=2, description='Covers concepts related to client side development, including cascading style sheets and JavaScript')
    finc311 = Course(coursenumber='FINC311', title='Principle of Finance', professor_id=3, description='Introduces fundamental techniques and concepts related to the financial management of business firms. Topics include the time value of money, valuation, capital budgeting, working capital management, cost of capital, capital structure analysis, short and long term financing')
    finc419 = Course(coursenumber='FINC419', title='Financial Modeling', professor_id=3, description='Applies economic principles and financial modeling techniques to value seasoned equity, initial public offerings, mergers, private equity transactions, and leveraged buyouts')
    db.session.add(Terry)
    db.session.add(Harry)
    db.session.add(Richard)
    db.session.add(finc415)
    db.session.add(misy350)
    db.session.add(finc311)
    db.session.add(finc419)
    db.session.commit()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
