from os import path
import subprocess

class ActionType:

    READ = 'read'
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'

class FlagConst:

    TID = '-tid'
    QUERY = '-query'
    INFILE = '-infile'
    OUTFILE = '-outfile'

class UnitTester:

    def __init__(self):
        self.exe = 'tip-cli'
        self.infile = path.abspath(path.dirname(__file__) + 'data_dummy.csv')

    def create(self):
        output = subprocess.run(' '.join(
            [self.exe, ActionType.CREATE, FlagConst.INFILE, self.infile]),
            shell=True)
        return output

    def read_compound(self):
        output = subprocess.check_output(
            [self.exe, ActionType.READ, FlagConst.QUERY,
             'type:compound,common_names:Water,cid:962'])
        return output

    def read_assay(self):
        output = subprocess.check_output(
            [self.exe, ActionType.READ, FlagConst.QUERY,
             'type:assay,compound:1'])
        return output

    def update(self):
        output = subprocess.check_output(
            [self.exe, ActionType.UPDATE, FlagConst.TID, '1', FlagConst.QUERY,
             'type:compound,common_names:"Water;Ice"'])
        return output

    def delete_compound(self):
        output = subprocess.check_output(
            [self.exe, ActionType.DELETE, FlagConst.TID, '1', FlagConst.QUERY,
             'type:compound'])
        return output

    def delete_assay(self):
        output = subprocess.check_output(
            [self.exe, ActionType.DELETE, FlagConst.TID, '5', FlagConst.QUERY,
             'type:assay'])
        return output

    def test(self):
        # self.create()
        # self.read()
        # self.update()
        self.delete_assay()


if __name__ == '__main__':
    tester = UnitTester()
    tester.test()
