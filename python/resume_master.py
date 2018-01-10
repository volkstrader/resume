import yaml

from pystache import TemplateSpec
from resume_overview import ResumeOverview

class ResumeMaster(object):
    def __init__(self):
        with open('../data/summary.yaml') as f:
            self.summary = yaml.safe_load(f)
            self.overview = ResumeOverview(self.summary['overview'])
            self.recognitions = self.summary['recognitions']
            self.education = self.summary['education']
            self.history = self.summary['history']
            self.experiences = []

        for h in self.history:
            with open("../data/{0}.yaml".format(h['id'])) as f:
                projects = yaml.safe_load(f)

                if projects:
                    exp = {
                        'company': h['company'],
                        'office': h['office'],
                        'title': h['title'],
                        'projects': projects
                    }
                    self.experiences.append(exp)

    def profile(self):
        return self.summary['profile']

    def profileName(self):
        return self.profile()['name']

    def home(self):
        return self.profile()['home']

    def phone(self):
        return self.profile()['phone']

    def email(self):
        return self.profile()['email']

    def linkedin(self):
        return self.profile()['linkedin']    

    def github(self):
        return self.profile()['github']