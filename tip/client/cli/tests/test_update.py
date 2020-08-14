import json
import subprocess


class UnitTester:

    def __init__(self):
        self.exe = 'tip-cli'
        self.action = 'update'
        self.tid_flag = '-tid'
        self.query_flag = '-query'

    def update_compound(self):
        tid = '5f360c170d5b10949c15b40e'
        query = 'type:compound,common_names:"Ice;Dihydrogen oxide"'
        output = subprocess.check_output([self.exe, self.action, self.tid_flag,
                                          tid, self.query_flag, query])
        output = json.loads(output.decode())
        assert [output['common_names'], output['iupac_name']] == \
            [["Ice", "Dihydrogen oxide"], "Oxidine"]

    def update_assay(self):
        tid = '5f360c170d5b10949c15b40c'
        query = 'type:assay,pmid:12345678;12121313'
        output = subprocess.check_output([self.exe, self.action, self.tid_flag,
                                          tid, self.query_flag, query])
        output = json.loads(output.decode())
        assert [output['pmid'], output['protein']] == \
            [[12345678, 12121313], "mEHh"]

    def test(self):
        self.update_compound()
        self.update_assay()
        print('Success!')


if __name__ == '__main__':
    tester = UnitTester()
    tester.test()
