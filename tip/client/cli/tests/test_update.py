import json
import subprocess


class UnitTester:

    def __init__(self):
        self.exe = 'tip-cli'
        self.action = 'update'
        self.tid_flag = '-tid'
        self.query_flag = '-query'

    def update_compound(self):
        action = 'update'
        tid = '5f360c170d5b10949c15b40e'
        query = 'type:compound,comment:"You can spill it."'
        output = subprocess.check_output([self.exe, self.action, self.tid_flag,
                                          tid, self.query_flag, query])
        output = json.loads(output.decode())
        assert [output['common_names'], output['iupac_name'],
                output['comment']] == \
               [["Water","Dihydrogen oxide"], "Oxidine", "You can spill it."]

    def update_assay(self):
        action = 'update'
        tid = '5f360c170d5b10949c15b40c'
        query = 'type:assay,comment:"You can freeze it.",species:doggy'
        output = subprocess.check_output([self.exe, self.action, self.tid_flag,
                                          tid, self.query_flag, query])
        output = json.loads(output.decode())
        assert [output['pmid'], output['protein'],
                output['comment']] == \
               [[12345678], "mEHh", "You can freeze it."]

    def test(self):
        self.update_compound()
        self.update_assay()
        print('Success!')

if __name__ == '__main__':
    tester = UnitTester()
    tester.test()
