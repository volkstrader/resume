class ResumeOverview(object):
    def __init__(self, overview):
        self.general = overview['general']
        self.sections = overview['sections']
        self.skills = []

        skills = overview['skills']
        for skill in skills:
            self.skills.append(Skill(skill['key'], skill['values']))

    def description(self):
        return self.general['description']

    def responsibilities(self):
        return self.general['responsibilities']

class Skill(object):
    def __init__(self, key, values):
        self.key = key
        self.items = []
        d = u", "

        for v in values:
            if 'details' in v:
                s = { 'name': v['name'], 'score': v['score'], 'value': d.join(v['details']) }
                self.items.append(s)
        
        value = d.join(map(lambda v: self.format_value(v), filter(lambda v: 'details' not in v , values)))
        self.items.append({ 'value': value })

    def format_value(self, v):
        if 'score' not in v:
            return v['name']
        else:
            return v['name'] + '<span class="score">(' + str(v['score']) + ')</span>'
