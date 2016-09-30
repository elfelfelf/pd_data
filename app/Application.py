

class App(object):

    def __init__(self):
        pass


class AppData():

    def __init__(self, name, sub_dir, file_ext):
        self.name = name

        self.file_ext = file_ext
        self.base_dir = r''
        self.dir = self.base_dir + sub_dir
        self.file_path = self.dir + self.name + self.file_ext
        pass



class Project(AppData):

    def __init__(self, name):
        super(appProject, self).__init__(name, r'Projects\\{}'.format(name), '.enc')


class Dataset(AppData):

    def __init__(self, name, project):
        self.project = project
        super(Dataset, self).__init__(name, r'{}\\Datasets\\'.format(self.project.name,name), '.dset')


class Macro(AppData):

    def __init__(self):
        super(Dataset, self).__init__(name, r'{}\\Macros\\'.format(project_name,name), '.csf')
        pass


class Report(AppData):

    def __init__(self):
        pass
